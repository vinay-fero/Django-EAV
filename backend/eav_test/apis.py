from rest_framework.routers import DefaultRouter

from main import views as main_views
from custom import views as custom_views

router = DefaultRouter()
router.register("eav/order", main_views.OrderViewSet, basename="eav_order")

router.register("organization", custom_views.OrganizationViewSet, basename="organization")
router.register("order", custom_views.OrderViewSet, basename="order")

urlpatterns = []

urlpatterns += router.urls
