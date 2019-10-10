from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'text']
        labels = {
            'title': "Заголовок", 'text': "Текст рецензии"
        }

class LoginForm(forms.Form):
      username = forms.CharField()
      password = forms.CharField(widget=forms.PasswordInput)
