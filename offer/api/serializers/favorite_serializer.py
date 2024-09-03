from rest_framework import serializers
from offer.models import FavoriteOfferModel


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteOfferModel
        fields: list = 'user', 'offer'
