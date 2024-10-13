from asset.api.serializers import AssetSerializer
from asset.api.serializers.asset_price_flow_serializer import AssetPriceSerializer
from asset.models import AssetModel


class AssetDetailSerializer(AssetSerializer):
    price_flow = AssetPriceSerializer(many=True)

    class Meta:
        model = AssetModel
        exclude: tuple = 'updated_by',
