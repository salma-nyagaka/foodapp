from django.db import models

from ..models import BaseModel


class Menu(BaseModel):

    name = models.CharField(db_index=True, max_length=255, unique=True)
    price = models.IntegerField(default=0)
    # avatar = models.CharField(db_index=True, max_length=255, unique=True)
    description = models.CharField(db_index=True, max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    @property
    def category_name(self):
        return self.name