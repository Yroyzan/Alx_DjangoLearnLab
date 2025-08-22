from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'), # This line was added to handle the feed view
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'), # This line was added to handle liking posts
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'), # This line was added to handle unliking posts

]

urlpatterns += router.urls


