# Generated by Django 3.0.3 on 2020-02-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200220_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='%Y/%m/%d')),
            ],
        ),
    ]