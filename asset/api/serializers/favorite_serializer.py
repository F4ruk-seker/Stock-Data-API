from rest_framework import serializers
from asset.models import FavoriteAssetModel


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteAssetModel
        fields: list = 'asset',
