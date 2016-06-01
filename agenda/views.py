# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.views.generic.edit import FormView

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
    fields = ('name', 'datetime_repr', 'comment', 'status')
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


home = MainPage.as_view()