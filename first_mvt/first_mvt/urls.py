from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('family/', include('family.urls')),
    path('adventures/', include('adventures.urls')),
    path('possessions/', include('possessions.urls')),
]
