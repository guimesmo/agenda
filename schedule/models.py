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

    creation_user = models.ForeignKey('auth.User')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_edition = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(
        choices=STATUS_CHOICES,
        default=NOT_CONFIRMED)

    class Meta:
        ordering = ("datetime", "name",)

    def __unicode__(self):
        return self.name

    @property
    def datetime_repr(self):
        return self.datetime.isoformat()

    def css_class_by_status(self):
        STATUS_CHOICE = {
            self.NOT_CONFIRMED: "",
            self.CONFIRMED: "active",
            self.DELAYED: "danger",
            self.CANCELLED: "warning",
            self.CONCLUDED: "active",
        }
        return STATUS_CHOICE[self.status]


CASH = 100
DEBIT_CARD = 101
CREDIT_CARD = 102
CHECK = 103

PAYMENT_METHODS = (
    (CASH, "Dinheiro"),
    (DEBIT_CARD, "Cartão de débito"),
    (CREDIT_CARD, "Cartão de crédito"),
    (CHECK, "Cheque")
)


class Payment(models.Model):
    event = models.ForeignKey(Event)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.PositiveIntegerField(choices=PAYMENT_METHODS)
    additional_comments = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
