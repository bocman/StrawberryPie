from django.db import models


class ActiveClientsManager(models.Manager):

    def get_queryset(self):
        return super(ActiveClientsManager, self).get_queryset().filter(deleted=False)


