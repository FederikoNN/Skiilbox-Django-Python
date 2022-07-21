from django import forms
from .views import Post


class PostForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False, label='Прикрепить изображения')

    class Meta:
        model = Post
        fields = ['title', 'description', 'images']


class UploadPostsForm(forms.Form):
    file = forms.FileField()
