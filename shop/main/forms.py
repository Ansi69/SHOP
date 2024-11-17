from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from main.models import User

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )
    
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class CustomPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField()
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()