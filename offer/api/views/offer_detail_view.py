from rest_framework.generics import RetrieveAPIView
from offer.models import OfferModel
from offer.api.serializers import OfferDetailSerializer


class OfferDetailView(RetrieveAPIView):
    lookup_field = 'code'
    queryset = OfferModel.objects.all()
    serializer_class = OfferDetailSerializer
