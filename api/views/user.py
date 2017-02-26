from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from api.pagination import Pagination
from api.serializers.user import UserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer


class ListUserView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateUserView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FindByUsernameUserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
