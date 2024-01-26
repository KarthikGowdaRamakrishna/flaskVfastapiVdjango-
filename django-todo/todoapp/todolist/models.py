from django.db import models

# Create your models here.
class Todo(models.Model):
    #no need to create a 'id' feature django does that for us
    title=models.CharField(max_length=350)
    complete=models.BooleanField(default=False)
    # for accurate description
    def __str__(self):
        return self.title