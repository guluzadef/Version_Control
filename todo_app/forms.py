from django import forms
from .models import *


class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'desc']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'desc']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
