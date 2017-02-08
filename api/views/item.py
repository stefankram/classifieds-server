from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import ItemModel
from api.pagination import Pagination
from api.serializers import ItemSerializer


class CreateItemView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = ItemSerializer


class ListItemView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class RetrieveUpdateItemView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
