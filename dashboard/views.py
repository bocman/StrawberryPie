from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse

import logging
from settings.models import Client

log = logging.getLogger(__name__)


def dashboard(request):
    """
    TODO
    """

    context = {
        'clients_online': Client.online.count(),
    }
    return TemplateResponse(request, 'dashboard/dashboard.html', context)