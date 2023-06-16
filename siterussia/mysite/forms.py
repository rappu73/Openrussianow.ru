import form as form
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.http import HttpResponseRedirect

from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'photo', 'photo1', 'photo2', 'photo3', 'photo4', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'slug': forms.TextInput(attrs={'class': "form-control"}),
            'content': forms.Textarea(attrs={'class': "form-control"}),
            'photo': forms.FileInput(attrs={'class': "form-control-file"}),
            'photo1': forms.FileInput(attrs={'class': "form-control-file"}),
            'photo2': forms.FileInput(attrs={'class': "form-control-file"}),
            'photo3': forms.FileInput(attrs={'class': "form-control-file"}),
            'photo4': forms.FileInput(attrs={'class': "form-control-file"}),
            'cat': forms.Select(attrs={'class': "form-control"})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))
    content = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'class': 'form-control bg-secondary bg-opacity-25 text-white'}))
    captcha = CaptchaField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentNew
        fields = ('body', 'photo')
        widgets = {
            'body': forms.Textarea(attrs={'class': "form-control bg-secondary bg-opacity-25 text-white"}),
            'photo': forms.FileInput(attrs={'class': "form-control-file"})
        }





