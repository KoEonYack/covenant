from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^python_main/$', views.python, name='lecture'),

]