from rest_framework.generics import RetrieveUpdateDestroyAPIView
from asset.api.serializers import SlotSerializer
from asset.models import AssetOwnershipModel
from django.shortcuts import get_object_or_404


class SlotRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = SlotSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        code = self.kwargs.get('code')
        user = self.request.user
        asset_owner = get_object_or_404(AssetOwnershipModel, owner=user, asset=code)
        return asset_owner.slots.filter(pk=pk)
