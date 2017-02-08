from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import MessageModel
from api.pagination import Pagination
from api.serializers import MessageSerializer


class CreateMessageView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = MessageSerializer


class ListMessageView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


class RetrieveUpdateMessageView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
