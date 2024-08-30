from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField


class RegisterForm(UserCreationForm):

    phone_number = PhoneNumberField()
    country = CountryField().formfield()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "phone_number",
                  "country", "password1", "password2")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=155)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ("username", "password")
