from rest_framework import serializers
from asset.models import AssetOwnershipModel
from .asset_serializer import AssetSerializer
from .slot_serializer import SlotSerializer


class ShareOwnershipSerializer(serializers.ModelSerializer):
    asset = AssetSerializer(read_only=True)
    slots = SlotSerializer(read_only=True, many=True)
    general_status = serializers.SerializerMethodField()


    @staticmethod
    def get_general_status(obj):
        return obj.get_general_status()
        # remaining_lots = 0
        # total_profit = 0
        # for transaction in obj.slots.all():
        #     if transaction.progres_type == transaction.ProgresType.BUY:
        #         remaining_lots += transaction.quantity
        #     else:
        #         sold_lots = transaction.quantity
        #         sale_price = float(transaction.price)
        #         profit = sold_lots * (sale_price - float(obj.asset.current_price))
        #         total_profit += profit
        #         remaining_lots -= sold_lots
        # return {
        #     'total_profit': total_profit,
        #     'remaining_lots': remaining_lots
        # }

    class Meta:
        model = AssetOwnershipModel
        fields: str = '__all__'
