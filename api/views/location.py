from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import LocationModel
from api.pagination import Pagination
from api.serializers import LocationSerializer


class CreateLocationView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer


class ListLocationView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer


class RetrieveUpdateLocationView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer
