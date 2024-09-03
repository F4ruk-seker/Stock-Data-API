from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from offer.models import FavoriteOfferModel
from offer.api.serializers import FavoriteSerializer
from django.shortcuts import get_object_or_404


class FavoriteCreateDeleteView(CreateAPIView, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    lookup_field = 'code'
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return FavoriteOfferModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        offer = serializer.validated_data['offer']
        if not FavoriteOfferModel.objects.filter(
                user=self.request.user,
                offer=offer
        ).exists():
            serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        if code := kwargs.get(self.lookup_field):
            favorite_offer_model: FavoriteOfferModel = get_object_or_404(
                FavoriteOfferModel,
                user=self.request.user,
                offer=code
            )
            favorite_offer_model.delete()
            return Response(
                data={"detail": "The favorite has been deleted successfully."},
                status=status.HTTP_204_NO_CONTENT
            )
