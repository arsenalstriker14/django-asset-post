"""dapprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from assetpost.views import *
from filebrowser.sites import site

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', login_user, name ='login_user'),
    #url(r'^$', home, name ='home'),
]
urlpatterns += (
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^main/', postsearch),

    url(r'^logout/$', logout_page),
    url(r'^create/', create_record),
    url(r'^filebrowser/', file_browser),
    url(r'^newpostpage/', create_postpage),
    url(r'^newpostentry/', create_postentry),
    url(r'^editpostentry/(?P<id>\w+)/', edit_postentry),
    url(r'^poststatus/', post_status),
    url(r'^displaypost/(?P<id>\w+)/', display_post),
    url(r'^upload/', file_upload),
    url(r'^userprofile/(?P<id>\w+)/', display_profile),
#    (r'^attachments/', include('attachments.urls')),
    url(r'^quickpost/(?P<job_number>[A-Z0-9-]+)/', quickpost, name="quickpost"),
#    url(r'^branding/(?P<client>[A-Za-z-]+)/', branding, name="branding"),
    url(r'^production-display/(?P<id>\w+)/', display_prdInboxEntry),
    url(r'^edit-inbox/(?P<id>\w+)/(?P<userid>\w+)/', edit_prdInboxEntry),
    url(r'^delete-item/(?P<id>\w+)/(?P<userid>\w+)/', delete_prdInboxEntry),
    url(r'^specdisplay/(?P<job_number>[A-Z0-9-]+)/', display_record, name="display_record"),
)
