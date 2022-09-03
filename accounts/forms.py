from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'gender', 'email', 'phone_number']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ChangePasswordForm(PasswordChangeForm):
    pass
