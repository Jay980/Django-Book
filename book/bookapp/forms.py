from django import forms
from django.contrib.auth.models import User
from . import models
from django import forms
class bookform(forms.ModelForm):
        class Meta:
            model=models.Bookinfo
            fields=['book_name','author','genre','language']
