from rest_framework import serializers
from asset.models import AssetModel


class AssetsOnlyNameAndCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model: AssetModel = AssetModel
        fields: str = 'code', 'name'
