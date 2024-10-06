from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(label = "사용자 아이디")
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "last_name", "first_name", "email")