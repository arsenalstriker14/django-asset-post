from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib.auth import logout
from django.template import Context, RequestContext
from django.template.loader import get_template
from .models import * 
from .forms import *
from django import forms
from django.conf import settings
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.db.models import get_model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models import Q
from itertools import chain, islice
import operator
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from datetime import datetime
from django.forms.models import modelformset_factory
from django.forms.models import *
from django.template.response import TemplateResponse

# Create your views here.
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('registration/login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/') 
def home(request):
     return render(request, "index.html", {})

def logout_page(request): 
        logout(request) 
        return HttpResponseRedirect('/')

def display_record(request, job_number):
            records = PostEntry.objects.filter(job_number=job_number)
            precords = PostPage.objects.filter(job_number=job_number).order_by('-create_date')
            cdrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='cd_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
            cerecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='ce_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
            cmrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='cm_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
            mrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='m_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
            frrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='FinalRelease').order_by('-date', '-post_round', 'cell_number', 'post_title')

            if request.user.is_authenticated():
                    tpl = 'display_template.html'
                    return render_to_response(tpl, { 'records': records, 'precords': precords, 'mrecords': mrecords, 'cdrecords': cdrecords, 'cerecords': cerecords, 'cmrecords': cmrecords, 'frrecords': frrecords })
            else:
                    tpl = 'display_template.html'
                    return render_to_response(tpl, { 'records': records, 'precords': precords, 'mrecords': mrecords, 'cdrecords': cdrecords, 'cerecords': cerecords, 'cmrecords': cmrecords, 'frrecords': frrecords })




def file_upload(request):
                return render_to_response('upload.html')







@csrf_protect
def create_record(request):
        if request.method == 'POST': # If the form has been submitted...
            form = PostRequestForm(request.POST) # A form bound to the POST data
            if form.is_valid():  #All validation rules pass
                        # Process the data in form.cleaned_data
                form.save()
                return HttpResponseRedirect('/create/')
        else:
            form = PostRequestForm()
        return render(request, 'createpostrequest.html', {
            'form': form,
    })

def create_postpage(request):
    tpl = "createpostpage.html"
    user = request.user
    variables = RequestContext(request, { 'user': user }) 
    return TemplateResponse(request, tpl, {'form': PageForm()})


def create_postentry(request):
    if request.method == 'POST':
        form = PostEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newpostentry/')
    else:
        form = PostEntryForm()
    return render(request,'createpostentry.html', {'form':form})
    
def file_browser(request):
    tpl = "admin_filebrowser.html"
    user = request.user
    variables = RequestContext(request, { 'user': user }) 
    return render_to_response(tpl, variables)
    
def display_profile(request, id):
    profiles = UserProfile.objects.filter(pk=id)
    tpl = 'profile_page.html'
    return render_to_response(tpl, {'profiles': profiles })

@csrf_protect
def post_status(request):
    posts = PostRequest.objects.all()
    amposts = PostRequest.objects.filter(client__iexact="Amazon")
    apposts = PostRequest.objects.filter(client__iexact="Apple")
    ggposts = PostRequest.objects.filter(client__iexact="Google")
    inposts = PostRequest.objects.filter(client__iexact="Intel")
    msposts = PostRequest.objects.filter(client__iexact="Microsoft")
    psposts = PostRequest.objects.filter(client__iexact="PepsiCo")
    vzposts = PostRequest.objects.filter(client__iexact="Verizon")
    wdposts = PostRequest.objects.filter(client__iexact="Disney")
    tpl = 'post_status.html'
    return render_to_response(tpl, {'posts': posts, 'amposts': amposts, 'apposts': apposts, 'ggposts': ggposts, 'inposts': inposts, 'msposts': msposts, 'psposts': psposts, 'vzposts': vzposts, 'wdposts': wdposts })

def display_post(request, id):
        if request.method == 'POST':
                a = PostRequest.objects.get(pk=id)
                form = PostRequestForm(request.POST, instance=a)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/poststatus/')
        else:
                a = PostRequest.objects.get(pk=id)
                form = PostRequestForm(instance=a)
        return render_to_response('createpostrequest.html', {'form': form})

def edit_postentry(request, id):
    records = PostRequest.objects.get(pk=id)
    tpl = 'admin_editpostentry.html'
    return render_to_response(tpl, {'records': records,})
    
    
