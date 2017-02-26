from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import OrderModel
from api.pagination import Pagination
from api.serializers import OrderSerializer


class CreateOrderView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer


class ListOrderView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer


class RetrieveUpdateOrderView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
