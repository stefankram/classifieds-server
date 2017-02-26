from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import CompanyModel
from api.pagination import Pagination
from api.serializers import CompanySerializer


class CreateCompanyView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer


class ListCompanyView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer


class RetrieveUpdateCompanyView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
