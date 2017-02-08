from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

from api.models import BuyerModel
from api.serializers import BuyerSerializer


class CreateBuyerView(CreateAPIView):
    serializer_class = BuyerSerializer


class RetrieveUpdateBuyerView(RetrieveUpdateAPIView):
    serializer_class = BuyerSerializer
    queryset = BuyerModel.objects.all()
