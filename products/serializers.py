from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

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


class OneImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['photo']


class ProductImgSerializer(serializers.ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, product):
        return OneImgSerializer(product.image.first()).data
