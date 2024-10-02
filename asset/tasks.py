from celery import shared_task
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


@shared_task
def uzun_sureli_gorev(*args, **kwargs):
    print(args)
    print(kwargs)
    import time

    logger.info(f'start on > {datetime.now()} |')
    time.sleep(1)
    with open('task_results.txt', 'a+', encoding='utf-8') as df:
        df.write(f'OK > {datetime.now()} |\n')
    logger.info(f'end  on > {datetime.now()} |')

    return 0


@shared_task
def add(x, y):
    raise x + y
