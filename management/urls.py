from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login_user', views.login_user, name='loginuser'),
    path('logout_user',views.logout_user,name='logoutuser'),
    path('register_user',views.register_user,name='registeruser'),
    path('record/<int:pk>', views.record, name='record'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('add_record', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update'),

]
