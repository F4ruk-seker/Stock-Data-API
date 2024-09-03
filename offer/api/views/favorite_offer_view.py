from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from offer.api.serializers import OfferSerializer, FavoriteSerializer
from offer.models import FavoriteOfferModel
from django.contrib.auth.models import User


class FavoriteOffersListView(viewsets.ViewSet, CreateModelMixin, DestroyModelMixin):
    lookup_field = ''
    serializer_classes: dict = {
        'list': OfferSerializer,
        'create': FavoriteSerializer,
        'destroy': FavoriteSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)

    def get_object(self, *args, **kwargs):
        print(args)
        print(kwargs)
        if not self.action == 'list':
            return FavoriteOfferModel

    def list(self, request, *args, **kwargs):
        # user = self.request.user
        print('list içerden')
        user = User.objects.first()
        queryset = FavoriteOfferModel.objects.filter(user=user)
        queryset.order_by('created_at')

        return Response(OfferSerializer([_.offer for _ in queryset], many=True).data)

    def post(self, request, *args, **kwargs):
        print(self)
        print(request)
        print(args)
        print(kwargs)
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
