from django.forms import ModelForm
from .models import Reminder


# TODO add support for selecting date rather than typing it
class ReminderForm(ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'reminder_time', 'description']
