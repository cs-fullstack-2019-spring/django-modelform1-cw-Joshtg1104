from django import forms
from .models import BlogPost

# binds a form to the BlogPost model
class NewPostForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ['title', 'text']
