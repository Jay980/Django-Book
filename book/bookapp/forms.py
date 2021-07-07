from django import forms
from django.contrib.auth.models import User
from . import models
class bookform(forms.ModelForm):
    
    book_name = forms.CharField()
    author = forms.CharField()
    genre = forms.CharField()
    language = forms.CharField()
    class Meta:
        model=models.Bookinfo
        fields=['book_name','author','genre','language']
