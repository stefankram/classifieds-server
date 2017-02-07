from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import AddressView

urlpatterns = [
    url(r'^api/address/(?P<pk>[0-9]+)/$', AddressView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
