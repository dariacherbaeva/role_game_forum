import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'role_game_forum.settings')

app = Celery('role_game_forum')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
