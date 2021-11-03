from django.db import models

from ..models import BaseModel
from ..authentication.models import User
from ..menu.models import Menu


class Order(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Menu, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, blank=True, null=True)
