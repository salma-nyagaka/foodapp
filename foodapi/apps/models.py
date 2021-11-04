from django.db import models


class BaseModel(models.Model):
    """
    The common field in all the models are defined here
    """
    # Add fields with attributes to our database
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)


    class Meta:
        abstract = True
