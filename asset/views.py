from django.shortcuts import HttpResponse
# from .tasks import uzun_sureli_gorev
from config.celery_config import debug_task, uzun_sureli_gorev, debug_task_2


def task_test(request):
    # debug_task()
    debug_task() # çalışıyor
    debug_task_2.delay() # çalışmıyor
    # uzun_sureli_gorev() # çalışıyor ama bekleniyor
    # uzun_sureli_gorev.apply_async(countdown=0)  # çalışmıyor ama celery received
    # uzun_sureli_gorev.apply_async(queue='long_tasks')  # çalışmıyor ama celery received
    r = [
        uzun_sureli_gorev.delay(),
        # uzun_sureli_gorev.delay_async(),
        # uzun_sureli_gorev.apply(),
        # uzun_sureli_gorev.apply_async((4, 6), countdown=1)
    ]
    for _ in r:
        print(_)
        print(_.id)
        print(_.status)
        print(_.result)  # Görevin sonucunu gör
    return HttpResponse(f'ok -> {'result'}')

