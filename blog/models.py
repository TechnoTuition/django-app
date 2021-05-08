from django.db import models

# Create your models here.
class Post(models.Model):
    sno_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=3000)
    slug = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    def __str__(self):
        return self.title