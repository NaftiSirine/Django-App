from django import forms
from .models import Person

class LoginForm(forms.ModelForm):
    #class meta car ModelForm
    class Meta:
        model=Person
        fields=('username','password')
    password=forms.CharField(widget=forms.PasswordInput)