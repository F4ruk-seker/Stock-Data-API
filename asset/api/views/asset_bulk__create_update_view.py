from rest_framework.response import Response
from rest_framework.views import APIView
from asset.api.serializers import AssetSerializer
from asset.models import AssetModel


class AssetBulkCreateUpdateView(APIView):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return AssetModel.objects.all()

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data

        # Extract codes from request data
        codes = [item['code'] for item in data if 'code' in item]

        # Fetch all existing records in a single query
        existing_records = {item.code: item for item in AssetModel.objects.filter(code__in=codes)}

        # Separate data into bulk update and bulk create lists
        bulk_update_data = [item for item in data if 'code' in item and item['code'] in existing_records]
        bulk_create_data = [item for item in data if 'code' not in item or item['code'] not in existing_records]

        response_data = {}

        # Bulk update
        if bulk_update_data:
            update_instances = [existing_records[item['code']] for item in bulk_update_data]
            for item in bulk_update_data:
                # Update each instance individually
                instance = existing_records[item['code']]
                serializer = self.get_serializer(instance, data=item, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            response_data['updated'] = [self.get_serializer(instance).data for instance in update_instances]

        # Bulk create
        if bulk_create_data:
            create_serializer = self.get_serializer(data=bulk_create_data, many=True)
            create_serializer.is_valid(raise_exception=True)
            create_serializer.save()
            response_data['created'] = create_serializer.data

        return Response(response_data, status=200)
