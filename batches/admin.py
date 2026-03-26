from django.contrib import admin
from .models import WoolBatch


@admin.register(WoolBatch)
class WoolBatchAdmin(admin.ModelAdmin):
    list_display = ("batch_id", "farm", "shear_date", "weight_kg", "quality_grade", "status", "current_location")
    list_filter = ("status", "quality_grade", "shear_date")
    search_fields = ("batch_id", "farm__name", "current_location")
