import sys
import os
from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _

# Register your models here.

def released(modeladmin, request, queryset):
    queryset.update(status='Released')
released.short_description = "Mark selected projects as Released"

def in_progress(modeladmin, request, queryset):
    queryset.update(status='In Progress')
in_progress.short_description = "Mark selected projects as In Progress"

def posted(modeladmin, request, queryset):
    queryset.update(status='Posted')
posted.short_description = "Mark selected projects as Posted"

def completed(modeladmin, request, queryset):
    queryset.update(status='Completed')
completed.short_description = "Mark selected projects as Completed"

def awaiting_action(modeladmin, request, queryset):
    queryset.update(status='Awaiting Action')
awaiting_action.short_description = "Mark selected projects as Awaiting Action"

class InboxEntryAdmin(admin.ModelAdmin):
    list_display = ['job_number', 'cell_number', 'job_name', 'basecamp_link', 'note', 'status']
    ordering = ['job_number']
    actions = [released, completed, posted, in_progress, awaiting_action]
    
    def basecamp_link(self,obj):
        return u'<a href="/basecamp_link/%s/">%s</a>' % (obj.basecamp_link,obj)
        domain_link.allow_tags = True
        domain_link.short_description = "foo"
        def __init__(self,*args,**kwargs):
            super(ProductionInboxAdmin, self).__init__(*args, **kwargs)
            self.list_display_links = (None, )


admin.autodiscover()

admin.site.register(InboxEntry, InboxEntryAdmin)
admin.site.register(TaskBox)



def main():
    pass


if __name__ == '__main__':
    main()
