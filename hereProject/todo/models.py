from django.db import models

# Create your models here.

#runserver하면 primary_key란이 있어야하는데 왜 없을까...
class Todo(models.Model):
    id=models.AutoField(primary_key=True)
    content=models.CharField(max_length=200)
    is_done=models.BooleanField()

    def __str__(self):
        return self.content
