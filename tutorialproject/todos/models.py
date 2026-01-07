from django.db import models


class PriorityChoices(models.IntegerChoices):
    LOW = 1, 'Low'
    MEDIUM = 2, 'Medium'
    HIGH = 3, 'High'
    URGENT = 4, 'Urgent'

class Todos(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    deadline = models.DateField(blank=True, null=True)
    priority = models.IntegerField(choices=PriorityChoices.choices, default=PriorityChoices.LOW, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.title}"
