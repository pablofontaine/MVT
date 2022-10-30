from django.contrib import admin

# Register your models here.

from adventures.models import Adventure

admin.site.register(Adventure)