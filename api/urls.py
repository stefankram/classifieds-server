from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api.views import CreateAddressView
from api.views import CreateBillingView
from api.views import CreateBuyerView
from api.views import CreateCompanyView
from api.views import CreateItemView
from api.views import CreateUserView
from api.views import ListAddressView
from api.views import ListBillingView
from api.views import ListBuyerView
from api.views import ListCompanyView
from api.views import ListItemView
from api.views import ListUserView
from api.views import RetrieveUpdateAddressView
from api.views import RetrieveUpdateBillingView
from api.views import RetrieveUpdateBuyerView
from api.views import RetrieveUpdateCompanyView
from api.views import RetrieveUpdateItemView
from api.views import RetrieveUpdateUserView

urlpatterns = [
    # Address urls
    url(r'^addresses/$', ListAddressView.as_view()),
    url(r'^address/create/$', CreateAddressView.as_view()),
    url(r'^address/(?P<pk>[0-9]+)/$', RetrieveUpdateAddressView.as_view()),

    # Billing urls
    url(r'^billings/$', ListBillingView.as_view()),
    url(r'^billing/create/$', CreateBillingView.as_view()),
    url(r'^billing/(?P<pk>[0-9]+)/$', RetrieveUpdateBillingView.as_view()),

    # Buyer urls
    url(r'^buyers/$', ListBuyerView.as_view()),
    url(r'^buyer/create/$', CreateBuyerView.as_view()),
    url(r'^buyer/(?P<pk>[0-9]+)/$', RetrieveUpdateBuyerView.as_view()),

    # Company urls
    url(r'companies/$', ListCompanyView.as_view()),
    url(r'company/create/$', CreateCompanyView.as_view()),
    url(r'company/(?P<pk>[0-9]+)/$', RetrieveUpdateCompanyView.as_view()),

    # Item urls
    url(r'items/$', ListItemView.as_view()),
    url(r'item/create/$', CreateItemView.as_view()),
    url(r'item/(?P<pk>[0-9]+)/$', RetrieveUpdateItemView.as_view()),

    # Token authentication urls
    url(r'^token/obtain/$', obtain_jwt_token),
    url(r'^token/refresh/$', refresh_jwt_token),

    # User urls
    url(r'^users/$', ListUserView.as_view()),
    url(r'^user/create/$', CreateUserView.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', RetrieveUpdateUserView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
