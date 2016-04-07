"""mup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from publication import views

urlpatterns = [
    url(r'^admin-site/', admin.site.urls),
    url(r'^reg_users/', views.register_user, name='register_user'),
    url(r'^admin/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^new/', views.add_post, name='add_post'),
    url(r'^(?P<slug>[^\.]+).html', views.view_more, name='view_more'),
    url(r'^$', views.view_post, name='home'),
    url(r'^sub/', views.subscriptions, name='sub'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^update_posts/(?P<id>\d+)/$', views.update_post, name="update_post"),
    url(r'^archive/(?P<id>\d+)/$', views.archive_post, name="update_post"),
    url(r'^update/$', views.update_post, name='update_post'),
    url(r'^send/$', views.send_newsletters, name='send_mails'),
    url(r'^resetpassword/$', views.forgot_password, name='forgot_password'),


    

]