from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from asset.models import FavoriteAssetModel
from asset.api.serializers import FavoriteSerializer
from django.shortcuts import get_object_or_404


class FavoriteCreateDeleteView(CreateAPIView, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    lookup_field = 'code'
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return FavoriteAssetModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        asset = serializer.validated_data['asset']
        if not FavoriteAssetModel.objects.filter(
                user=self.request.user,
                asset=asset
        ).exists():
            serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        if code := kwargs.get(self.lookup_field):
            favorite_asset_model: FavoriteAssetModel = get_object_or_404(
                FavoriteAssetModel,
                user=self.request.user,
                asset=code
            )
            favorite_asset_model.delete()
            return Response(
                data={"detail": "The favorite has been deleted successfully."},
                status=status.HTTP_204_NO_CONTENT
            )
