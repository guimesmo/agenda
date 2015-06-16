# -*- coding utf-8 *-*

from schedule.models import Event
import datetime

def update_events():
    # update all pending events to delayed
    now = datetime.datetime.now()
    (Event.objects
                  .filter(datetime__lte=now)
                  .exclude(status__in=(
                                       Event.CANCELLED,
                                       Event.CONCLUDED,
                                       Event.DELAYED
                                       ))).update(status=Event.DELAYED)
        
