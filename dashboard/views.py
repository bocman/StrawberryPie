from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse

import logging


log = logging.getLogger(__name__)


def test_dashboard(request):
    """
    TODO
    """

    return HttpResponse("delam daj ")
