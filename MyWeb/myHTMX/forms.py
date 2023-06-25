from django import forms

# from django.forms.models import inlineformset_factory

from django import forms
from .models import UserEntry


class UserEntryForm(forms.ModelForm):
    class Meta:
        model = UserEntry

        fields = [
            "name",
            "contact",
            "email",
            "description1",
            "description2",
            "description3",
            "note1",
            "note2",
            "note3",
            "note4",
            "status",
            "pnl",
            "content",
            "comment1",
            "comment2",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "contact": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"cols": 20, "rows": 5}),
            "comment1": forms.Textarea(attrs={"cols": 30, "rows": 10}),
        }
