from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'new_profile1', views.new_profile1, name='new_profile1'),
    url(r'post_edit', views.post_edit, name='post_edit')
]