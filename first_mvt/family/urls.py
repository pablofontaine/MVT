from django.urls import path

from family import views

app_name = 'family'
urlpatterns = [
    path('family_members', views.family_list, name='family-list'),
    path('family_members/add', views.family_add_member, name='family-add-member'),
]