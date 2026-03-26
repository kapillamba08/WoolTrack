from django import forms
from .models import WoolBatch


class WoolBatchForm(forms.ModelForm):
    class Meta:
        model = WoolBatch
        fields = [
            "batch_id",
            "farm",
            "shear_date",
            "weight_kg",
            "quality_grade",
            "status",
            "current_location",
        ]

