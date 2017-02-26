from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import SellerModel
from api.pagination import Pagination
from api.serializers import SellerSerializer


class CreateSellerView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SellerSerializer


class ListSellerView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = SellerModel.objects.all()
    serializer_class = SellerSerializer


class RetrieveUpdateSellerView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SellerModel.objects.all()
    serializer_class = SellerSerializer
