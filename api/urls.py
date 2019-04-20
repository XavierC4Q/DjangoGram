from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet

router = DefaultRouter()

router.register(R'user', UserViewSet, 'User')
router.register(R'post', PostViewSet, 'Post')

urlpatterns = [
    path('', include(router.urls)),
]