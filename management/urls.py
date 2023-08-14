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
    path('sort_by_order', views.sort_by_order, name='sort_by_order'),
    path('sort_by_firstname', views.sort_by_firstname, name='sort_by_firstname'),
    path('sort_by_lastname', views.sort_by_lastname, name='sort_by_lastname'),
    path('sort_by_city', views.sort_by_city, name='sort_by_city'),
    path('sort_by_state', views.sort_by_state, name='sort_by_state'),

]
