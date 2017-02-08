from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import BuyerModel
from api.pagination import Pagination
from api.serializers import BuyerSerializer


class CreateBuyerView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = BuyerSerializer


class ListBuyerView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = BuyerModel.objects.all()


class RetrieveUpdateBuyerView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = BuyerModel.objects.all()
    serializer_class = BuyerSerializer
