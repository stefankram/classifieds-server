from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import MessageModel
from api.pagination import Pagination
from api.serializers import MessageSerializer


class CreateMessageView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer


class ListMessageView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


class RetrieveUpdateMessageView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


class FindAllBySearchIdMessageView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        return MessageModel.objects.filter(search_id=self.kwargs['search_id'])
