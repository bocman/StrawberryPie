from datetime import datetime

from celery import task
from project._celery import app
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .models import Event, EventActivationElements
#from views import activate_modul



import logging
log = logging.getLogger(__name__)
logger = get_task_logger(__name__)


@task(bind=True)
def schedule_event(self):
    event = Event.objects.get(task_id=self.request.id)
    #log.info(
     #   "Started AUTOMATIC EVENT with id{0}".format(event.id)
      #  )
    activations = EventActivationElements.objects.filter(event=event)

    logger.info("--------------------")



# A periodic task that will run every minute (the symbol "*" means every)
#@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
@task()
def example():
    logger.info("BOSTJAN NOVAK zacetek")
    now = datetime.now()
    logger.info("BOSTJAN END")
    log.info("sem logiral BOSTJAN")