# Generated by Django 4.2 on 2024-10-14 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='title',
        ),
    ]
