from django.db import models

import json


class Kino(models.Model):
    """
        Save results of kinlo lottery
    """
    draw = models.IntegerField(null=False)
    result = models.CharField(max_length=200)

    def __str__(self) -> str:
        return super().__str__()
