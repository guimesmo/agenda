# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt

from schedule.models import Event
from schedule.forms import EventForm


class MainPage(FormView):

    form_class = EventForm
    template_name = "base.html"
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super(MainPage, self).get_form_kwargs()
        kwargs['creation_user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(MainPage, self).form_valid(form)


def json_response(qs):
    fields = ('id', 'name', 'datetime_repr', 'comment', 'status')
    objects_list = []
    for obj in qs:
        obj_dict = dict()
        for field in fields:
            obj_dict[field] = getattr(obj, field)
        objects_list.append(obj_dict)

    return HttpResponse(json.dumps(objects_list))


def delayed_events(request):
    events = Event.objects.filter(status=Event.DELAYED)
    return json_response(events)


def next_events(request):
    events = Event.objects.filter(status__in=(Event.CONFIRMED, Event.NOT_CONFIRMED))
    return json_response(events)


def done_events(request):
    events = Event.objects.filter(status=Event.CONCLUDED).order_by('-datetime')[:100]
    return json_response(events)


@csrf_exempt
def event(request):
    data = json.loads(request.body.decode('utf-8'))

    form = EventForm(data, creation_user=request.user)
    if not form.is_valid():
        json_response(form.errors, status_code=400)
    form.save()
    return HttpResponse(form.instance.pk)



@csrf_exempt
def finish_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    data = json.loads(request.body.decode('utf-8'))
    event.status = data.get('status', event.status)
    event.save()
    return HttpResponse(event.pk)


home = MainPage.as_view()