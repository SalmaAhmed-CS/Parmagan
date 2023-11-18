
from django import forms


class searchform(forms.Form):
    word = forms.CharField(label="word", max_length=100)
