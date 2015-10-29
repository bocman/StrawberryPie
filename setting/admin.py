from django.contrib import admin

# Register your models here.
from .models import Client, Event, EventActivationElements

admin.site.register(Client)
admin.site.register(Event)
admin.site.register(EventActivationElements)
