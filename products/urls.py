from rest_framework import routers
from .views import ProductViewSet, ImageViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet, 'products')
router.register('products/images/', ImageViewSet, 'products/images')

urlpatterns = router.urls
