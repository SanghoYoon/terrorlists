from django import forms
from .models import Post

#class PostForm(forms.Form):
#    title = forms.CharField()
#    position = forms.CharField()
#    text = forms.CharField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','position','text',)