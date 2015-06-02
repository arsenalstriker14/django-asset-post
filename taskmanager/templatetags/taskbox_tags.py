from django import template

register = template.Library()


def distribute_entrys(inboxentry):
    boxentrys = inboxentry.box_set.all()
    return {'boxentrys': boxentrys}
