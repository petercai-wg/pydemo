from django import forms
from .models import FundRation


class FundForm(forms.ModelForm):
    class Meta:
        model = FundRation
        fields = ("name", "pct", "comment")
        # widgets = {
        #     "name": forms.TextInput(attrs={"class", "form-control"}),
        #     "pct": forms.TextInput(attrs={"class", "form-control"}),
        #     "comment": forms.TextInput(attrs={"class", "form-control"}),
        # }
