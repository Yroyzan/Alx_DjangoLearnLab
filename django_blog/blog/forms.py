from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from taggit.forms import TagField, TagWidget


# ---------- User Forms ----------
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")


# ---------- Post Form ----------
class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


# ---------- Comment Form ----------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment...'
            }),
        }
