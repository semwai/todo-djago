from django import forms
from base.models import Project


class TaskGroupForm(forms.Form):
    name = forms.CharField(label="Название")
    description = forms.CharField(label="Описание", widget=forms.Textarea)
    project_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(TaskGroupForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'


class TaskForm(forms.Form):
    name = forms.CharField(label="Название")
    text = forms.CharField(label="Описание", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['class'] = 'form-control'


class ProjectForm(forms.Form):
    name = forms.CharField(label="Название проекта")

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
