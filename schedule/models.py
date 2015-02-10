# -*- coding utf-8 -*-

from django.db import models


class Event(models.Model):
    """Evento com nome, dia, horario e comentario"""
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        ordering = ("datetime", "name",)

    def __unicode__(self):
        return self.name
