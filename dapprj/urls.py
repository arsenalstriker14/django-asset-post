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
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from assetpost.views import *
from filebrowser.sites import site

if settings.DEBUG:
    import debug_toolbar


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', login_user, name ='login_user'),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^main/', postsearch),
    url(r'^logout/$', logout_page),
    url(r'^filebrowser/', file_browser),
    url(r'^assetpost/', include('assetpost.urls', namespace='assetpost', app_name='assetpost')),
    url(r'^upload/', file_upload),
    url(r'^quickpost/(?P<job_number>[A-Z0-9-]+)/', quickpost, name="quickpost"),
    url(r'^taskmanager/', include('taskmanager.urls', namespace="taskmanager")),
#    url(r'^delete-item/(?P<id>\w+)/(?P<userid>\w+)/', delete_prdInboxEntry),
    url(r'^specdisplay/(?P<job_number>[A-Z0-9-]+)/', display_record, name="display_record"),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += (
   url(r'^__debug__/', include(debug_toolbar.urls)),
)
