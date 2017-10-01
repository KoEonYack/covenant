from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^python_list/$', views.python_lecture_list, name='python_lecture'),
    url(r'^python_list/python_1$', views.python_lecture_1, name='python1'),
    url(r'^python_list/python_2$', views.python_lecture_2, name='python2'),
    url(r'^python_list/python_3$', views.python_lecture_3, name='python3'),
    url(r'^python_list/python_4$', views.python_lecture_4, name='python4'),
    url(r'^python_list/python_5$', views.python_lecture_5, name='python5'),
    url(r'^python_list/python_6$', views.python_lecture_6, name='python6'),
    url(r'^python_list/python_7$', views.python_lecture_7, name='python7'),
]