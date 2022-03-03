from rest_framework import serializers
from .models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'
