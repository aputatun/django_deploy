from django.db import models

# Create your models here.
class Users(models.Model):
    userfirst = models.CharField(max_length= 264)
    userlast = models.CharField(max_length= 265)
    userEmail = models.URLField()
