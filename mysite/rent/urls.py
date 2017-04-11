from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^rent/(?P<item_id>[0-9]+)/$', views.rent, name="rent"),
    url(r'^return/(?P<item_id>[0-9]+)/$', views.returns, name="return")
]
