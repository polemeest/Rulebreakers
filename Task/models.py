from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True)

    class Meta():
        db_table = 'Task'
