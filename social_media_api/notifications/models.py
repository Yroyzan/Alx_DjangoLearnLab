from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="actor_notifications")
    verb = models.CharField(max_length=255)  # e.g., "liked", "commented", "followed"
    
    # generic relation to  to allow the notification to reference any model (like a post, comment, etc.)
    # This allows notifications to be flexible and not tied to a specific model.
    # For example, a notification can be for a post or a comment.
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey("target_content_type", "target_object_id")

    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target}"


# DOCUMENTATION
# This model lets you create flexible notifications for any kind of activity (like, comment, follow) 
# and link them to any object in your app (post, comment, etc.), while tracking who did the action, 
# who received it, and whether it’s been read.