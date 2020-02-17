from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils.timezone import now, timedelta
from RESToDo.models import Todo


class Command(BaseCommand):
    """
    External manage.py command
    """

    help = 'Creates initial data for models.'

    def handle(self, *args, **options):
        """
        Override BaseCommand handle method.
        """

        user1 = User.objects.first()
        user2 = User.objects.all()[1]

        Todo.objects.create(
            name='Admin task',
            user=user1,
            task_status="NEW",
            due_date=now() + timedelta(days=5),
            description='Some description'
        )

        Todo.objects.create(
            name='Admin task delayed',
            user=user1,
            task_status="NEW",
            due_date=now() - timedelta(days=5),
            description='Some description for delayed'
        )

        Todo.objects.create(
            name='Admin task DONE test',
            user=user1,
            task_status="DONE",
            due_date=now() - timedelta(days=5),
            description='Some description'
        )

        Todo.objects.create(
            name='Task for TEST USER',
            user=user2,
            task_status="NEW",
            due_date=now() + timedelta(days=5),
            description='Some description bla bla bla'
        )

        Todo.objects.create(
            name='DELAYED Task for TEST USER',
            user=user2,
            task_status="NEW",
            due_date=now() - timedelta(days=15),
            description='Some description for DELAYED'
        )

        self.stdout.write(self.style.SUCCESS('Succesfully added initial test data'))
