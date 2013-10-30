from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index1, name='index'),
    url(r'^1$',
        # /
        views.index,
        name = 'team-index',
    ),
    url('^editbook/(?P<author_id>\d+)/$', views.update_book, name='update-book') ,
    url('^submit_book/$', views.submit_book, name='update-book') , 
)

