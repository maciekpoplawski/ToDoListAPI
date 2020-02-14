from rest_framework import serializers
from RESToDo import models

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username', default='anonymous')
    is_task_delayed = serializers.ReadOnlyField(source='delayed_status')

    class Meta:
        fields = '__all__'
        model = models.Todo
