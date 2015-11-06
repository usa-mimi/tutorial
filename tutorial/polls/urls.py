from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<pk>\d+)/$', views.detail, name='poll_detail'),
    url(r'(?P<pk>\d+)/vote$', views.vote, name='poll_vote'),
    url(r'(?P<pk>\d+)/results$', views.results, name='poll_results'),
]
