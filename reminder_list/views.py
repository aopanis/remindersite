import dateutil.parser
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser
from django.urls import reverse
from django.shortcuts import render
from .models import Reminder
from .serializers import ReminderSerializer
from .forms import ReminderForm


# View for the index of the website, displays the index template
# TODO order notifications by urgency
def index(request):
    reminders = Reminder.objects.all().order_by('reminder_time')
    return render(request, 'reminder_list/index.html', {'reminders': reminders})


# View to add a new reminder, displays the add_reminder template
def edit(request, action):
    if action == 'new':
        form = ReminderForm()
        pk = -1
    else:
        form = ReminderForm(instance=Reminder.objects.get(pk=action))
        pk = action
    return render(request, 'reminder_list/add_reminder.html', {'form': form, 'pk': pk})


# View for creating a new reminder, receives info from add_reminder template and adds a new entry to the DB
def successful_add(request):
    pk = int(request.POST['pk'])
    if pk > 0:
        reminder = Reminder.objects.get(pk=pk)
        reminder.title = request.POST['title']
        reminder.description = request.POST['description']
        reminder.reminder_time = dateutil.parser.parse(request.POST['reminder_time'])
        reminder.save()
    else:
        new_reminder = Reminder(title=request.POST['title'],
                                description=request.POST['description'],
                                reminder_time=dateutil.parser.parse(
                                    request.POST['reminder_time']))
        new_reminder.save()
    return HttpResponseRedirect(reverse('reminder_list:index'))


def detail(request, question_id):
    reminder = Reminder.objects.get(pk=question_id)
    return render(request, 'reminder_list/detail.html', {'reminder': reminder,
                                                         'pk': question_id})


def delete(request, question_id):
    reminder = Reminder.objects.get(pk=question_id)
    reminder.delete()
    return HttpResponseRedirect(reverse('reminder_list:index'))


# TODO add support for editing existing reminders
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def reminder_api(request):
    """
    List all reminders, or create a new reminder
    """
    if request.method == 'GET':
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReminderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
