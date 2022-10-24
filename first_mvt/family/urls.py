from django.urls import path

from family import views

app_name = 'family'
urlpatterns = [
    # path('create_family_member/<str:name>/<str:last_name>/<int:age>/<str:relationship>', views.fun_create_family_member),
    # path('list_family_member/', views.fun_show_family_members),
    path('family_members/', views.family_members, name='family-members-list'),
]