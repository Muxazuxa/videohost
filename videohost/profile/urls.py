from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .import views

app_name = 'profile'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='profile/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='profile/logout.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile')
]