from django import forms
from main.models import Clients
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

class ClientCreationForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneNumberField()
    class Meta:
        model = Clients
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')