@login_required(login_url='/') 
def postsearch(request):
                        form = PostSearchForm() 

                        pagelinks = []
                        clientlinks = []

                        show_results = True 
                        if 'query' in request.GET: 
                                show_results = True 
                                query = request.GET['query'].strip() 
                                if query:
                                        form = PostSearchForm({'query' : query}) 
                                        pagelinks = \
                                                PostPage.objects.filter(job_number__iexact=query)
                                        clientlinks = \
                                                PostPage.objects.filter(client__name__icontains=query)
        

                        if len(clientlinks) >= 1:
                                user = request.user
                                records = PostPage.objects.filter(Q(client__name__icontains=query) & Q(page_type__iexact="POST")).order_by('-job_number')
                                t = get_template('list_template.html')
                                html = t.render(Context({'user': user, 'records': records, 'form': form }))
                                return HttpResponse(html)

                        if    len(pagelinks) >= 1:
                                user = request.user
                                records = PostPage.objects.filter(Q(job_number__icontains=query) & Q(page_type__iexact="POST")).order_by('-create_date')
                                t = get_template('list_template.html')
                                html = t.render(Context({'user': user, 'records': records, 'form': form}))
                                return HttpResponse(html)

                        else:
                                user = request.user
                                tpl = "list_template.html"
                                variables = RequestContext(request, {'user': user, 'form': form,
                                'show_results': show_results}) 
                                return render_to_response(tpl, variables)

def display_prdInboxEntry(request, id):
    if request.method == 'POST':
        form = PrdInboxForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/production-display/'+ id +'/')
        else:
            form = PrdInboxForm(request.POST)
            return HttpResponseRedirect('/production-display/'+ id +'/')
            
    else:
        form = PrdInboxForm()
        user = request.user
        u = UserProfile.objects.get(pk=id)
        assignedrecords = InboxEntry.objects.filter(assigned_by=u)
        creativerecords = InboxEntry.objects.filter(box__iexact="Creative").order_by('status')
        studiorecords = InboxEntry.objects.filter(box__iexact="Studio").order_by('status')
        t = ProjectTeam.objects.get(team_name="Studio")
        records = InboxEntry.objects.filter(Q(assigned_to=u) | Q(assigned_team=t)).order_by('status')
        return render_to_response('home_inbox.html', {'form': form, 'assignedrecords': assignedrecords, 'records': records, 'studiorecords': studiorecords, 'creativerecords': creativerecords, 'user': user}, context_instance=RequestContext(request))


def delete_prdInboxEntry(request, id, userid):
    if request.method == 'POST':
        a=InboxEntry.objects.get(pk=id)
        form = PrdInboxForm(request.POST, instance=a)
        if form.is_valid():
            form.delete()
            return HttpResponseRedirect('/production-display/'+ userid +'/')
    else:
        a=InboxEntry.objects.get(pk=id)
        form = PrdInboxForm(instance=a)
        user = request.user
        u = UserProfile.objects.get(pk=userid)
        creativerecords = InboxEntry.objects.filter(box="Creative")
        studiorecords = InboxEntry.objects.filter(box="Studio")
        records = InboxEntry.objects.filter(assigned_to=u)
    return render(request, 'home_inbox.html', {'form': form, 'records': records, 'studiorecords': studiorecords, 'creativerecords': creativerecords, 'user': user})




def edit_prdInboxEntry(request, id, userid):
    if request.method == 'POST':
        a=InboxEntry.objects.get(pk=id)
        form = PrdInboxForm(request.POST, instance=a)
        if request.POST.get('delete'):
            a.delete()
            return HttpResponseRedirect('/production-display/'+ userid +'/')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/production-display/'+ userid +'/')
    else:
        a=InboxEntry.objects.get(pk=id)
        form = PrdInboxForm(instance=a)
        user = request.user
        u = UserProfile.objects.get(pk=userid)
        assignedrecords = InboxEntry.objects.filter(assigned_by=u)
        creativerecords = InboxEntry.objects.filter(box="Creative")
        studiorecords = InboxEntry.objects.filter(box="Studio")
        records = InboxEntry.objects.filter(assigned_to=u)
        return render_to_response('home_inbox.html', {'form': form, 'assignedrecords': assignedrecords, 'records': records, 'studiorecords': studiorecords, 'creativerecords': creativerecords, 'user': user}, context_instance=RequestContext(request))


def quickpost(request, job_number):
            records = PostEntry.objects.filter(job_number=job_number)
            precords = PostPage.objects.filter(job_number=job_number).order_by('-create_date')
            cdrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='cd_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
            cerecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='ce_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
            cmrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='cm_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
            mrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='m_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
            frrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='FinalRelease').order_by('-date', '-post_round', 'cell_number', 'post_title')

            if request.user.is_authenticated():
                    tpl = 'quickpost.html'
                    return render_to_response(tpl, { 'records': records, 'precords': precords, 'mrecords': mrecords, 'cdrecords': cdrecords, 'cerecords': cerecords, 'cmrecords': cmrecords, 'frrecords': frrecords })
            else:
                    tpl = 'quickpost.html'
                    return render_to_response(tpl, { 'records': records, 'precords': precords, 'mrecords': mrecords, 'cdrecords': cdrecords, 'cerecords': cerecords, 'cmrecords': cmrecords, 'frrecords': frrecords })

