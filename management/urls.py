from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('',views.home,name='home'),
    #path('login_user', views.login_user, name='loginuser'),
    path('logout_user',views.logout_user,name='logoutuser'),
    path('register_user',views.register_user,name='registeruser')



    
]
