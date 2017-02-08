from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    url(r'^buyer/$', views.CreateBuyerView.as_view()),
    url(r'^buyer/(?P<pk>[0-9]+)/$', views.RetrieveUpdateBuyerView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
