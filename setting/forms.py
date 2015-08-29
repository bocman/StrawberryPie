from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from models import ElementGroup, Client, Modul, Event


class ElementForm(ModelForm):
    """
    Form which is used to create/edit informations
    about group which hold
    """

    class Meta:
        model = ElementGroup
        fields = [
            'name', 'description'
        ]


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
            'port', 'key'
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













