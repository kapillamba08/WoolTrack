from django import forms
from .models import DistributionEvent


class DistributionEventForm(forms.ModelForm):
    class Meta:
        model = DistributionEvent
        fields = [
            "batch",
            "event_type",
            "location",
            "timestamp",
            "quantity_kg",
            "notes",
        ]

