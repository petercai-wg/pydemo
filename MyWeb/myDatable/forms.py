from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        fields = ['name', 'contact', 'email']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'contact': forms.TextInput(attrs={'class': 'form-control'}),
                   }
