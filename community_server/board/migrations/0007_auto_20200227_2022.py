# Generated by Django 3.0.3 on 2020-02-27 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_board_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='thumbnail',
            field=models.CharField(default='', max_length=200),
        ),
    ]
