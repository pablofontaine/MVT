from django.urls import path

from family.views import fun_create_family_member, fun_show_family_members

urlpatterns = [
    path('create_family_member/<str:name>/<str:last_name>/<int:age>/<str:relationship>/<str:birth>', fun_create_family_member),
    path('list_family_member/', fun_show_family_members),
]