"""product_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from product_catalog.products.views import ProductImageListView, ProductImageRetrieveView, ProductListCreateView, ProductRetrieveView


api_patterns = [
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductRetrieveView.as_view()),
    path('images/', ProductImageListView.as_view()),
    path('images/<int:pk>/', ProductImageRetrieveView.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(arg=(api_patterns, 'api_patterns'), namespace='api')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
