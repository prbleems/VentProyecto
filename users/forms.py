# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # tu modelo custom, supongo que se llama User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # ajusta según campos de tu User
