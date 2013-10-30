from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns('',
    url('^addexp/$', views.addexp, name='addexp') , 
    url('^viewexp/$', views.viewexp, name='viewexp') , 
    url('^editexp/(?P<expid>\d+)/$', views.editexp, name='editexp') ,
)

