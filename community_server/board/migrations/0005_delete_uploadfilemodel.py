# Generated by Django 3.0.3 on 2020-02-26 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_uploadfilemodel_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFileModel',
        ),
    ]
