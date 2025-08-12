from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("post/new/", BlogCreateView.as_view(), name="post-new"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
