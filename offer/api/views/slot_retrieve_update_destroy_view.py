from rest_framework.generics import RetrieveUpdateDestroyAPIView
from offer.api.serializers import SlotSerializer
from offer.models import OfferOwnershipModel
from django.shortcuts import get_object_or_404


class SlotRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = SlotSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        code = self.kwargs.get('code')
        user = self.request.user
        offer_owner = get_object_or_404(OfferOwnershipModel, owner=user, offer=code)
        return offer_owner.slots.filter(pk=pk)
