from django import forms
from .models import Home


class HomeForm(forms.ModelForm):
    video = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Write a url",
        }
    )),
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Write a name",
        }
    ))

    class Meta:
        model = Home
        fields = ('video', 'name')