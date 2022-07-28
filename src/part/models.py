from django.core.exceptions import ValidationError
from django.db import models
from django_extensions.db.models import TimeStampedModel
from djmoney.models.fields import MoneyField

from part.constants import PART_SOURCES, STOCK_SOURCES


class Part(TimeStampedModel):
    reference = models.CharField(unique=True, max_length=13, default=None)
    source = models.CharField(choices=PART_SOURCES, max_length=20)

    def save(self, **kwargs):
        if self.reference == "":
            raise ValidationError("Empty reference")
        super().save(**kwargs)

    def __str__(self):
        return self.reference


class Stock(TimeStampedModel):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    price = MoneyField(max_digits=10, null=True, default_currency=None)
    available = models.BooleanField(null=True, default=None)
    discontinued = models.BooleanField(null=True, default=None)
    source = models.CharField(choices=STOCK_SOURCES, max_length=20)

    def __str__(self):
        return self.part.reference


class Image(models.Model):
    url = models.URLField(default=None, unique=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def save(self, **kwargs):
        if self.url == "":
            raise ValidationError("Empty url")
        super().save(**kwargs)
