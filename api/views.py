from rest_framework import viewsets
from .models import User, Post, Follow, Like
from .serializers import (
    UserSerializer,
    PostSerializer,
    FollowSerializer,
    LikeSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet (viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet (viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(methods=['GET'], detail=False)
    def user_posts(self, request):
        user_id = request.GET.get('user_id', 0)
        res = Post.objects.filter(user=user_id)

        serializer = self.get_serializer(res, many=True)

        return Response(serializer.data)



class FollowViewSet (viewsets.ModelViewSet):

    serializer_class = FollowSerializer
    queryset = Follow.objects.all()


class LikeViewSet (viewsets.ModelViewSet):

    serializer_class = LikeSerializer
    queryset = Like.objects.all()

