"""
This script was written for Pycharm.
Its purpose is to start and run celery services,
when the Django server is run.
f4
"""

import subprocess


def run_celery():
    c = 'celery -A config worker --loglevel=info --concurrency=4 -P threads'
    subprocess.run(c.split(' '))


if __name__ == '__main__':
    run_celery()
