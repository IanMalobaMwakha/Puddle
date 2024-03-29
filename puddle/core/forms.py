from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from .models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'location', 'bio')

    avatar = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'placeholder': 'Image Avatar/Profile Picture',
        'class': 'w-full py-4 px-6 rounded-xl border'
    }))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your location',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Enter your Bio/About',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))