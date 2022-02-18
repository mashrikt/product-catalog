from product_catalog.products.models import Product
from rest_framework import generics

from .models import Product, ProductImage
from .serializers import ProductImageDetailsSerializer, ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ('url',)


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageListView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailsSerializer
    filterset_fields = ('product__url',)


class ProductImageRetrieveView(generics.RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailsSerializer
