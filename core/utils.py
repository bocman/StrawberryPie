from collections import OrderedDict
import os

from settings.models import Client


def dashboard_data():
    data = OrderedDict()

    data['clients_online'] = Client.objects.count()

    return data

def files_in_directory(path, file_types=None, file_list=None):
    """
    TODO
    """
    file_list = []
    
    for root, dirs, files in os.walk(path):
        path = root.split('/')
        #file_list.append((len(path) - 1) *'---' +str(os.path.basename(root)) )      
        parent = FileDirectory(os.path.basename(root), root, True)
        file_list.append(parent)
        for element in files:
            child = FileDirectory(element, os.path.join(root,element), False, parent)
            file_list.append(child)

    return file_list

class FileDirectory(object):
    """
    TODO
    """
    is_directory = None
    filename = None
    path = None
    parent = None

    def __init__(self, filename, path, is_directory, parent=None):
        self.is_directory = is_directory
        self.filename = filename
        self.is_directory = is_directory
        self.parent = parent

    def __str__(self):
        return self.filename +"    "+str(self.parent)

    def get_filename():
        return self.filename

    def get_path():
        return self.path

    def is_directory():
        return self.is_directory
        