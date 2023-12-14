from django import forms
from .models import GalleryModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryModel
        fields = '__all__'
        labels = {'photo':''}

class SignupForm(UserCreationForm):
    password = None
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}




