from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
import os
import project.settings as global_settings

from core.utils import files_in_directory

@login_required
def music(request):   
   
    """
    TODO
    """
    
    data = files_in_directory(global_settings.MUSIC_PATH)


    return TemplateResponse(request, 'entertainment/music.html', {
        'data': data
    })