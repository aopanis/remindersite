from rest_framework import serializers
from reminder_list.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=500, required=False, default='')
    class Meta:
        model = Reminder
        fields = ('title', 'reminder_time', 'description', 'pk')

    def create(self, validated_data):
        return Reminder.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.reminder_time = validated_data.get('reminder_time', instance.reminder_time)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
