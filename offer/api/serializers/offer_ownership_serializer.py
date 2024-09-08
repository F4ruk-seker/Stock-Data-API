from rest_framework import serializers
from offer.models import OfferOwnershipModel
from .offer_serializer import OfferSerializer
from .slot_serializer import SlotSerializer


class ShareOwnershipSerializer(serializers.ModelSerializer):
    offer = OfferSerializer(read_only=True)
    slots = SlotSerializer(read_only=True, many=True)
    general_status = serializers.SerializerMethodField()

    @staticmethod
    def get_general_status(obj):
        remaining_lots = 0
        total_profit = 0
        for transaction in obj.slots.all():
            if transaction.progres_type == transaction.ProgresType.BUY:
                remaining_lots += transaction.quantity
            else:
                sold_lots = transaction.quantity
                sale_price = float(transaction.price)
                profit = sold_lots * (sale_price - float(obj.offer.current_price))
                total_profit += profit
                remaining_lots -= sold_lots
        return {
            'total_profit': total_profit,
            'remaining_lots': remaining_lots
        }

    class Meta:
        model = OfferOwnershipModel
        fields: str = '__all__'
