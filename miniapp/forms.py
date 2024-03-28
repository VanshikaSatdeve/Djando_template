from django import forms
from .models import Post, Post_By

class Post_ByForm(forms.ModelForm):
    class Meta:
        model = Post_By
        fields = ['first_name', 'last_name', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_name', 'title', 'extract', 'content', 'posted_by', 'image', 'imagesecond', 'imagethird']


