from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('track/', views.track, name='track'),
    path('login/', views.login, name='login'),
    path('register_vehicle/', views.register_vehicle, name='register_vehicle'),
]
    # other URL patterns