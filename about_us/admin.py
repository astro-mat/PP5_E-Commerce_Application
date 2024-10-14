from django.contrib import admin
from .models import AboutUs

# Register your models here.
class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'order',
    )

    ordering = ('order',)

admin.site.register(AboutUs, AboutUsAdmin)