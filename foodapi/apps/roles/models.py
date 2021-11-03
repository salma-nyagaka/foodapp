from django.db import models

from ...helpers.push_id import PushID
from ..models import BaseModel


class Role(BaseModel):
    title = models.CharField(max_length=256,
                             blank=True,
                             default='Normal user')

    def __str__(self):
        return self.title