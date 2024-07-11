from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm, Textarea, TextInput


class UserOurRegistration(UserCreationForm): #форма регистрации
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        email = forms.EmailField()


class PostsForm(ModelForm): #форма поста
    class Meta:
        model = Posts
        fields = ['title', 'cat', 'full_text', 'photo']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название поста'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст поста'
            }),
        }


class ProfileForm(ModelForm): #форма профиля пользователя
    class Meta:
        model = Profile
        fields = ['first_name', 'phone', 'avatar']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш номер телефона'
            }),
        }


class CommentsForm(ModelForm): #форма комментариев
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий'
            })
        }
