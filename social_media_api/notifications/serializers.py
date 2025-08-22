from rest_framework import serializers
from .models import Notification


# Serializer for Notification model
class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'is_read', 'timestamp']
