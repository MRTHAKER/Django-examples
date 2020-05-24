from django import forms
from . models import posts,comment

class postfrom(forms.ModelForm):
    class Meta:
        model=post
        fields=('author','title','text')
        widgets={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields=('author','text')
        widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
