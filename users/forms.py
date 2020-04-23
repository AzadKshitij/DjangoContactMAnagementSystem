from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    info = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Write something about your self'}),)

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }
        fields = ['username', 'email', 'info', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    info = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Write something about your self'}),)

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }
        fields = ['username', 'email', 'info']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
