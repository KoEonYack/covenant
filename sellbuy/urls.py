
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^list/$', views.sell_list, name='sell_list'), # 삽니다 목록 리스트를 만들어야 한다.


    url(r'^(?P<id>\d+)/detail/$', views.sell_detail, name='sell_detail'),

    url(r'^main$', views.main, name='main'),

    url(r'^new/$', views.sell_new, name='sell_new'),
    url(r'^(?P<id>\d+)/edit/$', views.sell_edit, name='sell_edit'),

    url(r'^introducehuman/$', views.introduce_human, name='introduce_human'),
]
