from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from offer.models import ActivePublicOfferingModel
from offer.api.serializers import ActivePublicOfferSerializer


class ActivePublicOfferBulkCreateView(APIView):
    serializer_class = ActivePublicOfferSerializer

    @staticmethod
    def get_queryset():
        return ActivePublicOfferingModel.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        bulk_active_offer_create_data = []

        for item in data:
            if 'url' in item:
                if not ActivePublicOfferingModel.objects.filter(url=item.get('url')).exists():
                    bulk_active_offer_create_data.append(item)

        if bulk_active_offer_create_data:
            create_serializer = ActivePublicOfferSerializer(data=bulk_active_offer_create_data, many=True)
            if create_serializer.is_valid(raise_exception=True):
                create_serializer.save()
                return Response({'detail': 'add new records created with successful.'}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'No new records created.'}, status=status.HTTP_204_NO_CONTENT)
