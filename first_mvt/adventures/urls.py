from django.urls import path

from adventures import views

app_name = 'adventures'
urlpatterns = [
    path('', views.index),
]