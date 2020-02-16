from RESToDo import models
from .serializers import TodoSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny


class ListTasks(generics.ListAPIView):
    """
    View for listing all tasks.
    """
    permission_classes = (AllowAny,)
    serializer_class = TodoSerializer

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name', 'description', 'id')

    def get_queryset(self):
        return models.Todo.objects.all()


class TaskDetails(generics.RetrieveAPIView):
    """
    View for task details.
    """
    lookup_field = 'pk'
    permission_classes = (AllowAny,)
    serializer_class = TodoSerializer
    queryset = models.Todo.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    """
    Task API ViewSet.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    queryset = models.Todo.objects.all()

    def perform_create(self, serializer):
        """
        Assigning currently authenticated user to new task object.
        """

        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Overridden queryset - will return objects for current user.
        """

        return self.queryset.filter(user=self.request.user)
