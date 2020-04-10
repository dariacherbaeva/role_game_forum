from django.db import models

from foundation.models import SiteUser


class Subscription(models.Model):
    subscriptor = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='who')
    subscriber = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='to_who')
