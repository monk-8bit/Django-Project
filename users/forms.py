from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

# Nested namespace for configurations, keeps configs in one place.
# Model to be affected. ex: Form.save() == User.save()
# Fields to be shown in form in order
#    "python.pythonPath": "C:\\Program Files (x86)\\Python37\\python.exe",
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
