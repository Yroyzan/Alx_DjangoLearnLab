from django.contrib.auth.models import AbstractUser
from django.db import models

#class User(AbstractUser):
    #bio = models.TextField(blank=True, null=True)
    #profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    #followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    #def __str__(self):
       # return self.username


# for handling following 
class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,  # important: user A following user B ≠ B following A
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username
