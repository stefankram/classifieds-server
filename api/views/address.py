from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import AddressModel
from api.pagination import Pagination
from api.serializers import AddressSerializer


class CreateAddressView(CreateAPIView):
    serializer_class = AddressSerializer


class ListAddressView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer


class RetrieveUpdateAddressView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer
