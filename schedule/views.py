# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Event
from .forms import EventForm
from .tasks import update_events_task


def json_response(qs):
    fields = ('id', 'name', 'datetime_repr', 'comment', 'status')
    objects_list = []
    for obj in qs:
        obj_dict = dict()
        for field in fields:
            obj_dict[field] = getattr(obj, field)
        objects_list.append(obj_dict)

    return HttpResponse(json.dumps(objects_list))

@login_required
def delayed_events(request):
    events = Event.objects.filter(
        status=Event.DELAYED,
        creation_user=request.user
    )
    return json_response(events)


@login_required
def next_events(request):
    events = Event.objects.filter(
        status__in=(Event.CONFIRMED, Event.NOT_CONFIRMED),
        creation_user=request.user
    )
    return json_response(events)


@login_required
def done_events(request):
    events = Event.objects.filter(
        status=Event.CONCLUDED,
        creation_user=request.user
    ).order_by('-datetime')
    return json_response(events)


@login_required
def canceled_evevnts(request):
    events = Event.objects.filter(
        status=Event.CANCELED,
        creation_user=request.user
    ).order_by('-datetime')
    return json_response(events)


@login_required
@csrf_exempt
def event(request):
    data = json.loads(request.body.decode('utf-8'))

    form = EventForm(data, creation_user=request.user)
    if not form.is_valid():
        json_response(form.errors, status_code=400)
    form.save()
    return HttpResponse(form.instance.pk)


@login_required
@csrf_exempt
def finish_event(request, event_id):
    event = get_object_or_404(Event,
        creation_user=request.user,
        pk=event_id)
    data = json.loads(request.body.decode('utf-8'))
    event.status = data.get('status', event.status)
    event.save()
    return HttpResponse(event.pk)


@login_required
def update_events(request):
    update_events_task(request.user)
    return HttpResponse('1')
