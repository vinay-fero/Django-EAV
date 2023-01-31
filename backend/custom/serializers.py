from rest_framework import serializers

from custom.models import Attribute, AttributeValue
from main.models import Order, Organization
from django.contrib.contenttypes.models import ContentType


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("id", "code", "order_fields")

    def create(self, validated_data):
        order_fields = validated_data.get("order_fields")
        organization = super().create(validated_data=validated_data)

        for key, value in order_fields.items():
            Attribute.objects.create(organization=organization, name=key, **value)

        return organization


class OrderCustomFieldSerializer(serializers.ModelSerializer):
    custom_fields = serializers.JSONField(write_only=True)

    class Meta:
        model = Order
        fields = ("id", "organization", "reference_number", "custom_fields")

    def create(self, validated_data):
        custom_fields = validated_data.pop("custom_fields", {})

        order = super().create(validated_data=validated_data)

        for key, value in custom_fields.items():
            AttributeValue.objects.create(
                attribute=Attribute.objects.get(name=key),
                value=value,
                content_type=ContentType.objects.get_for_model(order.__class__),
                object_id=order.id,
            )

            # setattr(order.eav, key, value)

        return order

    def to_representation(self, instance):
        response = super().to_representation(instance=instance)

        custom_fields = instance.custom_fields.values("attribute__name", "value")

        response.update({"custom_fields": custom_fields})

        return response
