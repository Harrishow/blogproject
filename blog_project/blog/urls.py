from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('details', views.post_details, name='details'),
    path('register', views.register, name='register'),
    path('users/', views.users, name='users.list'),

]