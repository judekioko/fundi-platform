from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from core.choices import CATEGORY_CHOICES

from .models import Provider


class ProviderRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    business_name = forms.CharField(max_length=120, label="Business / your name")
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    area = forms.CharField(max_length=120, label="Area you cover", widget=forms.TextInput(
        attrs={"placeholder": "e.g. Kilimani, Nairobi"}
    ))
    phone = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={"placeholder": "e.g. 0712 345 678"}
    ))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "rows": 3,
        "placeholder": "A short note on your experience (optional)",
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=commit)
        Provider.objects.create(
            user=user,
            business_name=self.cleaned_data["business_name"],
            category=self.cleaned_data["category"],
            area=self.cleaned_data["area"],
            phone=self.cleaned_data["phone"],
            bio=self.cleaned_data["bio"],
        )
        return user
