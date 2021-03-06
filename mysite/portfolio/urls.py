from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'new_profile1', views.new_profile1, name='new_profile1'),
    url(r'full_profile', views.full_profile, name='full_profile'),
    url(r'edit_profile', views.edit_profile, name='edit_profile'),
    url(r'post_view', views.post_view, name='post_view'),
    url(r'post_edit', views.post_edit, name='post_edit')
]