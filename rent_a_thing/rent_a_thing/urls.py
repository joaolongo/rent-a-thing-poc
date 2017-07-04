"""rent_a_thing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from server import views as server_views
from client import views as client_views

server_router = routers.DefaultRouter()
server_router.register(r'users', server_views.UserViewSet)
server_router.register(r'groups', server_views.GroupViewSet)
server_router.register(r'clients', server_views.ClientViewSet)

client_router = routers.DefaultRouter()
client_router.register(r'command', client_views.CommandViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^server/api/', include(server_router.urls)),
    url(r'^client/api/', include(client_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
