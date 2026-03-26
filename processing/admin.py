from django.contrib import admin
from .models import ProcessingStage


@admin.register(ProcessingStage)
class ProcessingStageAdmin(admin.ModelAdmin):
    list_display = ("batch", "stage_type", "facility", "status", "started_at", "ended_at")
    list_filter = ("stage_type", "status", "facility")
    search_fields = ("batch__batch_id", "facility")
