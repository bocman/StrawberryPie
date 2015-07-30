from collections import OrderedDict
import os

#from settings.models import Client


#def dashboard_data():
 #   data = OrderedDict()

  #  data['clients_online'] = Client.objects.count()

   # return data


def format_time_interval(start_time, end_time):
    """
    This method is used to return custom formated time interval between
    two datetime objects. Result is returned in 'd h m s' style. If something
    result can't be calculates 'N/A' string is returned.
    """
    time_string = ""
    if not start_time or not end_time:
        return "N/A"
    elif start_time == end_time:
        return "0s"
    time_interval = end_time - start_time
    days = time_interval.days
    time_interval = time_interval.seconds
    hours = time_interval / 3600
    minutes = (time_interval % 3600) / 60
    seconds = (minutes % 60) / 60
    if days:
        time_string += str(days) + "d "
    if hours:
        time_string += str(hours) + "h "
    if minutes:
        time_string += str(minutes) + "m "
    if seconds:
        time_string += str(seconds) + "s "
    return time_string.strip()


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
        