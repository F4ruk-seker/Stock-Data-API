# myproject/celery.py
from __future__ import absolute_import, unicode_literals
from config.settings.base import env
from celery import Celery
from asset.tasks import regular_asset_data_acquisition, regular_public_asset_data_acquisition


env('DJANGO_SETTINGS_MODULE')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    return 2+5

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # 10 saniyede bir çalışacak bir görev örneği
#     sender.add_periodic_task(60.0, regular_asset_data_acquisition.s(), name='regular_asset_data_acquisition - Her 10 saniyede bir')


# from celery.schedules import crontab
#
# CELERY_BEAT_SCHEDULE = {
#     'yaz_hello_world_her_10_dakikada_bir': {
#         'task': 'asset.tasks.yaz_hello_world',
#         # 'schedule': crontab(minute='*/10', hour='7-18', day_of_week='1-5'),  # Her 10 dakikada, hafta içi (Pzt-Cuma), 08:00-18:30
#         'schedule': crontab(minute='*/1', hour='7-18', day_of_week='1-5'),  # Her 10 dakikada, hafta içi (Pzt-Cuma), 08:00-18:30
#     },
# }
#
# CELERY_TIMEZONE = 'Europe/Istanbul'

#
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # 10 saniyede bir çalışacak bir görev örneği
#     sender.add_periodic_task(60.0, regular_asset_data_acquisition.s(),
#                              name='regular_asset_data_acquisition - Her 10 saniyede bir')
#     #
#     # # 10 saniyede bir çalışacak bir görev örneği
#     # sender.add_periodic_task(10.0, regular_public_asset_data_acquisition.s(),
#     #                          name='regular_asset_data_acquisition - Her 10 saniyede bir')
#
