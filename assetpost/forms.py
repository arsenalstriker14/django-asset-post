from django import forms
from multiupload.fields import MultiFileField
from django.forms import ModelForm
from .models import *

import re
from django.forms.widgets import Widget, Select, MultiWidget
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe
from django.forms.models import modelformset_factory, BaseInlineFormSet, inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field  


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
        
class PostsearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'size': 32})
    ) 
    def __init__(self, data=None, files=None, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'PostsearchForm'
        self.helper.form_method = 'get'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Field('query', placeholder=kwargs.pop('query_placeholder', 'enter client name or job number')),
        )
        super(PostsearchForm, self).__init__(data, files, **kwargs)

class PostEntryForm(forms.ModelForm):
    class Meta: 
        model = PostEntry
        fields = [ 'client', 'job_number', 'cell_number', 'post_title', 'date', 'post_type', 'post_round', 'preview_file', 'url_link', 'link_pdf', 'link_html', 'link_report', 'link_text', 'link_zip']




# class MultiEntryForm(ModelForm):
#     class Meta: 
#         model = PostEntry
#         fields = [ 'client', 'job_number', 'cell_number', 'post_title', 'date', 'post_type', 'post_round', 'preview_file', 'url_link', 'link_pdf', 'link_html', 'link_report', 'link_text', 'link_zip']

# class BaseFormSet(BaseInlineFormSet):
#     def add_fields(self, form, index):
#         super(BasePlanItemFormSet, self).add_fields(form, index)
#         # add fields to the form
#         fields = [ 'client', 'job_number', 'cell_number', 'post_title', 'date', 'post_type', 'post_round', 'preview_file', 'url_link', 'link_pdf', 'link_html', 'link_report', 'link_text', 'link_zip']
    
#     def save_new(self, form, commit=True):
#         # custom save behavior for new objects, form is a ModelForm
#         return super(BaseFormSet, self).save_new(form, commit=commit)
 
#     def save_existing(self, form, instance, commit=True):
#         # custom save behavior for existing objects
#         # instance is the existing object, and form has the updated data
#         return super(BaseFormSet, self).save_existing(form, instance, commit=commit)

# FormSet = inlineformset_factory(PostEntry, formset=BaseFormSet)



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

