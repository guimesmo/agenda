# -*- coding utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _


class Event(models.Model):
    """Evento com nome, dia, horario e comentario"""

    NOT_CONFIRMED = 101
    CONFIRMED = 102
    DELAYED = 103
    CANCELLED = 104
    CONCLUDED = 105

    STATUS_CHOICES = (
        (NOT_CONFIRMED, _("Not Confirmed")),
        (CONFIRMED, _("Confirmed")),
        (DELAYED, _("Delayed")),
        (CANCELLED, _("Cancelled")),
        (CONCLUDED, _("Concluded")),
    )

    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    comment = models.TextField()
    status = models.PositiveIntegerField(choices=STATUS_CHOICES)

    class Meta:
        ordering = ("datetime", "name",)

    def __unicode__(self):
        return self.name

    def css_class_by_status(self):
        STATUS_CHOICE = {
            self.NOT_CONFIRMED: "",
            self.CONFIRMED: "active",
            self.DELAYED: "danger",
            self.CANCELLED: "warning",
            self.CONCLUDED: "active",
        }
        return STATUS_CHOICE[self.status]