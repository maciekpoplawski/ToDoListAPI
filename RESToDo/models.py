from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    """
    ToDo list model
    """

    name = models.CharField(
        verbose_name='task name',
        null=True,
        blank=True,
        max_length=255
    )

    user = models.ForeignKey(User,
        verbose_name='user name',
        on_delete=models.CASCADE,
    )

    is_new = models.BooleanField(
        verbose_name='task status NEW',
        default=True,
        blank=True,
        null=True,
    )

    is_done = models.BooleanField(
        verbose_name='task status DONE',
        default=False,
        blank=True,
        null=True,
    )

    due_date = models.DateTimeField(
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

    is_delayed = models.BooleanField(
        verbose_name='task delayed',
        default=False,
        blank=True,
        null=True,
    )


    def __str__(self):
        """
        String representation of model object.
        """

        return self.name
