"""mystie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'main/$', lambda r: redirect('sell_list_page:main'), name='main'),

    url(r'^$', lambda r: redirect('sell_list_page:main'), name='root'),
    url(r'^sell/', include('sellbuy.urls', namespace='sell_list_page')), # 삽니다 목록 리스트를 만들어야 한다.

    url(r'^accounts/', include('accounts.urls')),
    url(r'^lecture/', include('lecture.urls', namespace='lecture')),

    url(r'^summernote/', include('django_summernote.urls')),
]
