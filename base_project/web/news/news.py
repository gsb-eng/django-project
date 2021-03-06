"""
News based views.
"""

from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):

    template = loader.get_template('news/news_index.tpl')
    context = RequestContext(request, {
        'title': 'News !!!',
    })
    return HttpResponse(template.render(context))
