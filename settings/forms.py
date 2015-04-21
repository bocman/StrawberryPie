from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from models import Client


class ClientForm(ModelForm):

    """ Form which is used to add/edit some client"""

    class Meta:
        model = Client
        fields = [
            'name', 'description', 'ip_address',
            'port', 'group'
        ]

class AlarmForm(forms.Form):
    """
    TODO
    """
    notes = forms.CharField(
        max_length=50,
        label='Notes',
        help_text='Short notes about this alarm'
        )
    alarm_volume = forms.IntegerField(
        label='Volume of the alarm',
        initial=100,
        max_value=100,
        min_value=0,
        help_text='Volume of the alarm melody'
        )

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

    password = forms.CharField(max_length=50)      













