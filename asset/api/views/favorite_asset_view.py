from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from asset.api.serializers import AssetSerializer
from asset.models import FavoriteAssetModel


class FavoriteAssetsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AssetSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = FavoriteAssetModel.objects.filter(user=user)
        queryset.order_by('created_at')
        return [fm.asset for fm in queryset]
