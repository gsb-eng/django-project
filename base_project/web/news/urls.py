"""
URL's for different parts of the application.
"""

from django.conf.urls import url


urlpatterns = [
    url(r'^/', 'views.index'),
]
