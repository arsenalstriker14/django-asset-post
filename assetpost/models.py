from django.db import models
import os.path
from django import forms
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.forms import ModelForm
from django.db.models import TextField
from django.contrib.auth.models import User 
from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.files import File
from django.core.validators import RegexValidator
import django_filters
import datetime


CLIENT_CHOICES = (
    ('amz', 'Amazon'),
    ('apl', 'Apple'),
    ('goog', 'Google'),
    ('int', 'Intel'),
    ('msft', 'Microsoft'),
    ('pps', 'PepsiCo'),
    ('vzn', 'Verizon'),
    ('wdc', 'Disney'),   
)

PAGE_CHOICES = (
        ('Project', 'Project'),
        ('Portal', 'Portal'),
        ('Released', 'Released'),
)

POST_CHOICES = (
    ('cd_round', 'Concept Development Round'),
    ('ce_round', 'Creative Execution Round'),
    ('cm_round', 'Coded Project Round'),
    ('m_round', 'Print Mechanical Round'),
    ('FinalRelease', 'Final Release'),
)
PRINT_CHOICES = (
    ('comp', 'comp'),
    ('creative execution', 'creative execution'),
    ('mechanical set', 'mechanical set'),
    ('mechanical revision', 'mechanical revision'),
    ('revise & post', 'revise & post'),
    ('post', 'post'),
    ('queue to release', 'queue to release'),
    ('release', 'release'),
    ('post release revision', 'post release revision'),
    ('re-release', 're-release'),
    ('retouching', 'retouching'),
)

EMP_GROUP_CHOICES = (
    ('Account', 'Account'),
    ('Administration', 'Administration'),
    ('Creative', 'Creative'),
    ('Interactive', 'Interactive'),
    ('IT', 'IT'),
    ('Studio', 'Studio'),
)

TEAM_CHOICES = (
    ('Charter Business', 'Charter Business'),
    ('Charter Communications', 'Charter Communications'),
    ('Kaiser Permanente', 'Kaiser Permanente'),
    ('Mastercard', 'Mastercard'),
    ('Studio', 'Studio'),
    ('Wells Fargo', 'Wells Fargo'),
    ('All Users', 'All Users' ),

)

