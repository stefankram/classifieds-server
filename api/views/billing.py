from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import BillingModel
from api.pagination import Pagination
from api.serializers import BillingSerializer


class CreateBillingView(CreateAPIView):
    serializer_class = BillingSerializer


class ListBillingView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = BillingModel.objects.all()
    serializer_class = BillingSerializer


class RetrieveUpdateBillingView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BillingModel.objects.all()
    serializer_class = BillingSerializer
