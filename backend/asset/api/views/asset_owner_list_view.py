from rest_framework.generics import ListAPIView
from asset.models import AssetOwnershipModel
from asset.api.serializers import ShareOwnershipSerializer


class AssetOwnerListView(ListAPIView):
    serializer_class = ShareOwnershipSerializer
    queryset = AssetOwnershipModel.objects.all()
    permission_classes = []
    authentication_classes = []