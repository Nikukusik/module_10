from django.forms import CharField, TextInput, EmailInput, EmailField, PasswordInput, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = CharField(max_length=30, required=True, widget=TextInput(attrs={"class": "form-control", }))
    email = EmailField(max_length=30, required=True, widget=EmailInput(attrs={"class": "form-control", }))
    password1 = CharField(required=True, widget=PasswordInput(attrs={"class": "form-control", }))
    password2 = CharField(required=True, widget=PasswordInput(attrs={"class": "form-control", }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
