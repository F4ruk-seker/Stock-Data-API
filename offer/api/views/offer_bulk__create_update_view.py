from rest_framework.response import Response
from rest_framework.views import APIView


class OfferBulkCreateUpdateView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'msg': 'ok'})