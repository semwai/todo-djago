from django import forms
from base.models import Project

class TaskGroupForm(forms.Form):
    name = forms.CharField(label="Название")
    description = forms.CharField(label="Описание", widget=forms.Textarea)
    Project = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(TaskGroupForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'


