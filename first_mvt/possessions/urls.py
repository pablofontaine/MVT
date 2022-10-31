from django.urls import path

from possessions import views

app_name = 'possessions'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.possesions_add, name='possesions-add'),
]