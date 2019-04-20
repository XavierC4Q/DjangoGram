from rest_framework import serializers
from .models import User, Post, Follow, Like

class UserSerializer (serializers.ModelSerializer):

    total_posts = serializers.SerializerMethodField(read_only=True)
    total_followers = serializers.SerializerMethodField(read_only=True)
    total_follows = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'date_joined',
            'last_login',
            'city',
            'country',
            'total_posts',
            'total_follows',
            'total_followers'
        )
        ordering = ['id']

    def get_total_posts(self, obj):
        return Post.objects.filter(user__id=obj.id).count()

    def get_total_followers(self, obj):
        return Follow.objects.filter(follows__id=obj.id).count()

    def get_total_follows(self, obj):
        return Follow.objects.filter(user__id=obj.id).count()



class PostsSerializer (serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer()

    class Meta:

        model = Post
        fields = '__all__'
        depth = 1
        ordering = ['-created']

    def get_like_count(self, obj):
        return Like.objects.filter(post__id=obj.id).count()

