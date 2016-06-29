# -*- coding utf-8 *-*

from schedule.models import Event
import datetime


def update_events_task(user):
    # update all pending events to delayed
    now = datetime.datetime.now()
    print(now)
    (Event.objects
                  .filter(
                      datetime__lte=now,
                      creation_user=user
                  )
                  .exclude(status__in=(
                                       Event.CANCELLED,
                                       Event.CONCLUDED,
                                       Event.DELAYED
                                       ))
                  .update(status=Event.DELAYED))

