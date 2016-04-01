from django.forms import ModelForm, PasswordInput
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

import logging

from models import Group, Client, Modul, Event

log = logging.getLogger(__name__)


class ModulForm(ModelForm):
    """
    Form which is used to work with Modul informations
    """

    class Meta:
        model = Modul
        fields = [
            'name', 'description', 'is_general',
            'pin_number', 'is_input', 'client',
            'is_activated'
        ]


class ClientForm(ModelForm):
    """
    Form which is used to add/edit some client
    """

    class Meta:
        model = Client
        fields = [
            'name', 'description', 'ip_address',
            'port', 'group'
        ]

class GroupForm(ModelForm):
    """
    Form is used to add/edit some Group
    """
    class Meta:
        model = Group
        fields = [
            'name', 'description'
        ]

class EventForm(ModelForm):
    """
    TODO
    """
    class Meta:
        model = Event
        fields = [
            'name', 'start_time',
            'is_periodically', 'end_time'
        ]


class UserForm(ModelForm):
    """
    Form is used to edit/update own user profile, or edit other user
    info
    """
    password = forms.CharField(
        required=False,
        max_length=50,
        widget=PasswordInput
        )
    confirm_password = forms.CharField(
        required=False,
        max_length=50,
        widget=PasswordInput
        )

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email'
        ]
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True

    def clean(self):
        msg = {
            'not_equals': 'Sorry, passwords do not match.',
            'no_password': "Please fill in new password",
            'no_confirm_password': "Please confirm your new password"
        }
        cleaned_data = super(UserForm, self).clean()
        new_password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and not confirm_password:
            self.add_error('password', _(msg['no_confirm_password']))
        if not new_password and confirm_password:
            self.add_error('password', _(msg['no_password']))
        if new_password != confirm_password:
            self.add_error('password', _(msg['not_equals']))

