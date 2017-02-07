from api.models import BillingModel
from api.serializers import BillingSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BillingView(APIView):
    """
    Billing View

    Description
    -----------
    Create a billing object
    """

    def put(self, req):
        """
        Create a billing object

        :param req: The request object
        :return: The newly created billing object
        """
        serializer = BillingSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

