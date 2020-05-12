from django.utils import timezone

from chat.models import Message
from foundation.models import SiteUser
from role_game_forum.celery import app


@app.task(name='message')
def send_message():
    for u in SiteUser.objects.exclude(id=1):
        Message.objects.create(text='Доброе утро! Новый день в нашей ролевой игре!', to_who_id=u.id, from_who_id=1,
                               when=timezone.now())
