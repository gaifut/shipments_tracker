from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CustomUserViewSet, TruckViewSet, ShipmentViewSet,
    LogbookShipmentViewSet
)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('users', CustomUserViewSet, basename='users')
router_v1.register('trucks', TruckViewSet, basename='trucks')
router_v1.register('shipments', ShipmentViewSet, basename='shipments')
router_v1.register('logbook', LogbookShipmentViewSet, basename='logbook')

urlpatterns = [
    path('', include(router_v1.urls)),
]
