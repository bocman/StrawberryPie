from django.forms import ModelForm
from models import Client


class ClientForm(ModelForm):
    """ Form which is used to add/edit some client"""

    class Meta:
        model = Client
        
        fields = [
            'name', 'description', 'ip_address',
            'port'
        ]
 