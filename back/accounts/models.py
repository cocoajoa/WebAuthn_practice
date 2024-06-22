from django.db import models

# Create your models here.
class WebUser(models.Model):
    username= models.TextField()
    credential_id = models.BinaryField()
    credential_public_key = models.BinaryField()
    sign_count = models.IntegerField(default=0)
    
    