from django import forms
from base.models import Project

class TaskGroupForm(forms.Form):
    name = forms.CharField(label="Название")
    description = forms.CharField(label="Описание", widget=forms.Textarea)
    Project = forms.IntegerField(widget=forms.HiddenInput())



