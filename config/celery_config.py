# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


import time
import json
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By



# Django ayar dosyanızın konumunu belirtiyoruz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

# Celery uygulaması oluşturuluyor
# app = Celery('config')


app = Celery('config',
             broker='',
             backend='rpc://',
             # include=['tasks']
             )

app.conf.update(
    timezone='UTC',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
)

# Django ayarlarında "CELERY" ile başlayan her şeyi yükler
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Tüm görevleri (tasks) Django uygulamalarından otomatik olarak bulur
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    return 2+5

from celery import shared_task
@shared_task(queue='my_queue')
def debug_task_2():
    print(2+5)

from datetime import datetime
import logging

logger = logging.getLogger(__name__)
# @shared_task


driver = Chrome()

prices: list = []


def get_prices() -> list:
    global driver
    result_div = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[3]/div/div/div[3]/div')
    return [item.text.replace('TL', '') for item in result_div.find_elements(By.CLASS_NAME, 'price')]


def has_other_page():
    pagenation_div = driver.find_element(By.CLASS_NAME, 'pagination')
    last_btn = pagenation_div.find_elements(By.TAG_NAME, 'li')[-1]
    if not last_btn.get_attribute('class') == 'disabled':
        last_btn.click()
        return True
    return False

@shared_task
def uzun_sureli_gorev(*args, **kwargs):
    global prices
    words = 'web analytics izleme'
    url = f'https://bionluk.com/search?term={words}'

    driver.get(url)
    time.sleep(10)

    try:
        while True:
            prices += get_prices()
            if has_other_page():
                time.sleep(5)
            else:
                break
    except Exception as exception:
        print(exception)
    finally:
        print(prices)
        with open(f'data/{words.replace(' ', '')}.json', 'w+', encoding='utf-8') as df:
            df.write(json.dumps(prices))
