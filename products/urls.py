from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


app_name = 'products'
urlpatterns = [
    path(
        'products/',
        views.product,
        name='products',
    ),
    path(
        'products/<int:product_id>/',
        views.product_view,
        name='product_detail',
    ),
    path(
        'categories/',
        views.categories,
        name='categories',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
