from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'follow', FollowViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
