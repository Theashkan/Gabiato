from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/<str:username>/<int:post_id>', views.post_view, name='post_view'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/like/<str:username>/<int:post_id>', views.post_like, name='post_like'),
    path('post/unlike/<str:username>/<int:post_id>', views.post_unlike, name='post_unlike'),
]
