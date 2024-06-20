from django.db import models

# Create your models here.
class WebUser(models.Model):
    id= models.TextField(primary_key=True)
    username= models.TextField()
    publicKey = models.TextField()
    
    