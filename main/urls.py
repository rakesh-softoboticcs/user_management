from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('', views.loginPage, name='login'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('logout/', views.logoutPage, name='logout'),
]
