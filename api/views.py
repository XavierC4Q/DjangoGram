from rest_framework import viewsets
from .models import User, Post
from .serializers import UserSerializer, PostsSerializer

class UserViewSet (viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class PostViewSet (viewsets.ModelViewSet):

    serializer_class = PostsSerializer
    queryset = Post.objects.all()

