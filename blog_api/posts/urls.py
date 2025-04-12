from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

#  from .views import PostListCreateView, PostDetailView, UserListCreateView, UserDetailView

# urlpatterns = [
#     path('users/', UserListCreateView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
#     path('', PostListCreateView.as_view(), name='post-list'),
#     path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
# ]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