STATUS_CHOICES = (
    ('Awaiting Action', 'Awaiting Action'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Posted', 'Posted'),
    ('Released', 'Released'),
)
INBOX_CHOICES = (
    ('Studio', 'Studio'),
    ('Creative', 'Creative'),
    ('Personal', 'Personal'),
)

LINK_CHOICES = (
        ('yes', 'yes'),
)

DISPLAY_CHOICES = (
        ('visible', 'visible'),
        ('hidden', 'hidden'),
)

TYPE_CHOICES = (
        ('Set Mechanical', 'Set Mechanical'),
        ('Revise Mechanical', 'Revise Mechanical'),
        ('Package Release', 'Package Release'),
        ('Other', 'Other'),
)

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
 
class JobContact(models.Model):
        name = models.CharField(max_length=64, unique=False, blank=True, null=True)
        position = models.CharField(max_length=64, unique=False, blank=True, null=True)
        phone = models.CharField(max_length=15, unique=False, blank=True, null=True)
        fax = models.CharField(max_length=15, unique=False, blank=True, null=True)
        email = models.EmailField(blank=True, null=True)
        
        def __unicode__ (self):
                return self.name

        class Admin: 
                pass
                
class ClientList(models.Model):
        name = models.CharField(max_length=64, unique=True, blank=True, null=True)
        
        def __unicode__ (self):
                return self.name

        class Admin: 
                pass

def content_file_name(instance, filename):
        return '/'.join([ instance.client.name, instance.job_number, instance.post_type + "_" + instance.post_round, instance.job_number + "-" + instance.cell_number, filename])

class PostEntry(models.Model):
            visibility = models.CharField(max_length=7, choices=DISPLAY_CHOICES, default='visible')
            client = models.ForeignKey(ClientList, blank=False, null=True, db_column='client', on_delete=models.SET_NULL)
            job_number = models.CharField(validators=[RegexValidator(regex='^\w{8}$', message='Please enter a valid job number', code='nomatch')], max_length=8, unique=False, blank=False, null=False)
            cell_number = models.CharField(max_length=4, unique=False, blank=True, null=True)
            post_title = models.CharField(max_length=64, unique=False, blank=True, null=True)
            date = models.DateField(("Date"), default=datetime.date.today)
            post_type = models.CharField(max_length=64, choices=POST_CHOICES)
            post_round = models.CharField(max_length=20, blank=False, null=False)
            is_rerelease = models.BooleanField(default=False)
            docfile = models.FileField(upload_to=content_file_name, storage=OverwriteStorage(), blank=True, null=True, max_length=300)
            url_link = models.URLField(blank=True, null=False, max_length=300)
            add_misc = models.NullBooleanField()
            misc_link = models.CharField(max_length=64, blank=True, null=True)
            link_misc = models.FileField(upload_to=content_file_name, blank=True, null=True, max_length=300)
            add_misc2 = models.NullBooleanField()
            misc_link2 = models.CharField(max_length=64, blank=True, null=True)
            link_misc2 = models.FileField(upload_to=content_file_name, blank=True, null=True, max_length=300)
            add_mobile_view = models.NullBooleanField()
            mobile_view_url = models.URLField(validators=[RegexValidator(regex='^(http|https)://', message='url must begin with http or https', code='nomatch')], blank=True, null=False, max_length=300)
            add_pdf = models.NullBooleanField()
            link_pdf = models.FileField(upload_to=content_file_name, blank=True, null=True, max_length=300)
            add_html = models.NullBooleanField()
            link_html = models.FileField(upload_to=content_file_name, blank=True, null=True, max_length=300)
            add_report = models.NullBooleanField()
            link_report = models.FileField(upload_to=content_file_name, blank=True, null=True, max_length=300)
            add_text = models.NullBooleanField()
            link_text = models.FileField(upload_to=content_file_name, blank=True, null=True, max_length=300)
            add_zip = models.NullBooleanField()
            link_zip = models.FileField(upload_to=content_file_name, blank=True, null=True, max_length=300)
            

            def __unicode__ (self):
                    return u'%s %s %s %s %s' % (self.client, self.job_number, '-', self.cell_number, self.post_title)

            def save(self, force_insert=False, force_update=False):
                    self.job_number = self.job_number.upper()
                    self.cell_number = self.cell_number.upper()
                    super(PostEntry, self).save(force_insert, force_update)

            class Meta:
                    ordering = ['-date', 'cell_number']

            class Admin: 
                    pass


class UserProfile(models.Model):  
    user = models.ForeignKey(User, unique=True, null=True, on_delete=models.SET_NULL)
    fullname = models.CharField(max_length=64, unique=False)
    company = models.CharField(max_length=50, choices=CLIENT_CHOICES)
    position = models.CharField(max_length=64, unique=False, blank=True, null=True)
    egroup = models.CharField(max_length=50, choices=EMP_GROUP_CHOICES)
#    im_username = models.CharField(max_length=64, unique=True, blank=True, null=True)
    address1 = models.CharField(max_length=130, unique=False, blank=True, null=True)
    address2 = models.CharField(max_length=30, unique=False, blank=True, null=True)
    city = models.CharField(max_length=64, unique=False, blank=True, null=True)
    state = models.CharField(max_length=64, unique=False, blank=True, null=True)
    zipcode = models.CharField(max_length=15, unique=False, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=False, blank=True, null=True)
    extension = models.CharField(max_length=15, unique=False, blank=True, null=True)
    hphone = models.CharField(max_length=15, unique=False, blank=True, null=True)
    mobile = models.CharField(max_length=15, unique=False, blank=True, null=True)
    fax = models.CharField(max_length=15, unique=False, blank=True, null=True)
    notes = models.TextField(max_length=2000, blank=True, null=True)
    email = models.EmailField()

    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
  
  
    def __unicode__(self):
        return u'%s' % self.fullname
        
    class Meta:
            ordering = ['fullname']

    class Admin: 
        pass  


class TaskGroup(models.Model):
        group_name = models.CharField(max_length=100)
        member = models.ManyToManyField(UserProfile)

        def __unicode__ (self):
                return u'%s' % (self.group_name)

        class Admin:
                pass

class AccountGroup(models.Model):
        client = models.CharField(max_length=50, choices=CLIENT_CHOICES)
        member = models.ManyToManyField(UserProfile)

        def __unicode__ (self):
                return u'%s' % (self.client)

        class Admin:
                pass

class PostPage(models.Model):
        client = models.ForeignKey(ClientList, blank=False, null=True, db_column='client', on_delete=models.SET_NULL)
        job_number = models.CharField(max_length=8, unique=True, blank=False, null=False)
        job_name = models.CharField(max_length=64, unique=False, blank=False, null=False)
        page_type = models.CharField(max_length=50, default='POST')
        create_date = models.DateField(("Date"), default=datetime.date.today)
        contact = models.ManyToManyField(AccountGroup)

        def __unicode__ (self):
                return u'%s %s %s' % (self.client, self.job_number, self.job_name)

        def save(self, force_insert=False, force_update=False):
                self.job_number = self.job_number.upper()
                super(PostPage, self).save(force_insert, force_update)

        class Admin: 
                pass


        class Meta:
                ordering = ['-create_date']
                permissions = (('view_postpage', 'View postpage'),)




class RequireLoginMiddleware(object):
    """
    Require Login middleware. If enabled, each Django-powered page will
    require authentication.
    
    If an anonymous user requests a page, he/she is redirected to the login
    page set by REQUIRE_LOGIN_PATH or /accounts/login/ by default.
    """
    def __init__(self):
        self.require_login_path = getattr(settings, 'REQUIRE_LOGIN_PATH', '/accounts/login/')
    
    def process_request(self, request):
        if request.path != self.require_login_path and request.user.is_anonymous():
            if request.POST:
                return login(request)
            else:
                return HttpResponseRedirect('%s?next=%s' % (self.require_login_path, request.path))


class AutoLogout:
  def process_request(self, request):
    if not request.user.is_authenticated() :
      #Can't log out if not logged in
      return

    try:
      if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
        auth.logout(request)
        del request.session['last_touch']
        return
    except KeyError:
      pass

    request.session['last_touch'] = datetime.now()


class FreelanceProfile(models.Model):  
    fullname = models.CharField(max_length=64, unique=False)
    company = models.CharField(max_length=64,unique=False, blank=True, null=True)
    position = models.CharField(max_length=64, unique=False, blank=True, null=True)
    address1 = models.CharField(max_length=130, unique=False, blank=True, null=True)
    address2 = models.CharField(max_length=30, unique=False, blank=True, null=True)
    city = models.CharField(max_length=64, unique=False, blank=True, null=True)
    state = models.CharField(max_length=64, unique=False, blank=True, null=True)
    zipcode = models.CharField(max_length=15, unique=False, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=False, blank=True, null=True)
    extension = models.CharField(max_length=15, unique=False, blank=True, null=True)
    hphone = models.CharField(max_length=15, unique=False, blank=True, null=True)
    mobile = models.CharField(max_length=15, unique=False, blank=True, null=True)
    fax = models.CharField(max_length=15, unique=False, blank=True, null=True)
    notes = models.TextField(max_length=2000, blank=True, null=True)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s' % self.fullname

    class Meta:
            ordering = ['fullname']

    class Admin: 
        pass

def user_post_delete(sender, instance, **kwargs):
    try:
        UserProfile.objects.get(user=instance).delete()
    except:
        pass

def user_post_save(sender, instance, **kwargs):
    try:
        profile, new = UserProfile.objects.get_or_create(user=instance)
    except:
        pass

models.signals.post_delete.connect(user_post_delete, sender=User)
models.signals.post_save.connect(user_post_save, sender=User)

class Employee(models.Model):
        fname = models.CharField(max_length=64, unique=False, blank=True, null=True)
        lname = models.CharField(max_length=64, unique=False, blank=True, null=True)
        group = models.CharField(max_length=50, choices=EMP_GROUP_CHOICES)
        position = models.CharField(max_length=64, unique=False, blank=True, null=True)
        phone = models.CharField(max_length=15, unique=False, blank=True, null=True)
        fax = models.CharField(max_length=15, unique=False, blank=True, null=True)
        email = models.EmailField(blank=True, null=True)
        
        def __unicode__ (self):
                return u'%s' % self.lname

        class Admin: 
                pass

class ProjectTeam(models.Model):
        team_name = models.CharField(max_length=64, choices=TEAM_CHOICES)
        team_member = models.ManyToManyField(UserProfile)

        def __unicode__ (self):
                return u'%s' % self.team_name

        class Admin: 
                pass


class InboxEntry(models.Model):
        job_number = models.CharField(max_length=14, unique=False, blank=False, null=False)
        cell_number = models.CharField(max_length=20, unique=False, blank=True, null=True)
        job_name = models.CharField(max_length=64, unique=False, blank=False, null=False)
        request = models.CharField(max_length=64, choices=PRINT_CHOICES, blank=True, null=True)
        date_in = models.DateField(("Date"), auto_now=True)
        date_due = models.DateTimeField(("Due"),auto_now=False)
        basecamp_link = models.URLField(validators=[RegexValidator(regex='^(http|https)://', message='url must begin with http or https', code='nomatch')], blank=True, null=False, max_length=300)
        note = models.TextField(max_length=1000, unique=False, blank=True, null=True)
        assigned_by = models.ForeignKey(UserProfile, blank=False, null=False)
        box = models.CharField(max_length=64, choices=INBOX_CHOICES)
        assigned_to = models.ManyToManyField(UserProfile, related_name='+', blank=True)
        assigned_team = models.ManyToManyField(ProjectTeam, blank=True)
        status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Awaiting Action")
        accepted_by = models.ForeignKey(UserProfile, related_name='+', blank=True, null=True)
        completed_on = models.DateTimeField(("Completed"),auto_now=False, blank=True, null=True)

        def __unicode__ (self):
            return u'%s %s' % (self.job_number, self.job_name)

        class Admin: 
            pass
            
        class Meta:
            ordering = ['status']


class InboxEntryFilter(django_filters.FilterSet):
        basecamp_link = django_filters.AllValuesFilter(widget=django_filters.widgets.LinkWidget)
        status = django_filters.AllValuesFilter(widget=django_filters.widgets.LinkWidget)
        class Meta:
                model = InboxEntry
                fields =  ['job_number', 'cell_number', 'job_name', 'basecamp_link', 'note', 'status']

class TaskEntry(models.Model):
        project = models.CharField(validators=[RegexValidator(regex='^\w{8}$', message='Please enter a valid job number', code='nomatch')], max_length=8, unique=False, blank=False, null=False)
        project_type = models.CharField(max_length=64, choices=TYPE_CHOICES)
        description = models.CharField(max_length=200, unique=False, blank=True, null=True)
        message = models.TextField(max_length=500, unique=False, blank=True, null=True)
        created_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.SET_NULL)
        assigned_team = models.ForeignKey(UserProfile, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
        assigned_member = models.ForeignKey(UserProfile, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
        create_date = models.DateTimeField(auto_now_add=True)
        due_date = models.DateTimeField(auto_now_add=False)
        completed_by = models.ForeignKey(UserProfile, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
        returned = models.DateTimeField(auto_now_add=False)

        def __unicode__ (self):
            return u'%s %s' % (self.project, self.description)

        class Admin: 
            pass
