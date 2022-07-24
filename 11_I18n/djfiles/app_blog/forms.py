from django import forms
from .views import Post
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False, label=_('Images'))

    class Meta:
        model = Post
        fields = ['title', 'description', 'images']


class UploadPostsForm(forms.Form):
    file = forms.FileField()
