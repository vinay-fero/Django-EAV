from eav.models import Attribute
from rest_framework import serializers

from main.models import Order


class OrderSerializer(serializers.ModelSerializer):
    custom_fields = serializers.JSONField(write_only=True)

    class Meta:
        model = Order
        fields = ("id", "organization", "reference_number", "custom_fields")

    def create(self, validated_data):
        Attribute.objects.create(name="voyage_id", datatype=Attribute.TYPE_TEXT)
        # Attribute.objects.create(name="unit_name", datatype=Attribute.TYPE_TEXT)

        custom_fields = validated_data.pop("custom_fields", {})

        order = super().create(validated_data=validated_data)

        for key, value in custom_fields.items():
            setattr(order.eav, key, value)

        order.save()

        return order

    def to_representation(self, instance):
        response = super().to_representation(instance=instance)

        # organization = instance.organization
        # organization_fields = organization.order_fields

        custom_fields_data = instance.eav_values.values("attribute__name", "value_text")

        response.update({"custom_fields_data": custom_fields_data})

        return response
