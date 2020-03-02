from django.db import models

# Create your models here.
class UploadFileModel(models.Model):
    upload = models.ImageField(upload_to="")