from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^popNatal$', views.popNatal, name='popNatal'),
    url(r'^popMossoro$', views.popNatal, name='popMossoro'),
    url(r'^popNatalMossoro$', views.popNatal, name='popNatalMossoro')


]
