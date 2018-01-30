from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^new/$', views.Create_post.as_view(), name='create'),
    # Страница редактирования сигнатуры
    url(r'^update/(?P<pk>[0-9]+)/$', views.Update_post.as_view(), name='update'),
    # Страница удаления сигнатуры
    url(r'^delete/(?P<pk>[0-9]+)/$', views.Delete_post.as_view(), name='delete'),
]