from django.db import models
from django.contrib.contenttypes.models import ContentType

import eav

from custom.models import ContactMixin


class Organization(models.Model):
    code = models.CharField(max_length=20, unique=True)
    order_fields = models.JSONField()

    def __str__(self):
        return self.code


class Order(ContactMixin, models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=20)

    def __str__(self):
        return self.reference_number


eav.register(Order)
