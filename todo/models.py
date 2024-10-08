from django.db import models

# Create your models here.

class Todos(models.Model):

    title=models.CharField(max_length=300)

    desc=models.TextField()

    completed=models.BooleanField(default=False)

    def __str__(self)->str:
        return self.title
    #It is a dunder method it returns string representation of an object here -->str is a type hint.