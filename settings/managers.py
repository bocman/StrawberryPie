from django.db import models


class ActiveClientsManager(models.Manager):

    """
    This manager is in use to get all Clients which have status set to 
    none deleted
    """

    def get_queryset(self):
        return super(ActiveClientsManager, self).get_queryset().filter(deleted=False)


class EnabledClientsManager(models.Manager):

    """
    This manager is in use to get all Clients which have status set to 
    none disabled
    """

    def get_queryset(self):
        return super(ActiveClientsManager, self).get_queryset().filter(disabled=False)
