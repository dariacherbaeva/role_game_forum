from django.db import models

from foundation.models import SiteUser


class Subscription(models.Model):
    subscriptor = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='who')
    subscriber = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='to_who')

    class Meta:
        unique_together = (('subscriptor', 'subscriber'),)

    def __str__(self):
        return self.subscriptor.username + ' ' + self.subscriber.username
