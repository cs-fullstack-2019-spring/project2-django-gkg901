from django import forms
from .models import relatedModel, postModel


class relatedForm(forms.ModelForm):
    class Meta:
        model = relatedModel
        exclude = ['created', 'updated', 'post']


class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        exclude = ['created', 'updated', 'userTableForeignKey']
