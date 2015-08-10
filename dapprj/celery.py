from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dap.settings')

from django.conf import settings

app = Celery('dapprj', backend='amqp', broker='amqp://guest@localhost//')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task
def convertbin(num):
    if num < 0:
        isNeg = True
        num = abs(num)
    else:
        isNeg = False
    result = ""
    if num == 0:
        result = "0"
    while num > 0:
        result = str(num%2) + result
        num = num/2
    if isNeg == True:
        result = "-" + result
    return result

@app.task
def add(x, y):
    return x + y