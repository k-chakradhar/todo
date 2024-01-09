from django.db import models

# Create your models here.
class Todo(models.Model):
    t_title = models.CharField(max_length =50)
    t_description = models.TextField()