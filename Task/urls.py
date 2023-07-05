from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', UpdateTask.as_view()),
    path('', ReadTasks.as_view()),
    path('create', CreateTask.as_view()),
    path('delete/<int:pk>', DeleteTask.as_view())
]