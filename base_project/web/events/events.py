"""
Event based views.
"""

from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):

    template = loader.get_template('events/events_index.tpl')
    context = RequestContext(request, {
        'title': 'Events !!!',
    })
    return HttpResponse(template.render(context))
