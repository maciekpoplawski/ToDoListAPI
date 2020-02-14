from RESToDo import models
from .serializers import TodoSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    """
    Task API ViewSet.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('name', 'description')

    queryset = models.Todo.objects.all()

    def perform_create(self, serializer):
        """
        Assigning currently authenticated user to new Task object.
        """

        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Overridden queryset - will return objects for current user if user is authenticated.
        """

        return self.queryset.filter(user=self.request.user) if self.request.user.is_authenticated else self.queryset
