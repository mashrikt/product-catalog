from django.conf import settings
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from sorl.thumbnail import get_thumbnail

from .models import IMAGE_SIZE, Product, ProductImage


class ProductImageSerializer(ModelSerializer):
    image = SerializerMethodField('get_resized_image')

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'created_at')

    def get_resized_image(self, obj):
        if not obj.image:
            return ""

        request = self.context.get('request')
        size_category = request.query_params.get('size')
        size = IMAGE_SIZE.get(size_category) if size_category else None
        original_size = obj.image.width
        if not size or original_size < size:
            return request.build_absolute_uri(obj.image.url)

        # height is smaller by the same ratio as the width
        width, height = size, (obj.image.height*original_size)//size
        image = get_thumbnail(obj.image, f'{width}x{height}')
        return request.build_absolute_uri(image.url)


class ProductImageDetailsSerializer(ProductImageSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'created_at', 'metadata')


class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(source='productimage_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'metadata', 'images')
        read_only_fields = ('name', 'metadata')
