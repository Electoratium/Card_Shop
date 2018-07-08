from django import forms
from .models import AuthorModel, SlidesModel


class AuthorForm(forms.ModelForm):
    authorJob = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'maxlength': 256}), label='Ученая степень, место работы и т.д.')
    authorDescription = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'maxlength': 64}), label = 'Описание')
    class Meta:
        model = AuthorModel
        fields = [field.name for field in AuthorModel._meta.fields]



class SlidesForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'maxlength': 128}), label='Описание', required=False)
    class Meta:
        model = SlidesModel
        exclude = ['created']
