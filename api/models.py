from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class User (AbstractUser):

    email = models.EmailField(blank=False, null=False)
    city = models.CharField(max_length=25, default='New York City')
    country = models.CharField(max_length=30, default='United States of America')
    profile_img = models.ImageField(
        upload_to='uploads/profile_images',
        blank=True,
        null=True
    )

    def __str__(self):
        return F'User: {self.username}'



class Post (models.Model):

    user = models.ForeignKey(User, related_name='user_post', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    img = models.ImageField(
        upload_to='uploads/post',
        blank=True,
        null=True
    )
    caption = models.TextField(default='')
    tags = ArrayField(
        models.CharField(max_length=50, default=''),
        default=list
    )

    def __str__(self):
        return F'Post: {self.id}'


class Follow (models.Model):

    user = models.ForeignKey(User, related_name='user_follow', on_delete=models.CASCADE)
    follows = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' follows ' + self.follows.username


class Like (models.Model):

    user = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_liked', on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' likes ' + self.post.id

