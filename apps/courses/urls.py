from django.conf.urls import url
from . import views 


urlpatterns = [
    url(r'^$', views.index),
    url(r'^course$', views.course),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^process/delete/(?P<id>\d+)$', views.delete)
]