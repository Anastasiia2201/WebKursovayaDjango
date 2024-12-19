from django import forms
from django.core.mail import send_mail
from django.contrib.auth import get_user_model


User = get_user_model()

class RegistrationForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('username', 'email', 'photo_check')


class UpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password', 'last_name', 'first_name', 'group', 'avatar', 'year')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class TokenForm(forms.Form):
    email = forms.EmailField()
    token = forms.CharField()
