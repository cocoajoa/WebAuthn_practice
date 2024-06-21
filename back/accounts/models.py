from django.db import models

# Create your models here.
class WebUser(models.Model):
    username= models.TextField()
    credential_id = models.CharField(max_length=255, blank=True, null=True)
    credential_public_key = models.TextField(blank=True, null=True)
    sign_count = models.IntegerField(default=0)
    
    