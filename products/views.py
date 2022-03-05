from . import serializers
from .models import Product, Image
from rest_framework import viewsets
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductImgSerializer
        if self.action == 'retrieve':
            return serializers.ProductSerializer
        return serializers.ProductImgSerializer
