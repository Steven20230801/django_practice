from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRigesterForm(UserCreationForm):
    email = forms.EmailField()
    brand = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "email", "brand", "department", "password1", "password2"]
