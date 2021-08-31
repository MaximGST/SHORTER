from django import forms

from .models import Url

class UrlCreateforum(forms.ModelForm):
    
    class Meta:
        model = Url
        fields = ['origin_url']

        