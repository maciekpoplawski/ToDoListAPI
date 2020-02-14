from django.urls import path
from django.conf.urls import include
from RESToDo.router import router


urlpatterns = [
    path('v1/', include(router.urls))
]
