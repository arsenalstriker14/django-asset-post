from django.conf.urls import include, url
from .views import display_prdInboxEntry, edit_prdInboxEntry, delete_prdInboxEntry

urlpatterns = [
    url(r'^display/(?P<id>\w+)/', display_prdInboxEntry, name='display_inboxentry'),
    url(r'^edit/(?P<id>\w+)/(?P<userid>\w+)/', edit_prdInboxEntry, name='edit_inboxentry'),
    url(r'^delete/(?P<id>\w+)/(?P<userid>\w+)/', delete_prdInboxEntry, name='delete_inboxentry'),
]

