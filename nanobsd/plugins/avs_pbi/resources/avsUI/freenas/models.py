from django.db import models


class AVS(models.Model):
    """
    Django model describing every tunable setting for avs
    """

    enable = models.BooleanField(default=False)
