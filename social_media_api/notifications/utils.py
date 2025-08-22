from .models import Notification

def create_notification(recipient, actor, verb, target=None):
    if recipient != actor:  # prevent self-notifications
        Notification.objects.create(
            recipient=recipient,
            actor=actor,
            verb=verb,
            target=target
        )
# This utility function creates a notification for the recipient when an action occurs.