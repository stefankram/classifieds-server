from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import SellerItemModel
from api.pagination import Pagination
from api.serializers import SellerItemSerializer


class CreateSellerItemView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = SellerItemSerializer


class ListSellerItemView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = SellerItemModel.objects.all()
    serializer_class = SellerItemSerializer


class RetrieveUpdateSellerItemView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = SellerItemModel.objects.all()
    serializer_class = SellerItemSerializer
