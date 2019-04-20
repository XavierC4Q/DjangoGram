from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, LikeViewSet

router = DefaultRouter()

router.register(R'user', UserViewSet, 'User')
router.register(R'post', PostViewSet, 'Post')
router.register(R'like', LikeViewSet, 'Like')

urlpatterns = [
    path('', include(router.urls)),
]