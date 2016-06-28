import datetime
from django import forms
from django.conf import settings
from schedule.models import Event


class EventForm(forms.Form):
    name = forms.CharField()
    date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    time = forms.TimeField()

    def __init__(self, *args, **kwargs):
        self.creation_user = kwargs.pop('creation_user')
        super(EventForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data.get('date') and self.cleaned_data.get('time'):
            self.cleaned_data['event_datetime'] = datetime.datetime.combine(
                self.cleaned_data['date'],
                self.cleaned_data['time']
                )
        return self.cleaned_data

    def save(self):
        self.instance = Event.objects.create(
            creation_user=self.creation_user,
            datetime=self.cleaned_data['event_datetime'],
            name=self.cleaned_data['name']
        )
        return self.instance
