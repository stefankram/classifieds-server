from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import BillingModel
from api.pagination import Pagination
from api.serializers import BillingSerializer


class CreateBillingView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = BillingSerializer


class ListBillingView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = BillingModel.objects.all()
    serializer_class = BillingSerializer


class RetrieveUpdateBillingView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = BillingModel.objects.all()
    serializer_class = BillingSerializer
