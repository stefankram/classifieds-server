from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import OrderModel
from api.pagination import Pagination
from api.serializers import OrderSerializer


class CreateOrderView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = OrderSerializer


class ListOrderView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer


class RetrieveUpdateOrderView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
