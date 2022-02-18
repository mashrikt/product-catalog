from django.contrib import admin

from product_catalog.products.models import Product, ProductImage


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageAdmin,)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
