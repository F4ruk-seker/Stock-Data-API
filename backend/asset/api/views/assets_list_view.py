from rest_framework.generics import ListAPIView
from asset.api.serializers import AssetSerializer
from asset.models import AssetModel


class AssetListView(ListAPIView):
    queryset = AssetModel.objects.all()
    serializer_class = AssetSerializer

    # def get_queryset(self, *args, **kwargs):
    #     q = AssetModel.objects
    #     if only := self.request.query_params.get('only', None):
    #         return q.only(only)
    #     return q.all()
