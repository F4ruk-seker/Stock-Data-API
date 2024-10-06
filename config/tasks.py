from celery import shared_task
from datetime import datetime
import logging

logger = logging.getLogger(__name__)



@shared_task
def add(x, y):
    raise x + y
