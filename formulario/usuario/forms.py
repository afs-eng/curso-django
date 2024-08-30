from django import forms
from isort.profiles import attrs


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': '',
        'type': 'text',
        'placeholder': 'name'
    }))

    password = forms.CharField( widget=forms.PasswordInput(attrs={
        'class': '',
        'type': 'password',
        'placeholder': 'senha'
    }))


class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': '',
        'type': 'text',
        'placeholder': 'name'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': '',
        'type': 'password',
        'placeholder': 'senha'
    }))

    password = forms.CharField( widget=forms.PasswordInput(attrs={
        'class': '',
        'type': 'password',
        'placeholder': 'senha'
    }))

    confirmar_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': '',
        'type': 'password',
        'placeholder': 'confirmar_senha'
    }))