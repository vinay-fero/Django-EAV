from rest_framework.viewsets import ModelViewSet

from main.models import Order, Organization
from custom.serializers import OrderCustomFieldSerializer, OrganizationSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCustomFieldSerializer
