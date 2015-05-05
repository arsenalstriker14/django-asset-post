from django import forms
from django.forms import ModelForm
from .models import *

import re
from django.forms.widgets import Widget, Select, MultiWidget
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe
from django.forms.models import modelformset_factory


class PrdSearchForm(forms.Form): 
  query = forms.CharField( 
      label='', 
      widget=forms.TextInput(attrs={'size': 32}) 
  ) 
class RecordSearchForm(forms.Form): 
  query = forms.CharField( 
      label='', 
      widget=forms.TextInput(attrs={'size': 32}) 
  ) 
        
class PostSearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'size': 32})
    ) 

class PrdInboxForm(ModelForm):
  class Meta: 
    model = InboxEntry
#   fields = ['job_number', 'cell_number', 'job_name', 'request', 'date_in', 'date_due', 'basecamp_link', 'note', 'assigned_by', 'box', 'assigned_to', 'assigned_team', 'status', 'completed_on', 'accepted_by']
    fields = '__all__'


  def __init__(self, *args, **kwargs):
    super(PrdInboxForm, self).__init__(*args, **kwargs)
    self.fields['date_due'].widget = forms.TextInput(attrs={'class': 'form-control', 'data-format': 'YYYY-MM-DD HH:mm:ss', 'pickSeconds': False})
    self.fields['completed_on'].widget = forms.TextInput(attrs={'class': 'form-control', 'data-format': 'YYYY-MM-DD HH:mm:ss', 'pickSeconds': False})

class PostEntryForm(ModelForm):
    class Meta: 
        model = PostEntry
        fields = '__all__'
        
class PostPageForm(ModelForm):
    class Meta: 
        model = PostPage
        fields = '__all__'
            


class PostSearchForm(forms.Form): 
  query = forms.CharField( 
      label='', 
      widget=forms.TextInput(attrs={'size': 32}) 
  ) 

class PostEntryForm(ModelForm):
    class Meta: 
        model = PostEntry
        fields = '__all__'