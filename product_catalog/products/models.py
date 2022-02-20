import os

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from sorl.thumbnail import ImageField
from urllib import request


IMAGE_SIZE = {
    'small': 256,
    'medium': 1024,
    'large': 2048
}


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(TimeStampMixin):
    url = models.URLField(max_length=9000)
    name = models.CharField(max_length=100, blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name or str(self.id)


class ProductImage(TimeStampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = ImageField(upload_to ='product-images/')
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f'{self.product} - {self.id}'

    def get_remote_image(self, url):
        result = request.urlretrieve(url)
        self.image.save(
            os.path.basename(url),
            File(open(result[0], 'rb'))
        )
        self.save()
