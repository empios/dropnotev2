from django.db import models
from django.utils import timezone
from froala_editor.fields import FroalaField


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    hashtag = models.CharField(max_length=100)
    text = FroalaField(theme='dark')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Files(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300)

    def saveUrl(self):
        self.save()

    def __str__(self):
        return self.url


class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Body = models.TextField()
