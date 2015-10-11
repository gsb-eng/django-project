"""
Event based views.
"""

from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):

    template = loader.get_template('qanda/qanda_index.tpl')
    context = RequestContext(request, {
         'title': 'Q & A !!!',
     })
    return HttpResponse(template.render(context))
