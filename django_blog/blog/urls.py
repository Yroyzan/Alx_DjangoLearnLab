from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, add_comment, CommentUpdateView, CommentDeleteView, PostByTagListView, search_posts


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/Update/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/comments/new/', add_comment, name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tag_posts'),
    path('search/', search_posts, name='search_posts'),
]