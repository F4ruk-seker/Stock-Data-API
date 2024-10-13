from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from asset.models import ActivePublicAssetingModel
from asset.api.serializers import ActivePublicAssetSerializer


class ActivePublicAssetBulkCreateView(APIView):
    serializer_class = ActivePublicAssetSerializer

    @staticmethod
    def get_queryset():
        return ActivePublicAssetingModel.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        bulk_active_asset_create_data = []

        for item in data:
            if 'url' in item:
                if not ActivePublicAssetingModel.objects.filter(url=item.get('url')).exists():
                    bulk_active_asset_create_data.append(item)

        if bulk_active_asset_create_data:
            create_serializer = ActivePublicAssetSerializer(data=bulk_active_asset_create_data, many=True)
            if create_serializer.is_valid(raise_exception=True):
                create_serializer.save()
                return Response({'detail': 'add new records created with successful.'}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'No new records created.'}, status=status.HTTP_204_NO_CONTENT)
