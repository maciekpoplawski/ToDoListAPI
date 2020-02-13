from rest_framework import serializers
from RESToDo import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'user',
            'is_new',
            'is_done',
            'due_date',
            'description',
            'is_delayed',
        )
        model = models.Todo
