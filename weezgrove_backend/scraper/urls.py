from django.urls import path
from .views import scrape_flower_shop

urlpatterns = [
    path('scrape-flower-shop/', scrape_flower_shop, name='scrape_flower_shop'),
]