from django.urls import path
from . import views

urlpatterns = [
    path('', views.listPosts, name='ListPosts'),
    path('post/<int:id>', views.viewPost, name='ViewPost'),
    path('post/create', views.createPost, name='CreatePost'),
    path('post/<int:id>/edit', views.editPost, name='EditPost'),
    path('post/<int:id>/delete', views.deletePost, name='DeletePost'),
    path('post/<int:id>/add_comment', views.addComment, name='AddComment'),
    path('comment/<int:id>/edit', views.editComment, name='EditComment'),
    path('comment/<int:id>/delete', views.deleteComment, name='DeleteComment'),
]