from rest_framework.generics import ListAPIView
from offer.api.serializers import OfferSerializer
from offer.models import OfferModel


class OfferListView(ListAPIView):
    queryset = OfferModel.objects.all()
    serializer_class = OfferSerializer
