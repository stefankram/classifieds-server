from api.models import AddressModel
from api.serializers import AddressSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AddressView(APIView):
    """
    Address View

    Description
    -----------
    Display a specific address
    """

    def get_object(self, pk):
        try:
            return AddressModel.objects.get(pk=pk)
        except AddressModel.DoesNotExist:
            raise Http404

    def get(self, req, pk):
        return Response(AddressSerializer(self.get_object(pk)).data)

    def put(self, req, pk):
        serializer = AddressSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
