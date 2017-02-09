from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.pagination import Pagination
from api.serializers.user import UserSerializer


class CreateUserView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = UserSerializer


class ListUserView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateUserView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
