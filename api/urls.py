from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from api.views import BillingView

urlpatterns = [
    url(r'^address/$', ListAddressView.as_view()),
    url(r'^address/create/$', CreateAddressView.as_view()),
    url(r'^address/(?P<pk>[0-9]+)/$', AddressDetailView.as_view()),
    url(r'^billing/$', BillingView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
