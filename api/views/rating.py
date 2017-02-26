from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import RatingModel
from api.pagination import Pagination
from api.serializers import RatingSerializer


class CreateRatingView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RatingSerializer


class ListRatingView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    queryset = RatingModel.objects.all()
    serializer_class = RatingSerializer


class RetrieveUpdateRatingView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RatingModel.objects.all()
    serializer_class = RatingSerializer
