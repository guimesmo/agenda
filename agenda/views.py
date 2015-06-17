# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from schedule.models import Event
from django.contrib.auth.decorators import login_required
from schedule.forms import EventForm

class MainPage(FormView):

    form_class = EventForm
    template_name = "base.html"
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super(MainPage, self).get_form_kwargs()
        kwargs['creation_user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['delayed'] = Event.objects.filter(status=Event.DELAYED)
        context['nexts'] = Event.objects.filter(
            status__in=(Event.CONFIRMED, Event.NOT_CONFIRMED)
            ).order_by('datetime')
        context['concludeds'] = Event.objects.filter(
            status=Event.CONCLUDED).order_by('-datetime')[:10]
        return context

    def form_valid(self, form):
        form.save()
        return super(MainPage, self).form_valid(form)

home = MainPage.as_view()