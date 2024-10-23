from rest_framework.generics import ListAPIView
from asset.models import AssetModel
from asset.api.serializers import AssetsOnlyNameAndCodeSerializer


class AssetSummaryListView(ListAPIView):
    model: AssetModel = AssetModel
    serializer_class: AssetsOnlyNameAndCodeSerializer = AssetsOnlyNameAndCodeSerializer
    queryset = model.objects.only('code', 'name', 'logo')
