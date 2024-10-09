from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question