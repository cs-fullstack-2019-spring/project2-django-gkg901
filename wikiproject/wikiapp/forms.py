from django import forms
from .models import RelatedModel, PostModel


class relatedForm(forms.ModelForm):
    class Meta:
        model = RelatedModel
        exclude = ['created', 'updated', 'post']


class postForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ['created', 'updated', 'userTableForeignKey']
