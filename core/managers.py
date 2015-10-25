from django.db import models


class ActiveClientsManager(models.Manager):

    def get_queryset(self):
        """
        Method return all Clients which have status set to 
        none deleted
        """
        return super(ActiveClientsManager, self).get_queryset().filter(deleted=False)


class EnabledClientsManager(models.Manager):

    def get_queryset(self):
        """
        Method return all Clients which have status set to 
        none disabled
        """
        return super(EnabledClientsManager, self).get_queryset().filter(disabled=False)


class OnlineClientsManager(models.Manager):

    def get_queryset(self):
        """
        Method return all Clients, which are currently 
        connected (marked as online)
        """
        return [x for x in super(OnlineClientsManager, self).get_queryset() if x.is_connected()]

    def count(self):
        return len(self.get_queryset())

class ActiveModulsManager(models.Manager):

    def get_queryset(self):
        """
        Method return all Moduls which have status set to 
        none deleted
        """
        return super(ActiveModulsManager, self).get_queryset().filter(is_deleted=False)
