from rest_framework import generics

from .models import Product, ProductImage
from .serializers import ProductImageDetailsSerializer, ProductSerializer
from ..celery import scrape_ebay


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ('url',)

    def perform_create(self, serializer):
        obj = serializer.save()
        scrape_ebay.delay(obj.id)


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
