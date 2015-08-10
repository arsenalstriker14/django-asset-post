from celery.registry import tasks
from celery.task import Task
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import EmailMultiAlternatives

class SignUpTask(Task):

    def product(x, y):
        return x * y

tasks.register(SignUpTask)

