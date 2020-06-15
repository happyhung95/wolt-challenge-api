from django.urls import path

from Wolt_app import methods, views

urlpatterns = [
    path('restaurants/search', methods.search),
    path('', views.home)
]
