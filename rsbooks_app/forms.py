from django import forms
from . models import  RSBook, RSAuthor

class RSAuthorForm(forms.ModelForm):

    class Meta:
        model=RSAuthor
        fields=['name']


class RSBookForm(forms.ModelForm):
    class Meta:
        model=RSBook
        fields='__all__'
        widgets={
            'title':forms.TextInput(attrs={'style':'font-family: Arial, sans-serif;', 'placeholder':'enter the book name...' }),
            'description':forms.Textarea(attrs={'style':'font-family: Arial, sans-serif; vertical-align: top; height:60px;', 'placeholder':'enter description...' }),
            'quantity': forms.TextInput( attrs={'style': 'font-family: Arial, sans-serif;', 'placeholder': 'enter the book quantity...'}),
            'price':forms.TextInput(attrs={'style':'font-family: Arial, sans-serif;', 'placeholder':'enter the book price...' }),
        }

