from rest_framework.generics import RetrieveAPIView
from asset.models import AssetModel
from asset.api.serializers import AssetDetailSerializer


class AssetDetailView(RetrieveAPIView):
    lookup_field = 'code'
    queryset = AssetModel.objects.all()
    serializer_class = AssetDetailSerializer
