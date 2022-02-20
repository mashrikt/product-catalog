import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_catalog.settings')
app = Celery('product_catalog')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task(bind=True)
def scrape_ebay(self, product_id):
    from product_catalog.products.models import Product, ProductImage
    from product_catalog.scraper import EbayScraper
    product = Product.objects.get(id=product_id)
    scraper = EbayScraper(product.url)
    product.name, product.metadata['rating'] = scraper.get_product_details()
    product.save()

    url, alt = scraper.get_image_data()
    metadata = { 'alt': alt, 'url': url }
    image = ProductImage(product=product, metadata=metadata)
    image.get_remote_image(url)
