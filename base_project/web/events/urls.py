"""
URL's for different parts of the application.
"""

from . import events
from django.conf.urls import url


urlpatterns = [
    url(r'^$', events.index, name="events_home_page"),
]
