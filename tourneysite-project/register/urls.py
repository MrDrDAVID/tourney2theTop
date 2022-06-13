from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='userLogin'),
    path('user_logout/', views.user_logout, name='userLogout'),
]