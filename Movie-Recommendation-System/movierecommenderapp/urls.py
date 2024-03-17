from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend_movie/', views.recommend_movie, name='recommend_movie'),
]