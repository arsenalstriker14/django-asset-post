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
    


class PostEntryAdmin(admin.ModelAdmin):
    exclude = ()
    fieldsets = (
        (None, {
            'fields': ( 'client', 'job_number', 'cell_number', 'post_title', 'date', 'post_type', 'post_round', 'preview_file', 'url_link')
        }),
        ('Link Options', {
            'classes': ('collapse',),
            'fields': ( 'link_pdf', 
                    'link_html', 'link_report', 'link_text', 'link_zip' )
        }),
    )
    list_display = ('client', 'job_number', 'cell_number', 'post_type','post_round', 'post_title', 'date')
    list_filter = (
        ('client', ChoicesFieldListFilter),
    )
    search_fields = ['job_number']
    list_per_page = 35





admin.autodiscover()
        
admin.site.register(Employee)
admin.site.register(UserProfile)
admin.site.register(FreelanceProfile)
admin.site.register(ProjectTeam)
admin.site.register(PostPage, PostPageAdmin)
admin.site.register(JobContact)
admin.site.register(ClientList)
admin.site.register(PostEntry, PostEntryAdmin)
admin.site.register(AccountGroup)
#admin.site.register(TaskEntry)



def main():
    pass


if __name__ == '__main__':
    main()

