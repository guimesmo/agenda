from django import forms
from schedule.models import Event

class EventForm(forms.ModelForm):
    
    def __init__(self, *args, **kwrags):
        self.creation_user = kwargs.pop('creation_user')
        super(EventForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Event
        fields = ('name', 'datetime', 'comments', 'status')
        
    def save(self):
        self.instance = super(EventForm, self).save(commit=False)
        if not self.instance.creation_user:
            self.instance.creation_user = self.creation_user
        self.instance.save()
        return self.instance
        