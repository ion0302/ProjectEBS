from django.http import Http404

from .models import Product, Image
from rest_framework import viewsets
from .serializers import ProductSerializer, ImageSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# def detail(request, product_id):
#     try:
#         p = Product.objects.get(id=product_id)
#     except:
#         raise Http404("No found")
#
#     photos = p.images_set.orderby('-id')
