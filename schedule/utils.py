# -*- coding: utf-8 -*-

from .models import Event


def request_filter_factory(filter_string):
    """
    Getting the default code from event types by natural string
    """
    default = {
        'next': (Event.NOT_CONFIRMED, Event.CONFIRMED,),
        'delayed': (Event.DELAYED,),
        'cancelled': (Event.CANCELLED,),
        'done': (Event.CONCLUDED)
        }
    try:
        return default[filter_string]
    except (AttributeError, KeyError):
        # handling none type and key error. Not a problem
        return tuple()
