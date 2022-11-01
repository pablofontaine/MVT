from django.urls import path

from adventures import views

app_name = 'adventures'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.adventures_add, name='adventures-add'),
]