from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import ItemModel
from api.pagination import Pagination
from api.serializers import ItemSerializer


class CreateItemView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer


class ListItemView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class RetrieveUpdateItemView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class FindByNameItemView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'name'
