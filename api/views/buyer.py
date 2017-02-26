from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import BuyerModel
from api.pagination import Pagination
from api.serializers import BuyerSerializer


class CreateBuyerView(CreateAPIView):
    serializer_class = BuyerSerializer


class ListBuyerView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = BuyerModel.objects.all()
    serializer_class = BuyerSerializer


class RetrieveUpdateBuyerView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BuyerModel.objects.all()
    serializer_class = BuyerSerializer


class FindByUserIdBuyerView(RetrieveAPIView):
    lookup_field = 'user_id'
    permission_classes = (IsAuthenticated,)
    queryset = BuyerModel.objects.all()
    serializer_class = BuyerSerializer
