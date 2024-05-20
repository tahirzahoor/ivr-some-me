from django.urls import path
from .views import scrape_top_news

urlpatterns = [
    path('scrape-top-news/', scrape_top_news, name='scrape_top_news'),
]