from django import forms
from .models import Farm


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            "name",
            "owner_name",
            "location",
            "contact_email",
            "contact_phone",
            "certification",
        ]

