"""
Event based views.
"""

from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):

    template = loader.get_template('admin/admin_index.tpl')
    context = RequestContext(request, {
        'title': 'Admin !!!',
    })
    return HttpResponse(template.render(context))
