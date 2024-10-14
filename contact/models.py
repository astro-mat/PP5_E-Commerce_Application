from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Customer Email'
        verbose_name_plural = 'Customer Emails'

    def __str__(self):
        return f"{self.name} - {self.email}"