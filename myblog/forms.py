from django import forms
from .models import Post, Files, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from froala_editor.widgets import FroalaEditor


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Post
        fields = ('title', 'hashtag', 'text')


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UrlForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["Body"]
