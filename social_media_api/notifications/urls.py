from django.urls import path
from .views import NotificationListView


# This URL configuration handles the notifications endpoint, allowing users to view their notifications.
urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
]