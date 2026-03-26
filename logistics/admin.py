from django.contrib import admin
from .models import DistributionEvent


@admin.register(DistributionEvent)
class DistributionEventAdmin(admin.ModelAdmin):
    list_display = ("batch", "event_type", "location", "timestamp", "quantity_kg")
    list_filter = ("event_type", "location")
    search_fields = ("batch__batch_id", "location")
