from django import forms
from django.forms import ModelForm
from .models import InboxEntry
from bootstrap3_datetime.widgets import DateTimePicker
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PrdInboxForm(ModelForm):
    class Meta:
        model = InboxEntry
#       fields = ['job_number', 'cell_number', 'job_name', 'request', 'date_in', 'date_due', 'basecamp_link', 'note', 'assigned_by', 'box', 'assigned_to', 'assigned_team', 'status', 'completed_on', 'accepted_by']
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(PrdInboxForm, self).__init__(*args, **kwargs)
            self.fields['date_due'].widget = forms.DateTimeField(required=False, widget=DateTimePicker(options={'class': 'dateinput', "format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
            self.fields['completed_on'].widget = forms.DateTimeField(required=False, widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))

