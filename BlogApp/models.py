from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
