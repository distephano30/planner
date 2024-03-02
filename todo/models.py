from django.db import models
from django.contrib.auth.models import User

# Create your models here.
progress_choice = [
    ('Not started', 'Not started'),
    ('In progress', 'In progress'),
    ('Completed', 'Completed'),
]
priority_choice = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]

class todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    progress = models.CharField(max_length=20, choices=progress_choice, blank=True, null=True)
    priority = models.CharField(max_length=20, choices=priority_choice, blank=True, null=True)
    assign_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('due_date',)
        db_table = 'todo'