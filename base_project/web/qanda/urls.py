"""
URL's for different parts of the application.
"""
from . import qanda
from django.conf.urls import url


urlpatterns = [
    url(r'^$', qanda.index, name='qanda_home_page'),
]
