from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
