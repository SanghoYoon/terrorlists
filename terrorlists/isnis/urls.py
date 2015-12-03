from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^register.html/$', views.register, name='register'),
    url(r'^post/remove/(?P<post_id>[0-9]+)/(?P<post_author>[a-zA-Z0-9]+)/$',views.post_remove, name='post_remove'),
    url(r'^new/$', views.new, name='new'),
    url(r'^login/$',views.login, name='login'),
    url(r'^edit/(?P<post_author>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)/$',views.edit, name='edit'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]