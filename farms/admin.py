from django.contrib import admin
from .models import Farm


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ("name", "owner_name", "location", "certification", "created_at")
    search_fields = ("name", "owner_name", "location", "certification")
