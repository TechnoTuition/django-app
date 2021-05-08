from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    massege = models.TextField(max_length=400)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return self.name
