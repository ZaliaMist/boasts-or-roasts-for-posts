from django.db import models
from django.utils import timezone

class ModelForBoastsAndRoasts(models.Model):
    body = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    vote_holder = models.IntegerField(default=0)
    ROAST_OR_BOAST = ((True, 'Boast'), (False, 'Roast'))
    boast = models.BooleanField(
        choices=ROAST_OR_BOAST, default=True
    )

    def __str__(self):
        return self.body
