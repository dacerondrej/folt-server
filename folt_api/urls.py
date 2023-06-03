from django.urls import path, include
from .views import (
    CustomerListApiView,
    CourierListApiView,
    NationalTradeRegistryApiView,
    OfferApiView,
    PickupListApiView,
)

urlpatterns = [
    path('api', CustomerListApiView.as_view()),
    path('couriers', CourierListApiView.as_view()),
    path('ntr/checkSubject', NationalTradeRegistryApiView.as_view()),
    path('last-offer', OfferApiView.as_view()),
    path('pickups', PickupListApiView.as_view()),
]