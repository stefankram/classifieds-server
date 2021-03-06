from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from api.views import CreateAddressView
from api.views import CreateBillingView
from api.views import CreateBuyerView
from api.views import CreateCompanyView
from api.views import CreateItemView
from api.views import CreateMessageView
from api.views import CreateOrderView
from api.views import CreateRatingView
from api.views import CreateSellerItemView
from api.views import CreateSellerView
from api.views import CreateUserView
from api.views import FindAllByBuyerIdSearchView
from api.views import FindAllByItemIdSearchView
from api.views import FindAllBySearchIdMessageView
from api.views import FindByNameItemView
from api.views import ListAddressView
from api.views import ListBillingView
from api.views import ListBuyerView
from api.views import ListCompanyView
from api.views import ListItemView
from api.views import ListMessageView
from api.views import ListOrderView
from api.views import ListRatingView
from api.views import ListSellerItemView
from api.views import ListSellerView
from api.views import ListUserView
from api.views import RetrieveUpdateAddressView
from api.views import RetrieveUpdateBillingView
from api.views import RetrieveUpdateBuyerView
from api.views import RetrieveUpdateCompanyView
from api.views import RetrieveUpdateItemView
from api.views import RetrieveUpdateMessageView
from api.views import RetrieveUpdateOrderView
from api.views import RetrieveUpdateRatingView
from api.views import RetrieveUpdateSellerItemView
from api.views import RetrieveUpdateSellerView
from api.views import RetrieveUpdateUserView
from api.views import ListSearchView
from api.views import CreateSearchView
from api.views import RetrieveUpdateSearchView
from api.views import FindByUsernameUserView
from api.views import FindByUserIdBuyerView
from api.views.seller import FindByUserIdSellerView

urlpatterns = [
    url(r'^addresses/$', ListAddressView.as_view()),
    url(r'^address/create/$', CreateAddressView.as_view()),
    url(r'^address/(?P<pk>[0-9]+)/$', RetrieveUpdateAddressView.as_view()),

    url(r'^billings/$', ListBillingView.as_view()),
    url(r'^billing/create/$', CreateBillingView.as_view()),
    url(r'^billing/(?P<pk>[0-9]+)/$', RetrieveUpdateBillingView.as_view()),

    url(r'^buyers/$', ListBuyerView.as_view()),
    url(r'^buyer/create/$', CreateBuyerView.as_view()),
    url(r'^buyer/find/(?P<user_id>[0-9]+)/$', FindByUserIdBuyerView.as_view()),
    url(r'^buyer/(?P<pk>[0-9]+)/$', RetrieveUpdateBuyerView.as_view()),

    url(r'^companies/$', ListCompanyView.as_view()),
    url(r'^company/create/$', CreateCompanyView.as_view()),
    url(r'^company/(?P<pk>[0-9]+)/$', RetrieveUpdateCompanyView.as_view()),

    url(r'^items/$', ListItemView.as_view()),
    url(r'^item/create/$', CreateItemView.as_view()),
    url(r'^item/(?P<pk>[0-9]+)/$', RetrieveUpdateItemView.as_view()),
    url(r'^item/find/(?P<name>[a-z]+)/$', FindByNameItemView.as_view()),

    url(r'^messages/$', ListMessageView.as_view()),
    url(r'^message/create/$', CreateMessageView.as_view()),
    url(r'^message/find/all/(?P<search_id>[0-9]+)/$',
        FindAllBySearchIdMessageView.as_view()),
    url(r'^message/(?P<pk>[0-9]+)/$', RetrieveUpdateMessageView.as_view()),

    url(r'^orders/$', ListOrderView.as_view()),
    url(r'^order/create/$', CreateOrderView.as_view()),
    url(r'^order/(?P<pk>[0-9]+)/$', RetrieveUpdateOrderView.as_view()),

    url(r'^ratings/$', ListRatingView.as_view()),
    url(r'^rating/create/$', CreateRatingView.as_view()),
    url(r'^rating/(?P<pk>[0-9]+)/$', RetrieveUpdateRatingView.as_view()),

    url(r'^searches/$', ListSearchView.as_view()),
    url(r'^search/create/$', CreateSearchView.as_view()),
    url(r'^search/find/all/item/(?P<item_id>[0-9]+)/$',
        FindAllByItemIdSearchView.as_view()),
    url(r'^search/find/all/(?P<buyer_id>[0-9]+)/$',
        FindAllByBuyerIdSearchView.as_view()),
    url(r'^search/(?P<pk>[0-9]+)/$', RetrieveUpdateSearchView.as_view()),

    url(r'^sellers/$', ListSellerView.as_view()),
    url(r'^seller/create/$', CreateSellerView.as_view()),
    url(r'^seller/find/(?P<user_id>[0-9]+)/$',
        FindByUserIdSellerView.as_view()),
    url(r'^seller/(?P<pk>[0-9]+)/$', RetrieveUpdateSellerView.as_view()),

    url(r'^seller-items/$', ListSellerItemView.as_view()),
    url(r'^seller-item/create/$', CreateSellerItemView.as_view()),
    url(r'^seller-item/(?P<pk>[0-9]+)/$',
        RetrieveUpdateSellerItemView.as_view()),

    url(r'^token/obtain/$', obtain_jwt_token),
    url(r'^token/refresh/$', refresh_jwt_token),
    url(r'^token/verify/$', verify_jwt_token),

    url(r'^users/$', ListUserView.as_view()),
    url(r'^user/create/$', CreateUserView.as_view()),
    url(r'^user/find/(?P<username>.+)/$',
        FindByUsernameUserView.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', RetrieveUpdateUserView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
