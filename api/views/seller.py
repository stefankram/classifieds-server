from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import SellerModel
from api.pagination import Pagination
from api.serializers import SellerSerializer


class CreateSellerView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = SellerSerializer


class ListSellerView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = SellerModel.objects.all()
    serializer_class = SellerSerializer


class RetrieveUpdateSellerView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = SellerModel.objects.all()
    serializer_class = SellerSerializer
