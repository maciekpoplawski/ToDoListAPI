from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Todo(models.Model):
    """
    ToDo list model
    """


    NEW = 'NEW'
    DONE = 'DONE'

    TASK_STATUS_CHOICES = [
        (NEW, 'New'),
        (DONE, 'Done'),
    ]

    name = models.CharField(
        verbose_name='task name',
        null=True,
        blank=True,
        max_length=255
    )

    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
    )

    task_status = models.CharField(
        verbose_name='task status',
        max_length=4,
        choices=TASK_STATUS_CHOICES,
        default=NEW,
    )

    due_date = models.DateField(
        verbose_name='task due date',
        blank=True,
        null=True,
    )

    description = models.CharField(
        verbose_name='task description',
        null=True,
        blank=True,
        max_length=255
    )


    @property
    def delayed_status(self):
        if self.task_status=="NEW" and (self.due_date - date.today()).days < 0:
            return "DELAYED"


    def __str__(self):
        """
        String representation of model object.
        """

        return self.name
