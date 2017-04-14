from django.conf.urls import url

from . import views

pricepatterns = [
    url(r'^(?P<pk>[0-9]+)/?$', views.SupplierPriceBreakDetail.as_view(), name='supplierpricebreak-detail'),

    url(r'^\?.*/?$', views.SupplierPriceBreakList.as_view()),
    url(r'^$', views.SupplierPriceBreakList.as_view())
]

urlpatterns = [

    # Display details of a supplier
    url(r'^(?P<pk>[0-9]+)/$', views.SupplierDetail.as_view(), name='supplier-detail'),

    # List suppliers
    url(r'^\?.*/?$', views.SupplierList.as_view()),
    url(r'^$', views.SupplierList.as_view())
]
