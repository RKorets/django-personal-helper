from django import forms
from django.forms import ModelForm

from .models import *


class TagForm(ModelForm):
    tag = forms.CharField(label='Tag name', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['tag']


class NoteForm(ModelForm):
    name = forms.CharField(label='Note name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control',  'rows': 8}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Note
        fields = ['name', 'text', 'tags']
