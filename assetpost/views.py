from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import Context, RequestContext
from django.template.loader import get_template
from .models import *
from .forms import *
from django.forms.models import modelformset_factory, BaseModelFormSet
from django.template.response import TemplateResponse
from django.views.generic import CreateView, UpdateView
from rest_framework import authentication, permissions, viewsets

from .models import PostEntry
from .serializers import EntrySerializer
from .tasks import SignUpTask

# Create your views here.
class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class EntryViewSet(viewsets.ModelViewSet):
    queryset = PostEntry.objects.order_by('client')
    serializer_class = EntrySerializer


def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                SignUpTask.delay(6, 7)
                return HttpResponseRedirect('/main/')
    return render_to_response('registration/login.html', context_instance=RequestContext(request))

def logout_page(request):
    logout(request)
    return redirect('registration/login.html')


def createEntry(request):

    if request.method == 'POST':
        form = PostEntryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            tpl = 'assetpost/postentry_form.html'
            variables = RequestContext(request, {'form':form })
            return HttpResponseRedirect('/assetpost/create-entry/')
        
        else:
                form = PostEntryForm()
                tpl = 'assetpost/postentry_form.html'
                variables = RequestContext(request, {'form':form })
                return render_to_response(tpl, variables)
    else:
        form = PostEntryForm()
        tpl = 'assetpost/postentry_form.html'
        variables = RequestContext(request, {'form':form })
        return render_to_response(tpl, variables)


def updateEntry(request, id):

    if request.method == 'POST':
        form = PostEntryForm(request.POST, request.FILES, instance = PostEntry.objects.get(pk = id))
        if request.POST.get('delete'):
            instance = PostEntry.objects.get(pk=id)
            instance.delete()
            return HttpResponseRedirect('/main/')

        if form.is_valid():
            URL = request.POST.get('URL')
            form.save()
            return HttpResponseRedirect(URL)
        
    else:
        form = PostEntryForm(instance = PostEntry.objects.get(pk = id))
        tpl = 'assetpost/postupdate_form.html'
        variables = RequestContext(request, {'form':form })
        return render_to_response(tpl, variables)


def updatePage(request, id):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance = PostPage.objects.get(pk = id))
        if request.POST.get('delete'):
            instance = PostPage.objects.get(pk=id)
            URL = request.POST.get('URL')
            instance.delete()
            return HttpResponseRedirect(URL)

        if form.is_valid():
            URL = request.POST.get('URL')
            form.save()
            return HttpResponseRedirect(URL)
        
    else:
        form = PageForm(instance = PostPage.objects.get(pk = id))
        tpl = 'assetpost/pageupdate_form.html'
        variables = RequestContext(request, {'form':form })
        return render_to_response(tpl, variables)


# class BasePostEntryFormSet(BaseModelFormSet):
#     def __init__(self, *args, **kwargs):
#         super(BasePostEntryFormSet, self).__init__(*args, **kwargs)
#         self.queryset = PostEntry.objects.none()


def multipost(request):
    PostEntryFormset = modelformset_factory(PostEntry, fields='__all__', extra=6, formset=BasePostEntryFormSet)
    if request.method == 'POST':
        formset = PostEntryFormset(request.POST, request.FILES)

        if(formset.is_valid()):
            formset.save()
            return HttpResponseRedirect('/assetpost/multipost/')

    else:
        formset = PostEntryFormset()
        clients = ClientList.objects.all()
        variables = RequestContext(request, {'clients' : clients, 'formset':formset })
        return render_to_response("assetpost/multipost_form.html", variables)

def multipost_init(request, client, id):
    PostEntryFormset = modelformset_factory(PostEntry, fields='__all__', extra=6, formset=BasePostEntryFormSet)
    if request.method == 'POST':
        formset = PostEntryFormset(request.POST, request.FILES)
        
        if(formset.is_valid()):
            formset.save()
            return HttpResponseRedirect('/assetpost/multipost/')

    else:
        formset = PostEntryFormset(initial=[{'client': client, 'job_number': id,},{'client': client, 'job_number': id,},{'client': client, 'job_number': id,},{'client': client, 'job_number': id,},{'client': client, 'job_number': id,},{'client': client, 'job_number': id,}])
        clients = ClientList.objects.all()
        variables = RequestContext(request, {'clients' : clients, 'formset':formset })
        return render_to_response("assetpost/multipost_form.html", variables)
 

class PostEntryUpdate(UpdateView):
    model = PostEntry
    fields = '__all__'
    success_url = "../assetpost/newpostentry/"


