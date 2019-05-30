from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

# Nested namespace for configurations, keeps configs in one place.
# Model to be affected. ex: Form.save() == User.save()
# Fields to be shown in form in order
#    "python.pythonPath": "C:\\Program Files (x86)\\Python37\\python.exe",
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # Model Form: Form to work with a specific Database Model.
    email = forms.EmailField()

    class Meta:
        # To pass User to Model Form in View:
        #   modelForm( instance = request.user )
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
