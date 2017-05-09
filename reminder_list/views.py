import dateutil.parser
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Reminder


def index(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminder_list/index.html', {'reminders': reminders})


def add_reminder(request):
    return render(request, 'reminder_list/add_reminder.html', {})


def successful_add(request):
    new_reminder = Reminder(title=request.POST['title'],
                            reminder_time=dateutil.parser.parse(request.POST['reminder_time']))
    new_reminder.save()
    return HttpResponseRedirect(reverse('reminder_list:index'))
