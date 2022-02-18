from rest_framework.serializers import ModelSerializer

from .models import Product, ProductImage


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')


class ProductImageDetailsSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'metadata')


class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(source='productimage_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'images')
        read_only_fields = ('name',)
