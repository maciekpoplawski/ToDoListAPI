from django.urls import path
from django.conf.urls import include
from RESToDo.router import router
from .views import ListTasks, TaskDetails


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/index/', ListTasks.as_view()),
    path('v1/details/<int:pk>/', TaskDetails.as_view()),
]
