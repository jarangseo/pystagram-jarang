from django.conf.urls import url
#이번시간에는 app별로 url을 관리할 수 있도록 한다
#그래서 새로운 urls.py를 만듦
# photos/urls.py

from . import views


app_name = 'photos'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/like/$', views.like_photo, name='like_photo'),
    url(r'^(?P<pk>[0-9]+)/$', views.view_photo, name='view_photo'),
    url(r'^$', views.toppage, name='toppage'),
]
