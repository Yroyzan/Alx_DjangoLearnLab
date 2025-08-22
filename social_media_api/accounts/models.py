from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # ✅ Explicit "following" field (the people I follow)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username
