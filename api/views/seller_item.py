from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import SellerItemModel
from api.pagination import Pagination
from api.serializers import SellerItemSerializer


class CreateSellerItemView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SellerItemSerializer


class ListSellerItemView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = SellerItemModel.objects.all()
    serializer_class = SellerItemSerializer


class RetrieveUpdateSellerItemView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SellerItemModel.objects.all()
    serializer_class = SellerItemSerializer
