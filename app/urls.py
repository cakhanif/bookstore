from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^api/book/$', views.book_list),
    url(r'^api/book/(?P<pk>[0-9]+)/$', views.book_detail),
    url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework')),
]
