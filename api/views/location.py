from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import LocationModel
from api.pagination import Pagination
from api.serializers import LocationSerializer


class CreateLocationView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = LocationSerializer


class ListLocationView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer


class RetrieveUpdateLocationView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer
