from django.conf.urls import patterns, url
from .views import PostEntryUpdate, PageCreate, PageUpdate, createEntry, updateEntry, multipost, multipost_init

urlpatterns = patterns('',
#    url(r'^newpostentry/', PostEntryCreate.as_view(), name='post_entry'),
    url(r'^newpostpage/', PageCreate.as_view(), name='postpage'),
    url(r'^updatepostentry/(?P<pk>\w+)/$', PostEntryUpdate.as_view(), name='update_entry'),
    url(r'^updatepage/(?P<pk>\w+)/$', PageUpdate.as_view(), name='update_page'),
    url(r'^create-entry/', createEntry, name='createEntry'),
    url(r'^update-entry/(?P<id>\w+)/$', updateEntry, name='updateEntry'),
    url(r'^multipost/', multipost, name='multipost'),
    url(r'^multipost-init/(?P<client>\w+)/(?P<id>\w+)/$', multipost_init, name='multipost-initial'),

)

