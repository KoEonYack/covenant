from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^python_list/$', views.python, name='python_lecture'),
    url(r'^python_list/python_1$', views.python1, name='python1'),
    url(r'^python_list/python_2$', views.python2, name='python2'),
    url(r'^python_list/python_3$', views.python2, name='python3'),
    url(r'^python_list/python_4$', views.python2, name='python4'),
    url(r'^python_list/python_5$', views.python2, name='python5'),
    url(r'^python_list/python_6$', views.python2, name='python6'),
    url(r'^python_list/python_7$', views.python2, name='python7'),
]