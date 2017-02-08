from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import AddressModel
from api.pagination import Pagination
from api.serializers import AddressSerializer


class CreateAddressView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = AddressSerializer


class ListAddressView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer


class RetrieveUpdateAddressView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer
