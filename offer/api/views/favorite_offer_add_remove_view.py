from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response

from offer.models import FavoriteOfferModel
from offer.api.serializers import FavoriteSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class FavoriteCreateDeleteView(CreateAPIView, DestroyModelMixin):
    lookup_field = 'code'
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        # user = self.request.user
        user = User.objects.first()
        return FavoriteOfferModel.objects.filter(user=user)

    def perform_create(self, serializer):
        # user = self.request.user
        user = User.objects.first()

        offer = serializer.validated_data['offer']

        if not FavoriteOfferModel.objects.filter(user=user, offer=offer).exists():
            serializer.save(user=user)

    def delete(self, request, *args, **kwargs):
        if code := kwargs.get(self.lookup_field):
            user = User.objects.first()
            favorite_offer_model: FavoriteOfferModel = get_object_or_404(FavoriteOfferModel, user=user, offer=code)
            favorite_offer_model.delete()
            return Response(
                data={"detail": "The favorite has been deleted successfully."},
                status=status.HTTP_204_NO_CONTENT
            )
