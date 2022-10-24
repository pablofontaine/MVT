from django.urls import path

from dispenser import views

app_name = 'dispenser'
urlpatterns = [
    path('list-dispenser/', views.list_dispenser, name='list-dispenser'),
]