from dataclasses import fields
from pyexpat import model
from django import forms
from post.models import Post

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption', 'tags']
        widgets = {
                    'caption' : forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows':4}),
                    'tags' : forms.TextInput(attrs={'class': 'form-control form-control-lg', 'rows':1}),
                    'image' : forms.FileInput(attrs={"class": "form-control form-control-lg"}),


        }