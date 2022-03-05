from rest_framework import routers

from . import views
from .views import ProductViewSet, ImageViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, 'products')
router.register('products/images/', ImageViewSet, 'products/images')

urlpatterns = router.urls
