"""
URL's for different parts of the application.
"""
from . import news
from django.conf.urls import url


urlpatterns = [
    url(r'^$', news.index, name='news_home_page'),
]
