"""practica_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout, login
from django.views.static import serve
from django.views.generic import RedirectView
from museos import views as museos_views

urlpatterns = [
    url(r'^$', museos_views.homepage, name='homepage'),
    url(r'^museos$', museos_views.museos, name="museos"),
    url(r'^museos/(\d+)', museos_views.museo_info, name='museo_info'),
    url(r'^about$', museos_views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', museos_views.registro, name='registro'),
    url(r'^login/$', museos_views.autenticacion, name='autenticacion'),
    url(r'^museos/login/$', museos_views.autenticacion, name='autenticacion'),
    url(r'^logout/$', logout, name="logout"),
    url(r'^museos/logout/$', logout, name='logout'),
    url(r'^(.*)/xml$', museos_views.user_xml, name='user_xml'),
    url(r'^css/style.css$', museos_views.css, name="css"),
    url(r'^museos/css/style.css$', museos_views.css, name='css'),
    url(r'^museos/js/(.*)$', serve, {'document_root' : 'templates/template_html/js'}, name='js'),
    url(r'^museos/images/(.*)$', serve, {'document_root' : 'templates/template_html/images'}, name='images'),
    url(r'^museos/fonts/(.*)$', serve, {'document_root' : 'templates/template_html/fonts'}, name='fonts'),
    url(r'^js/(.*)$', serve, {'document_root': 'templates/template_html/js'}, name = "js"),
    url(r'^images/(.*)$', serve, {'document_root': 'templates/template_html/images'}, name='images'),
    url(r'^fonts/(.*)$', serve, {'document_root' : 'templates/template_html/fonts'}, name="fonts"),
    url(r'^assets/(.*)$', serve, {'document_root' : 'templates/template_html/assets'}, name='assets'),
    url(r'/^assets/(.*)$', serve, {'document_root' : 'templates/template_html/assets'}, name='assets'),
       
    url(r'^(.*)$', museos_views.userpage, name='userpage'),
]
