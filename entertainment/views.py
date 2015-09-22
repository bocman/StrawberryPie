from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
import os
import requests
import json

import project.settings as global_settings


@login_required
def music(request):   
   
    """
    TODO
    """
    data ={

        'is_activated': True,

    }
    headers = {'Content-type': 'application/json'}
    r = requests.patch('http://192.168.1.130/rest/gpio/update/3/', data =json.dumps(data), headers=headers)
    data = r.text


    return TemplateResponse(request, 'entertainment/music.html', {
        'data': data
    })