from django import forms
from .models import RSVP

class RSVPForm(forms.ModelForm):
    name = forms.CharField(help_text='Your Name*')
    email = forms.CharField(help_text='Your Email*')
    number = forms.IntegerField(min_value=0, max_value=20, help_text='Number of Guests*')
    message = forms.CharField(help_text='Message', widget=forms.Textarea, required=False)
    attending = forms.ChoiceField(choices=(('Both', 'Attending Ceremony and Reception'), ('Ceremony', 'Attending Ceremony Only'), ('None', 'Regretfully Decline')))

    class Meta:
        model = RSVP
        fields = ('name', 'email', 'number', 'message', 'attending')
