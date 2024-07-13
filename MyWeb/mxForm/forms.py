from django import forms
from .models import FundRation


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    pct = forms.IntegerField()
    comment = forms.CharField(max_length=100)


class FundForm(forms.ModelForm):
    class Meta:
        model = FundRation
        fields = ("name", "pct", "comment")
        # widgets = {
        #     "name": forms.TextInput(attrs={"class", "form-control"}),
        #     "pct": forms.TextInput(attrs={"class", "form-control"}),
        #     "comment": forms.TextInput(attrs={"class", "form-control"}),
        # }
