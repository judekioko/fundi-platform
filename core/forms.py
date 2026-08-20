from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["category", "description", "location", "urgency", "name", "phone"]
        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "e.g. My business Wi-Fi keeps disconnecting every afternoon around 2-4pm.",
            }),
            "location": forms.TextInput(attrs={"placeholder": "e.g. Kilimani, Nairobi"}),
            "name": forms.TextInput(attrs={"placeholder": "Full name"}),
            "phone": forms.TextInput(attrs={"placeholder": "e.g. 0712 345 678"}),
        }
