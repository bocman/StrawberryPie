from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
import os
import requests
import json

import project.settings as global_settings

from core.utils import files_in_directory

@login_required
def music(request):   
   
    """
    TODO
    """
    data ={
        'pin_number': 9,
        'is_activated': False,
        'is_input': False,
        'interval': 0,
        'is_general': True
    }
    headers = {'Content-type': 'application/json'}
    r = requests.patch('http://localhost:8002/rest/gpio/update/6/', data =json.dumps(data), headers=headers)
    data = r.text


    return TemplateResponse(request, 'entertainment/music.html', {
        'data': data
    })