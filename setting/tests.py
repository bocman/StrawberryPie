from django.test import TestCase
from django.test import Client as connectionClient
from models import Client 

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
        print "sem pognal teste"
        response = self.connection.get('/settings/clients/add/')
        print response.content
        print response.status_code