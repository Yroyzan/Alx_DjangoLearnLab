from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterView, LoginView, ProfileView

router = DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', UserViewSet.as_view({'post': 'follow'}), name='follow-user'), # This line was added to handle following users
    path('unfollow/<int:pk>/', UserViewSet.as_view({'post': 'unfollow'}), name='unfollow-user'), # This line was added to handle unfollowing users
]

urlpatterns += router.urls
