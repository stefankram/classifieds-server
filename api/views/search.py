from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import SearchModel
from api.pagination import Pagination
from api.serializers import SearchSerializer


class CreateSearchView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SearchSerializer


class ListSearchView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = SearchModel.objects.all()
    serializer_class = SearchSerializer


class RetrieveUpdateSearchView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SearchModel.objects.all()
    serializer_class = SearchSerializer


class FindAllByBuyerIdSearchView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SearchSerializer

    def get_queryset(self):
        return SearchModel.objects.filter(buyer_id=self.kwargs['buyer_id'])
