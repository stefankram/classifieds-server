from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import RatingModel
from api.pagination import Pagination
from api.serializers import RatingSerializer


class CreateRatingView(CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = RatingSerializer


class ListRatingView(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = Pagination
    queryset = RatingModel.objects.all()
    serializer_class = RatingSerializer


class RetrieveUpdateRatingView(RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = RatingModel.objects.all()
    serializer_class = RatingSerializer
