from rest_framework import serializers
from .models import Customer, Courier, Offer, OfferItem, Pickup

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['name', 'email']

class OfferItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferItem
        fields = ['name', 'unit', 'amount', 'price']

class OfferSerializer(serializers.ModelSerializer):
    items = OfferItemSerializer(many=True)

    class Meta:
        model = Offer
        fields = ['offer_id', 'state', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        offer = Offer.objects.create(**validated_data)
        for item_data in items_data:
            OfferItem.objects.create(offer=offer, **item_data)
        return offer

class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pickup
        fields = ['offer_id', 'courier_email']
