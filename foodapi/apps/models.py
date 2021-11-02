from django.db import models

from ..helpers.push_id import PushID


class BaseModel(models.Model):
    """
    The common field in all the models are defined here
    """
    # Add fields with attributes to our database
    id = models.CharField(db_index=True, max_length=255,
                          unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        push_id = PushID()
        # This to check if it creates a new or updates an old instance
        if not self.id:
            self.id = push_id.next_id()
        super(BaseModel, self).save()

    class Meta:
        abstract = True
