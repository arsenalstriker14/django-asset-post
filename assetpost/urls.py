from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from .views import PostEntryUpdate, PageCreate, updatePage, createEntry, updateEntry, multipost, multipost_init, DefaultsMixin, EntryViewSet

router = DefaultRouter()
router.register(r'entries', EntryViewSet)


urlpatterns = patterns('',
#    url(r'^newpostentry/', PostEntryCreate.as_view(), name='post_entry'),
    url(r'^newpostpage/', PageCreate.as_view(), name='postpage'),
    url(r'^updatepostentry/(?P<pk>\w+)/$', PostEntryUpdate.as_view(), name='update_entry'),
    url(r'^updatepage/(?P<id>\w+)/$', updatePage, name='updatePage'),
    url(r'^create-entry/', createEntry, name='createEntry'),
    url(r'^update-entry/(?P<id>\w+)/$', updateEntry, name='updateEntry'),
    url(r'^multipost/', multipost, name='multipost'),
    url(r'^multipost-init/(?P<client>\w+)/(?P<id>\w+)/$', multipost_init, name='multipost-initial'),

)

