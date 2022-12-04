from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список постов, отфильтрованных по группам
    path('group/<slug:slug>/', views.group_posts),
] 