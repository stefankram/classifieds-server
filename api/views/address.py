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
    Display all addresses or create one
    """

    def get(self, req):
        """
        Get all addresses

        :param req: The request object
        :return: JSON array of address objects
        :raise DoesNotExist if no addresses exist
        """
        try:
            addresses = AddressModel.objects.all()
            serializer = AddressSerializer(addresses, many=True)

            return Response(serializer.data)

        except AddressModel.DoesNotExist:
            raise Http404

    def put(self, req):
        """
        Create an address

        :param req: The request object
        :return: The newly created address
        """
        serializer = AddressSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetailView(APIView):
    """
    Address Detail View

    Description
    -----------
    Display a detailed address
    """

    def get(self, req, pk):
        """
        Get a specific address

        :param req: The request object
        :param pk: The address's primary key
        :return: The address object
        :raise DoesNotExist if no address exists for the primary key
        """
        try:
            address = AddressModel.objects.get(pk=pk)
            serializer = AddressSerializer(address)

            return Response(serializer.data)

        except AddressModel.DoesNotExist:
            raise Http404

    def delete(self, req, pk):
        """
        Delete a specific address

        :param req: The request object
        :param pk: The address's primary key
        :return: The address object
        :raise DoesNotExist if no address exists for the primary key
        """
        try:
            address = AddressModel.objects.get(pk=pk)
            address.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except AddressModel.DoesNotExist:
            raise Http404
