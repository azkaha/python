from django.db import models

# Create your models here.
class Todo(models.Model):
    tasktodo = models.CharField(max_length=100) # its ur todo item name
    ifcompleted = models.BooleanField(default=False) # checks if its completed or not
    created_at = models.DateTimeField(auto_now_add=True) # the date it was made (auto_now_add just sets it to the date it was made)
