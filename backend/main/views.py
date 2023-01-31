from rest_framework.viewsets import ModelViewSet

from main.models import Order
from main.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
