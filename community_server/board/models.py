from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    writer = models.CharField(max_length=10)
    writer_ip = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=10)
    post_hit = models.IntegerField(default=0)
    thumbnail = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.title