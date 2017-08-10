from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^python_list/$', views.python, name='python_lecture'),
    url(r'^python_list/python_1$', views.python1, name='python1'),
url(r'^python_list/python_2$', views.python2, name='python2'),

]