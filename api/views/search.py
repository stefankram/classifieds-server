from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import SearchModel
from api.pagination import Pagination
from api.serializers import SearchSerializer


class CreateSearchView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = SearchSerializer


class ListSearchView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = SearchModel.objects.all()
    serializer_class = SearchSerializer


class RetrieveUpdateSearchView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = SearchModel.objects.all()
    serializer_class = SearchSerializer
