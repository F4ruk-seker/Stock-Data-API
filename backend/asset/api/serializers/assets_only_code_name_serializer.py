from rest_framework import serializers
from asset.models import AssetModel


class AssetsOnlyNameAndCodeSerializer(serializers.ModelSerializer):
    # logo = serializers.SerializerMethodField()
    #
    # def get_logo(self, i):
    #     return i.logo if 'placeholder' in i.logo else 'None'

    class Meta:
        model: AssetModel = AssetModel
        fields: str = 'code', 'name', 'logo'
