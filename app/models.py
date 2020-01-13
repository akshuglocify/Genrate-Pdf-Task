from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    age = models.IntegerField()


class ProfilePicture(models.Model):
    profile_pic = models.ImageField(upload_to = 'image/')