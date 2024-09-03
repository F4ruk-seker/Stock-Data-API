from rest_framework.generics import ListAPIView
from offer.api.serializers import OfferSerializer
from offer.models import FavoriteOfferModel
from django.contrib.auth.models import User


class FavoriteOffersListView(ListAPIView):
    serializer_class = OfferSerializer

    def get_queryset(self):
        # user = self.request.user
        user = User.objects.first()
        queryset = FavoriteOfferModel.objects.filter(user=user)
        queryset.order_by('created_at')
        return [fm.offer for fm in queryset]
