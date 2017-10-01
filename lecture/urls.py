from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^python_list/$', views.python_lecture_list, name='python_lecture'),
    url(r'^python_list/python_1$', views.python_lecture_1, name='python_1'),
    url(r'^python_list/python_2$', views.python_lecture_2, name='python_2'),
    url(r'^python_list/python_3$', views.python_lecture_3, name='python_3'),
    url(r'^python_list/python_4$', views.python_lecture_4, name='python_4'),
    url(r'^python_list/python_5$', views.python_lecture_5, name='python_5'),
    url(r'^python_list/python_6$', views.python_lecture_6, name='python_6'),
    url(r'^python_list/python_7$', views.python_lecture_7, name='python_7'),
]