from django import forms
from django.forms import ModelForm
from .models import *

import re
from django.forms.widgets import Widget, Select, MultiWidget
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe
from django.forms.models import modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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
        
class xPageForm(ModelForm):
    class Meta: 
        model = PostPage
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-pageForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'main'

        self.helper.add_input(Submit('submit', 'Submit'))






class PageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

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