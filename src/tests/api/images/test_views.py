import pytest
from api.images.serializers import ImageSerializer
from django.contrib.auth.models import Permission, User
from django.shortcuts import resolve_url
from model_bakery import baker
from part.constants import SOURCE_TEGIWA
from part.models import Image, Part, Stock
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ErrorDetail

REFERENCE = "56483-PND-003"


@pytest.mark.django_db
class TestsImagesCreateView:
    endpoint = resolve_url("api:images-create")

    @pytest.fixture(autouse=True)
    def setup_class(self):
        user = baker.make(User)
        user.user_permissions.add(Permission.objects.get(name="Can add part"))
        self.token = baker.make(Token, user=user)

    def test_url(self):
        assert self.endpoint == "/api/images/"

    def test_success(self, client):
        assert not Image.objects.exists()

        part = baker.make(Part, reference=REFERENCE, source=SOURCE_TEGIWA)
        stock = baker.make(Stock, part=part, source=SOURCE_TEGIWA, country="US")
        response = client.post(
            self.endpoint,
            {"stock": stock.id, "url": "http://www.foo.com"},
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == ImageSerializer(Image.objects.get()).data
        assert Image.objects.count() == 1

    def test_duplicated_images(self, client):
        """Duplicated images per stock are not allowed"""

        part = baker.make(Part, reference=REFERENCE, source=SOURCE_TEGIWA)
        stock = baker.make(Stock, part=part, source=SOURCE_TEGIWA, country="US")
        image = "http://www.foo.com"
        response = client.post(
            self.endpoint,
            {"stock": stock.id, "url": image},
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )

        assert response.status_code == status.HTTP_201_CREATED

        response = client.post(
            self.endpoint,
            {"stock": stock.id, "url": image},
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {
            "url": [
                ErrorDetail(string="image with this url already exists.", code="unique")
            ]
        }
