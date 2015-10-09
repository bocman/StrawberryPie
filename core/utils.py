import os
import json
import logging
import requests
from datetime import date
from django.utils import timezone as tz


log = logging.getLogger(__name__)


def send_data(page_url, data=None, action_type=None):
    """
    TODO
    """
    data = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    request = requests.patch(url=page_url, data=data, headers=headers)
    return request.status_code


def activation(status, client_id=None, pin_number=None):
    """
    Function is used to activate specific modul on specific client.
    As parameter we get modul pin number and id of parent client. Then we
    fill those values in prepared url string, to get activation url.
    If activation was successfully we get status code 200 and
    we make note into the logs, otherway we make notes about failed activation
    :param client_id: Id of the client, if modul have a parent
    :param pin_number: GPIO number which is used by modul
    :param status: Value which tell as if we would like to activate
                   or deactivate value (True=activate, False=deactivate)
    :type client_id: Integer
    :type pin_number: Integer
    :type status: Boolean
    """
    from setting.models import Client
    data = {
        "is_activated": status
    }
    client = Client.objects.get(id=client_id)

    url = "http://{0}/rest/gpio/update/{1}/".format(client.ip_address, pin_number)
    log.info("PREPARE to activate modul with pin {0} on client {1}".format(pin_number, client.name))
    try:
        if send_data(url, data) == 200:
            if status == True:
                log.info("ACTIVATED modul with pin {0} on client {1}".format(pin_number, client.name))
            else:
               log.info("DEACTIVATED modul with pin {0} on client {1}".format(pin_number, client.name))
    except:
        log.info( "Failed to activate modul with pin{0} on client{1}".format(pin_number, client.name) )


def sunrise_time(datetime=None):
    """
    This method is used to return sunrise time for specific date,
    which we get as argument. In case that date isn't specified, then 
    function return today's sunrise time.
    """
    pass


def sunset_time(datetime=None):
    """
    This method is used to return sunset time for specific date,
    which we get as argument. In case that date isn't specified, then 
    function return today's sunset time.
    """ 
    request = requests.get(url=link)


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


def format_datetime(input_date):
    """
    TODO
    """
    if input_date.date() == date.today():
        log.info(input_date)
        log.info("-----------------------")
        return input_date.strftime('Today, %H:%M')
    else:
        return input_date


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