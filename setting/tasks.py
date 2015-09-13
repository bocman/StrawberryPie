from datetime import datetime

from celery import task
from project._celery import app
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .models import Event, EventActivationElements, Modul, Client
#from views import activate_modul
from core.utils import activation as activate


import logging
log = logging.getLogger(__name__)
logger = get_task_logger(__name__)


@task(bind=True)
def handle_event(self):
    logger.info(self.request.id)
    try:
        event = Event.objects.get(start_task_id=self.request.id)
    except:
        try:
            event = Event.objects.get(end_task_id=self.request.id)
        except:
            event = None
    if event:
        activations = EventActivationElements.objects.filter(event=event)
        for activation in activations:
            if activation.modul_id:
                client = Client.objects.get(id=1)
                if not event.is_active:
                    logger.info("READY to ACTIVATE modul")
                    logger.info("MODUL ID is "+ str(activation.modul_id))
                    activate(
                        status=True,
                        client_id=client.id,
                        pin_number=activation.modul_id
                        )
                    event.is_active = True
                else:
                    logger.info("READY to DEACTIVATE modul")
                    activate(
                        status=False,
                        client_id=client.id,
                        pin_number=activation.modul_id
                        )
                    event.is_active = False

            if activation.group:
                if not event.is_active:
                    logger.info("READY to ACTIVATE group")
                else:
                    logger.info("READY to DEACTIVATE group")
    else:
        logger.info("Event does not exist with this arguments")

    event.save()
# A periodic task that will run every minute (the symbol "*" means every)
#@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
@task()
def example():
    logger.info("BOSTJAN NOVAK zacetek")
    now = datetime.now()
    logger.info("BOSTJAN END")
    log.info("sem logiral BOSTJAN")