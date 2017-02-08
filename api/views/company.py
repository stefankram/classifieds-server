from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import CompanyModel
from api.pagination import Pagination
from api.serializers import CompanySerializer


class CreateCompanyView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = CompanySerializer


class ListCompanyView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer


class RetrieveUpdateCompanyView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
