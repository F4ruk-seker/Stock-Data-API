from rest_framework.generics import CreateAPIView
from offer.api.serializers import SlotSerializer
from offer.models import SlotModel, OfferOwnershipModel
from django.shortcuts import get_object_or_404


class SlotCreateView(CreateAPIView):
    serializer_class = SlotSerializer
    queryset = SlotModel.objects.all()

    def perform_create(self, serializer, *args, **kwargs):
        code = self.kwargs.get('code')
        user = self.request.user
        if offer_owner := get_object_or_404(OfferOwnershipModel, owner=user, offer=code):
            new_slot = serializer.save()
            offer_owner.slots.add(new_slot)
