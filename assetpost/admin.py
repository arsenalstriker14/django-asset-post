#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by krc.nyc on 2009-05-15.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import ChoicesFieldListFilter


class PostPageAdmin(admin.ModelAdmin):
    list_display = ('client', 'job_number', 'job_name', 'create_date')
    list_filter = (
        ('client', ChoicesFieldListFilter),
    )
    
def visible(modeladmin, request, queryset):
    queryset.update(visibility="visible")
visible.short_description = "Mark selected entries as visible"

def hidden(modeladmin, request, queryset):
    queryset.update(visibility="hidden")
hidden.short_description = "Mark selected entries as hidden"

class PostEntryAdmin(admin.ModelAdmin):
    exclude = ('add_misc', 'add_misc2', 'add_mobile_view', 'add_pdf', 'add_html', 'add_report', 'add_text', 'add_zip')
    fieldsets = (
        (None, {
            'fields': ('visibility', 'client', 'job_number', 'cell_number', 'post_title', 'date', 'post_type', 'post_round', 'docfile', 'url_link')
        }),
        ('Link Options', {
            'classes': ('collapse',),
            'fields': ( 'misc_link', 'link_misc', 'misc_link2', 'link_misc2', 'mobile_view_url', 'link_pdf', 
                    'link_html', 'link_report', 'link_text', 'link_zip' )
        }),
    )
    list_display = ('client', 'job_number', 'cell_number', 'post_type','post_round', 'post_title', 'date', 'visibility')
    list_filter = (
        ('client', ChoicesFieldListFilter),
    )
    search_fields = ['job_number']
    list_per_page = 35
    actions = [visible, hidden]

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
        
admin.site.register(Employee)
admin.site.register(UserProfile)
admin.site.register(FreelanceProfile)
admin.site.register(InboxEntry, InboxEntryAdmin)
admin.site.register(ProjectTeam)
admin.site.register(PostPage, PostPageAdmin)
admin.site.register(JobContact)
admin.site.register(ClientList)
admin.site.register(PostEntry, PostEntryAdmin)
admin.site.register(AccountGroup)
admin.site.register(TaskEntry)



def main():
    pass


if __name__ == '__main__':
    main()

