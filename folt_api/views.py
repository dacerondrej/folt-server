from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Customer, Courier, Offer, OfferItem, Pickup
from .serializers import CustomerSerializer, CourierSerializer, OfferSerializer, PickupSerializer
import json

class CustomerListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all customers
        '''
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create customer
        '''
        data = {
            'name': request.data.get('name'), 
            'email': request.data.get('email'), 
        }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourierListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all couriers
        '''
        couriers = Courier.objects.all()
        serializer = CourierSerializer(couriers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create courier
        '''
        data = {
            'name': request.data.get('name'), 
            'email': request.data.get('email'), 
        }
        serializer = CourierSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NationalTradeRegistryApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        Return NTR subject check
        '''
        subject_data = {
            'error': '',
            'approved': True
        }
        return Response(subject_data, status=status.HTTP_200_OK)

class OfferApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        Get last offer
        '''
        last_offer = Offer.objects.latest('offer_id')
        serializer = OfferSerializer(last_offer, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create offer
        '''
        data = {
            'state': request.data.get('state'), 
            'items': request.data.get('items'), 
        }
        serializer = OfferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PickupListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all pickups
        '''
        pickups = Pickup.objects.all()
        serializer = PickupSerializer(pickups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create pickup
        '''
        data = {
            'offer_id': request.data.get('offer_id'), 
            'courier_email': request.data.get('courier_email'), 
        }
        serializer = PickupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)