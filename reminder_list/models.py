from django.db import models

# Create your models here.

class Reminder(models.Model):
    title = models.CharField(max_length=200)
    reminder_time = models.DateTimeField('time to remind')

    def __str__(self):
        return self.title

