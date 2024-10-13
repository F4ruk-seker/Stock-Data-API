from rest_framework.generics import CreateAPIView
from asset.api.serializers import SlotSerializer
from asset.models import SlotModel, AssetOwnershipModel
from django.shortcuts import get_object_or_404


class SlotCreateView(CreateAPIView):
    serializer_class = SlotSerializer
    queryset = SlotModel.objects.all()

    def perform_create(self, serializer, *args, **kwargs):
        code = self.kwargs.get('code')
        user = self.request.user
        if asset_owner := get_object_or_404(AssetOwnershipModel, owner=user, asset=code):
            new_slot = serializer.save()
            asset_owner.slots.add(new_slot)
