from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

#app_name = "api"

urlpatterns = [
    url(r'^all/$', views.all.as_view(), name="AllProperties"),
    url(r'^details/(?P<pk>\d+)/$', views.details.as_view(), name="DetailProperty"),
]

urlpatterns = format_suffix_patterns(urlpatterns)