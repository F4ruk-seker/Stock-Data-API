from rest_framework import serializers
from offer.models.offer_model import OfferPriceModel


class OfferPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferPriceModel
        # fields: str = '__all__'
        exclude: tuple = 'id',
