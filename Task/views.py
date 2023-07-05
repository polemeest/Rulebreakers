from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *



class ReadTasks(generics.ListAPIView):
    ''' Read '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed']

class UpdateTask(generics.RetrieveUpdateAPIView):
    ''' Update '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTask(generics.CreateAPIView):
    ''' Create '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTask(generics.DestroyAPIView):
    ''' Delete '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
