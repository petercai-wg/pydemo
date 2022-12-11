from django import forms

from .models import Person, City, Car

from . import Util


# class CarListingForm(forms.ModelForm):
#     brand = forms.ChoiceField(choices=Util.getDBChoice(
#         'select distinct brand from myApp_car', 'Car_Brand'))

#     class Meta:
#         model = Car
#         exclude = ['brand']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(
                    country_id=country_id).order_by('name')

            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by(
                'name')


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'id': 'my-id'
            }
        ),
        help_text='Help_text:  Form.name'
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={'style': 'border-color: green;'})
    )

    password = forms.CharField(widget=forms.PasswordInput())

    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        help_text='Help_text:  Write here your message!',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            attrs = {
                "placeholder": f'Place holder {str(field)}',
                "class": 'form-control'
            }

            self.fields[str(field)].widget.attrs.update(attrs)

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')

        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')
        else:
            print("pass clean")

    def clean_password(self, *args, **kwargs):
        passwd = self.cleaned_data.get("password")
        if passwd == '12345':
            print("rase validate error for password")
            raise forms.ValidationError("Password can't be 12345")
        return passwd
