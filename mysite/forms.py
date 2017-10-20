#  coding: utf-8
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from mysite.models import Tasks,StatusOfTasks




class LoginForm(forms.Form):
    login = forms.ModelChoiceField(queryset=User.objects.all())
    password = forms.CharField( widget=forms.PasswordInput)


class MainForm(forms.Form):
    status = forms.ModelChoiceField(queryset=StatusOfTasks.objects.all())
    start  = forms.DateField( widget=SelectDateWidget )
    finish  = forms.DateField( widget=SelectDateWidget)




class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['user','title', 'start', 'finish', 'status','description','comments']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = widgets.AdminTextareaWidget(attrs={'cols': 80, 'rows': 1})
        self.fields['description'].widget = widgets.AdminTextareaWidget(attrs={'cols': 90, 'rows': 10})
        self.fields['comments'].widget = widgets.AdminTextareaWidget(attrs={'cols': 90, 'rows': 10})
        self.fields['start'].widget =    SelectDateWidget()
        self.fields['start'].widget.attrs['disabled'] = True
        self.fields['finish'].widget = SelectDateWidget()

