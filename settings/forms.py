from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from models import ClientGroup, Client, Item, Alarm


class GroupForm(ModelForm):

    """ Form which is used to work with ClientGroup informations"""

    class Meta:
        model = ClientGroup
        fields = [
            'name', 'description'
        ]


class ItemForm(ModelForm):

    """ Form which is used to work with Item informations"""

    class Meta:
        model = Item
        fields = [
            'name', 'description', 'is_general',
            'pin_number', 'is_input', 'client',
            'group', 'is_activated'
        ]


class ClientForm(ModelForm):

    """ Form which is used to add/edit some client"""

    class Meta:
        model = Client
        fields = [
            'name', 'description', 'ip_address',
            'port', 'group'
        ]


class AlarmForm(ModelForm):
    """
    TODO
    """
    class Meta:
        model = Alarm
        fields = [
            'note','alarm_volume','notification_time'
        ]

class UserForm(ModelForm):
    """
    Form is used to edit/update own user profile, or edit other user
    info
    """

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email'
        ]

    password = forms.CharField(
        max_length=50
        )
    confirm_password = forms.CharField(
        max_length=50
        )       













