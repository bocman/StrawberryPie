from django.test import TestCase
from django.test import Client as connectionClient
from models import Client, Event
from django.contrib.auth.models import User

from django.contrib.auth.models import User

class StrawberryTestCase(TestCase):
    
    def setUp(self):
        self.connection = connectionClient()
        user = User(username="test")
        user.set_password("test")
        user.save()

        #self.connection.login(username='bostjan', password='bostjan')
    
    def test_login(self):
        #self.connection.login(username='bostjan', password='bostjan')
        response = self.connection.get('/dashboard/', follow=True)
        print response.content


class ClientTestCase(TestCase):

    def setUp(self):
        self.connection = connectionClient()
        self.connection.login(username='bostjan', password='bostjan')

    def test_create_client(self):
        """
        TODO
        """
        data = {
            'name': 'Test',
            'description': 'Test case for client',
            'ip_address': '123.123.123',
            'port': 8000,

        }
        response = self.connection.get('/settings/clients/add/', follow=True)
        print response.content
        print response.status_code


class EventTestCase(TestCase):
    """
    TODO
    """

    def setUp(self):
        self.connection = connectionClient()

        self.connection.login(username='bostjan', password='bostjan')

    def test_start_greater_then_end_time(self):
        c = connectionClient()
        user = User.objects.create(username="bostjan")
        user.set_password("bostjan")
        user.save()
        c.login(username='bostjan', password='bostjan')
        current_num_events = Event.objects.count()
        response = c.post('/settings/events/add/', {
            'name': "Test name",
            'start_time': '2015-10-13 10:10',
            'end_time': '2015-10-10 10:25'
            },
            follow = True
        )
        #print response.content
        print response.context['form'].errors
        print str(current_num_events) +" "+ str(Event.objects.count()) + " -------->"
        print "status code "+ str(response.status_code)

        #self.assertEqual(my_func(a, 0), 'larry')

    def test_end_time_lesser_then_start_time(self):
        pass

    def test_blank_start_time(self):
        pass

    def test_blank_end_time(self):
        pass

    def test_blank_name(self):
        pass

    def test_delete_event(self):
        pass

    def test_create_event(self):
        pass

    def test_cancel_running_event(self):
        pass

    def test_modul_already_reserved_in_other_event(self):
        pass

    def test_group_already_reserverd_in_other_event(self):
        pass








