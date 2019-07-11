from django import forms
from .models import *
from comment_app.models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"})
        }
        labels = {
            "title": "标题",
            "body": "正文"
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "url", "content"]

