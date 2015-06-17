from django import forms
from schedule.models import Event

class EventForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.creation_user = kwargs.pop('creation_user')
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['status'].required = False
    
    class Meta:
        model = Event
        fields = ('name', 'datetime', 'comment', 'status')
        
    def save(self):
        self.instance = super(EventForm, self).save(commit=False)
        if not self.instance.id:
            self.instance.creation_user = self.creation_user
        self.instance.save()
        return self.instance
        