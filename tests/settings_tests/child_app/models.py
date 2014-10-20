from django.db import models

from ..parent_app.models import Parent


class Bastard(models.Model):
    parent = models.ForeignKey(Parent)
