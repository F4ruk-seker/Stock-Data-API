import subprocess


def celery_runner(c):
    subprocess.run(c.split(' '))
