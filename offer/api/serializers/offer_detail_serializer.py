from offer.api.serializers import OfferSerializer
from offer.api.serializers.offer_price_flow_serializer import OfferPriceSerializer
from offer.models import OfferModel


class OfferDetailSerializer(OfferSerializer):
    price_flow = OfferPriceSerializer(many=True)

    class Meta:
        model = OfferModel
        exclude: tuple = 'updated_by',
