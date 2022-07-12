from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='user_register'),

    path('dashboard/', views.user_dashbord, name='user_dashbord'),
    path('dashboard/edit', views.edit_dashboard, name='edit_dashboard'),
    path('<str:username>/', views.user_profile, name='user_profile'),
    path('follow/<str:username>/', views.user_following, name='user_following'),
    path('unfollow/<str:username>/', views.user_unfollowing, name='user_unfollowing'),

]
