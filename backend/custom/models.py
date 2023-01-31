from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields as generic


class Attribute(models.Model):
    organization = models.ForeignKey("main.Organization", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_required = models.BooleanField(default=False)
    type = models.CharField(max_length=255, default="text")

    # min
    # max
    # max_length
    # label

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, related_name='ct_attribute_values')
    object_id = models.IntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.value


class ContactMixin(object):
    @property
    def custom_fields(self):
        from main.models import Order
        c_type = ContentType.objects.get_for_model(self.__class__)
        try:
            data = AttributeValue.objects.filter(content_type__pk=c_type.id, object_id=self.id)
        except AttributeValue.DoesNotExist:
            return None
        return data
