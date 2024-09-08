from rest_framework.generics import ListAPIView
from offer.models import OfferOwnershipModel
from offer.api.serializers import ShareOwnershipSerializer


class OfferOwnerListView(ListAPIView):
    serializer_class = ShareOwnershipSerializer
    queryset = OfferOwnershipModel.objects.all()
