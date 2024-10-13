from django.db import models
from django.contrib.auth.models import User


# class about_us(models.Model):
#     paragraph = models.TextField()

#     def __str__(self):
#         return self.question




class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title[:20]}..."

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"