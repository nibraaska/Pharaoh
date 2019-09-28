from rest_framework import routers
from .api import PostViewSet

router = routers.DefaultRouter()
router.register('api/blog', PostViewSet, 'posts')

urlpatterns = router.urls