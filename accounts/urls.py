from django.conf.urls import url
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^singup/$', views.SignUp.as_view(), name='signup'),

    url(r'^profile/$', views.profile, name='profile'),

    url(r'^login/$', auth_views.login, name='login', kwargs={'template_name':'accounts/login_form.html'}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page':settings.LOGIN_URL}),
]