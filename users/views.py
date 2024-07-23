from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView

from users.forms import UserRegistrationForm
# Create your views here.

class RegisterView(CreateView):
    model = User
    from_class = UserRegistrationForm
    template_name = "users/register.html"