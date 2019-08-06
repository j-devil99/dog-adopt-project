from django.urls import path

from . import views

urlpatterns = [
    path('logins', views.login, name='logins'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]
