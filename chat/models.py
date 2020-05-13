from django.db import models

from foundation.models import SiteUser


class Message(models.Model):
    text = models.TextField()
    from_who = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='sender')
    to_who = models.ForeignKey(SiteUser, on_delete=models.CASCADE, related_name='receiver')
    when = models.DateTimeField()

    def __str__(self):
        return 'from: ' + self.from_who.username + ' to: ' + self.to_who.username + ' ' + self.text
