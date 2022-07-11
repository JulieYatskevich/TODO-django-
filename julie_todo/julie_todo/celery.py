import os

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'julie_todo.settings')

app = Celery('julie_todo')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
