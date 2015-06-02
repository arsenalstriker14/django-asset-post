from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from .models import *
from .forms import *
from django.db.models import Q
from assetpost.models import UserProfile 
from django.db.models.fields.related import ManyToManyField

def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
        else:
            data[f.name] = f.value_from_object(instance)
    return data




def display_prdInboxEntry(request, id):
    if request.method == 'POST':
        form = PrdInboxForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('taskmanager/display/'+ id +'/')
        else:
            form = PrdInboxForm(request.POST)
            return HttpResponseRedirect('taskmanager/display/'+ id +'/')
            
    else:
        form = PrdInboxForm()
        user = request.user
        u = UserProfile.objects.get(pk=id)
        boxrecords = TaskBox.objects.all()
        boxes = TaskBox.objects.all().count()
        boxdict = {}
        for x in range(1, boxes + 1):
            boxdict['box{0}s'.format(x)] = InboxEntry.objects.filter(box='{0}'.format(x))

        assignedrecords = InboxEntry.objects.filter(assigned_by=u)
        records = InboxEntry.objects.filter(assigned_to=u).order_by('status')
        returndict = {'form': form, 'assignedrecords': assignedrecords, 'records': records, 'boxrecords': boxrecords, 'user': user}
        z = returndict.copy()
        z.update(boxdict)
        return render_to_response('taskmanager/taskmanager_view.html', z, context_instance=RequestContext(request))


def delete_prdInboxEntry(request, id, userid):
    if request.method == 'POST':
        a=InboxEntry.objects.get(pk=id)
        form = PrdInboxForm(request.POST, instance=a)
        if form.is_valid():
            form.delete()
            return HttpResponseRedirect('/taskmanager/display/'+ userid +'/')
    else:
        a=InboxEntry.objects.get(pk=id)
        form = PrdInboxForm(instance=a)
        user = request.user
        u = UserProfile.objects.get(pk=userid)
        boxrecords = TaskBox.objects.all()
        boxes = TaskBox.objects.all().count()
        boxdict = {}
        for x in range(1, boxes + 1):
            boxdict['box{0}s'.format(x)] = InboxEntry.objects.filter(box='{0}'.format(x))

        assignedrecords = InboxEntry.objects.filter(assigned_by=u)
        records = InboxEntry.objects.filter(assigned_to=u).order_by('status')
        returndict = {'form': form, 'assignedrecords': assignedrecords, 'records': records, 'boxrecords': boxrecords, 'user': user}
        z = returndict.copy()
        z.update(boxdict)
        return render_to_response('taskmanager/taskmanager_view.html', z, context_instance=RequestContext(request))




def edit_prdInboxEntry(request, id, userid):
    if request.method == 'POST':
        a=InboxEntry.objects.get(pk=id)
        form = PrdInboxForm(request.POST, instance=a)
        if request.POST.get('delete'):
            a.delete()
            return HttpResponseRedirect('/taskmanager/display/'+ userid +'/')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/taskmanager/display/'+ userid +'/')
    else:
        a=InboxEntry.objects.get(pk=id)
        form = PrdInboxForm(instance=a)
        user = request.user
        u = UserProfile.objects.get(pk=userid)
        boxrecords = TaskBox.objects.all()
        boxes = TaskBox.objects.all().count()
        boxdict = {}
        for x in range(1, boxes + 1):
            boxdict['box{0}s'.format(x)] = InboxEntry.objects.filter(box='{0}'.format(x))

        assignedrecords = InboxEntry.objects.filter(assigned_by=u)
        records = InboxEntry.objects.filter(assigned_to=u).order_by('status')
        returndict = {'form': form, 'assignedrecords': assignedrecords, 'records': records, 'boxrecords': boxrecords, 'user': user}
        z = returndict.copy()
        z.update(boxdict)
        return render_to_response('taskmanager/taskmanager_view.html', z, context_instance=RequestContext(request))


