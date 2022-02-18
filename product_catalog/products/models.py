from django.db import models

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(TimeStampMixin):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100, blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name or str(self.id)


class ProductImage(TimeStampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='product-images/')
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f'{self.product} - {self.id}'
