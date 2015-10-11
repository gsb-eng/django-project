"""
URL's for different parts of the application.
"""

from . import admin
from django.conf.urls import url


urlpatterns = [
    url(r'^$', admin.index, name="admin_home_page"),
]
