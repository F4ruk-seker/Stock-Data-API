from django.shortcuts import HttpResponse
# from .tasks import uzun_sureli_gorev
from config.celery_config import debug_task


def task_test(request):
    # debug_task()
    debug_task()  # çalışıyor
    # uzun_sureli_gorev() # çalışıyor ama bekleniyor
    # uzun_sureli_gorev.apply_async(countdown=0)  # çalışmıyor ama celery received
    # uzun_sureli_gorev.apply_async(queue='long_tasks')  # çalışmıyor ama celery received

    return HttpResponse(f'ok -> {'result'}')


