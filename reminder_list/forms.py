from django.forms import ModelForm
from django import forms
from .models import Reminder
from .widgets import DateTimeInput


class ReminderForm(ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'reminder_time', 'description']

    reminder_time = forms.DateTimeField(widget=DateTimeInput())
    description = forms.CharField(required=False, max_length=500)
