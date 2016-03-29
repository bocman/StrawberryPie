from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.template.response import TemplateResponse
from os import path, listdir, walk
import fnmatch
import requests
import json

import project.settings as settings

import logging
log = logging.getLogger(__name__)

class Song(object):
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def get():
        return ""

class music(View):
    """
    TODO
    """
    template_name = 'entertainment/music.html'

    def get(self, request, *args, **kwargs):
        directory = path.join(settings.SONGS_ROOT, str(request.user))
        import os
        songs = []
        for root, dirs, files in os.walk(directory):
          for file in files:
            if file.endswith('.docx'):
              songs.append(Song("nekaj", "nekajs"))
              songs.append(os.path.join(root, file))
            if file.endswith('.mp3'):
              songs.append(os.path.join(root, file))
        log.info(songs[0].path)
        return TemplateResponse(request, self.template_name)
