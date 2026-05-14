from django import forms
from .models import Tweet

# craftng forms
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        