from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='userLogin'),
    # path('logout/', views.logout, name='logout'),
]