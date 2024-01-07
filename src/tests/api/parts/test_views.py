import pytest
from api.parts.serializers import PartOutputSerializer
from django.conf import settings
from django.contrib.auth.models import Permission, User
from django.shortcuts import resolve_url
from model_bakery import baker
from part.constants import SOURCE_TEGIWA
from part.models import Part, Stock
from rest_framework import status
from rest_framework.authtoken.models import Token

REFERENCE_1 = "56483-PND-003"
TITLE_1 = "Head Gasket"
TITLE_3 = "Cover"
REFERENCE_2 = "14721-PRB-A00"
TITLE_2 = "Oil Pump"


@pytest.mark.django_db
class TestsPartsView:
    def endpoint(self, reference):
        return resolve_url("api:parts-detail", reference=reference)

    def test_url(self):
        baker.make(Part, reference=REFERENCE_1, source=SOURCE_TEGIWA)

        assert (
            self.endpoint(REFERENCE_1.lower()) == f"/api/parts/{REFERENCE_1.lower()}/"
        )

    def test_success(self, client):
        part = baker.make(Part, reference=REFERENCE_1, source=SOURCE_TEGIWA)
        baker.make(Stock, part=part, source=SOURCE_TEGIWA, country="US")
        response = client.get(self.endpoint(REFERENCE_1.lower()))

        assert response.status_code == status.HTTP_200_OK
        assert response.data == PartOutputSerializer(part).data


@pytest.mark.django_db
class TestsPartsToScrapView:
    endpoint = resolve_url("api:to-scrap")

    @pytest.fixture(autouse=True)
    def setup_class(self):
        user = baker.make(User)
        user.user_permissions.add(Permission.objects.get(name="Can view part"))
        self.token = baker.make(Token, user=user)

    def test_url(self):
        assert self.endpoint == "/api/parts/to-scrap/"

    def test_no_token(self, client):
        response = client.get(self.endpoint)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_success(self, client):
        """
        we call two times the endpoint because the field "last_time_delivered" should change in the second one
        """
        part = baker.make(Part, reference=REFERENCE_1, source=SOURCE_TEGIWA)
        response = client.get(self.endpoint, HTTP_AUTHORIZATION=f"Token {self.token}")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == PartOutputSerializer(part).data
        assert response.data["last_time_delivered"] is None

        part.refresh_from_db()
        response = client.get(self.endpoint, HTTP_AUTHORIZATION=f"Token {self.token}")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == PartOutputSerializer(part).data
        assert response.data[
            "last_time_delivered"
        ] == part.last_time_delivered.astimezone().strftime(
            settings.REST_FRAMEWORK["DATETIME_FORMAT"]
        )
