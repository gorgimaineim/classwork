from django.db import models

STATUSES = {'draft': 'DRAFT',
            'in progress': 'IN PROGRESS',
            'completed': 'COMPLETED'}

class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=11, choices=STATUSES)
    description = models.CharField(max_length=100)

