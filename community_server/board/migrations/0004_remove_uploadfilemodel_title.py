# Generated by Django 3.0.3 on 2020-02-25 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_uploadfilemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfilemodel',
            name='title',
        ),
    ]