from rest_framework.generics import ListAPIView
from asset.api.serializers import AssetSerializer
from asset.models import AssetModel


class AssetListView(ListAPIView):
    queryset = AssetModel.objects.all()
    serializer_class = AssetSerializer
