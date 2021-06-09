from django.urls import path
from . import views

urlpatterns = [
    path('', views.athlete_list, name='athletes'),
    path('detail/<str:pk>', views.athlete_detail, name='detail'),
    path('create', views.athlete_create, name='create'),
    path('update/<str:pk>', views.athlete_update, name='update'),
    path('delete/<str:pk>', views.athlete_delete, name='delete'),
]