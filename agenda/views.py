# -*- coding: utf-8 -*-

from django.views.generic import ListView
from schedule.models import Event

class MainPage(ListView):

    model = Event
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['delayed'] = Event.objects.filter(status=Event.DELAYED)
        context['nexts'] = Event.objects.filter(
            status__in=(Event.CONFIRMED, Event.NOT_CONFIRMED)
            ).order_by('datetime')
        context['concludeds'] = Event.objects.filter(
            status=Event.CONCLUDED).order_by('-datetime')[:10]
        return context

home = MainPage.as_view()