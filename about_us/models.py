from django.db import models

class AboutUs(models.Model):
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.content