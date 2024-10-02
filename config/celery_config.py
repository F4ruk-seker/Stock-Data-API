# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django ayar dosyanızın konumunu belirtiyoruz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

# Celery uygulaması oluşturuluyor
app = Celery('config')

# Django ayarlarında "CELERY" ile başlayan her şeyi yükler
app.config_from_object('django.conf:settings', namespace='CELERY')

# Tüm görevleri (tasks) Django uygulamalarından otomatik olarak bulur
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


from celery import shared_task
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# @shared_task
# @app.task(bind=True)
@shared_task
def uzun_sureli_gorev(*args, **kwargs):
    print(args)
    print(kwargs)
    import time

    logger.info(f'start on > {datetime.now()} |')
    with open('task_results.txt', 'a+', encoding='utf-8') as df:
        df.write(f'OK > {datetime.now()} |\n')
    logger.info(f'end  on > {datetime.now()} |')

    return 0
