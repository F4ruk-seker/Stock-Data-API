from rest_framework import serializers
from asset.models.asset_model import AssetPriceModel


class AssetPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetPriceModel
        # fields: str = '__all__'
        exclude: tuple = 'id',
