from django import forms
from .models import ProcessingStage


class ProcessingStageForm(forms.ModelForm):
    class Meta:
        model = ProcessingStage
        fields = [
            "batch",
            "stage_type",
            "facility",
            "started_at",
            "ended_at",
            "status",
            "notes",
        ]