class PageCreate(CreateView):
    model = PostPage
    fields = ['client', 'job_number', 'job_name', 'create_date',  'contact']
    success_url = "/main/"


# class PageUpdate(UpdateView):
#     model = PostPage
#     fields = ['client', 'job_number', 'job_name', 'create_date',  'contact', 'URL']
#     template_name = 'assetpost/pageupdate_form.html'
#     success_url = URL


def create_postpage(request):
    tpl = "createpostpage.html"
    user = request.user
    variables = RequestContext(request, { 'user': user }) 
    return TemplateResponse(request, tpl, {'form': PageForm()})


    
def file_browser(request):
    tpl = "admin_filebrowser.html"
    clients = ClientList.objects.all()
    user = request.user
    variables = RequestContext(request, { 'user': user, 'clients' : clients }) 
    return render_to_response(tpl, variables)

    
    
@login_required(login_url='/') 
def postsearch(request):
                        form = PostsearchForm() 

                        pagelinks = []
                        clientlinks = []

                        show_results = True
                        if 'query' in request.GET:
                                show_results = True
                                query = request.GET['query'].strip()
                                if query:
                                        form = PostsearchForm({'query' : query})
                                        pagelinks = \
                                                PostPage.objects.filter(job_number__iexact=query)
                                        clientlinks = \
                                                PostPage.objects.filter(client__name__icontains=query)

                        if len(clientlinks) >= 1:
                                user = request.user
                                records = PostPage.objects.filter(client__name__icontains=query).order_by('-job_number')
                                cellrecords = PostEntry.objects.filter(client__name__icontains=query)
                                clients = ClientList.objects.all()
                                t = get_template('list_template.html')
                                html = t.render(Context({'user': user, 'records': records, 'cellrecords': cellrecords, 'form': form }))
                                #return HttpResponse(html)
                                return render_to_response('list_template.html', {'user': user, 'records': records, 'cellrecords': cellrecords, 'clients': clients, 'form': form}, context_instance=RequestContext(request))


                        if    len(pagelinks) >= 1:
                                user = request.user
                                records = PostPage.objects.filter(job_number__icontains=query).order_by('-create_date')
                                cellrecords = PostEntry.objects.filter(job_number__icontains=query)
                                clients = ClientList.objects.all()
                                t = get_template('list_template.html')
                                html = t.render(Context({'user': user, 'records': records, 'cellrecords': cellrecords, 'form': form}))
                                #return HttpResponse(html)
                                return render_to_response('list_template.html', {'user': user, 'records': records, 'cellrecords': cellrecords, 'clients': clients, 'form': form}, context_instance=RequestContext(request))

                        else:
                                user = request.user
                                tpl = "list_template.html"
                                clients = ClientList.objects.all()
                                variables = RequestContext(request, {'user': user, 'clients' : clients, 'form': form,
                                'show_results': show_results}) 
                                return render_to_response(tpl, variables)


def quickpost(request, job_number):
    records = PostEntry.objects.filter(job_number=job_number)
    precords = PostPage.objects.filter(job_number=job_number).order_by('-create_date')
    cdrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='cd_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
    cerecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='ce_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
    cmrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='cm_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
    mrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='m_round').order_by('-date', '-post_round', 'cell_number', 'post_title')
    frrecords = PostEntry.objects.filter(job_number=job_number, post_type__iexact='FinalRelease').order_by('-date', '-post_round', 'cell_number', 'post_title')

    if request.method == 'POST':
        form = PostEntryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            tpl = 'quickpost.html'
            variables = RequestContext(request, {'form':form, 'records': records, 'precords': precords, 'mrecords': mrecords, 'cdrecords': cdrecords, 'cerecords': cerecords, 'cmrecords': cmrecords, 'frrecords': frrecords })
            return HttpResponseRedirect('/quickpost/' + job_number + '/')
        
        else:
                tpl = 'quickpost.html'
                variables = RequestContext(request, { 'records': records, 'precords': precords, 'mrecords': mrecords, 'cdrecords': cdrecords, 'cerecords': cerecords, 'cmrecords': cmrecords, 'frrecords': frrecords })
                return render_to_response(tpl, variables)
    else:
        form = PostEntryForm()
        tpl = 'quickpost.html'
        variables = RequestContext(request, { 'form':form, 'records': records, 'precords': precords, 'mrecords': mrecords, 'cdrecords': cdrecords, 'cerecords': cerecords, 'cmrecords': cmrecords, 'frrecords': frrecords })
        return render_to_response(tpl, variables)



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