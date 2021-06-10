"""desafio_celero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from athlete_events.api import viewsets as athlete_viewset
from athlete_events.views import upload_data

route = routers.DefaultRouter()
route.register(r'athlete', athlete_viewset.AthletesEventsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include(route.urls)),
    path('upload_csv/', upload_data, name='upload_data'),
]
