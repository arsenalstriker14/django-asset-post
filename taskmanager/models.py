from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from assetpost.models import UserProfile, ProjectTeam
import django_filters
import datetime

PRIORITY_CHOICES = (
    ('normal', 'normal'),
    ('low', 'low'),
    ('high', 'high'),
    ('urgent', 'urgent'),    
)

STATUS_CHOICES = (
    ('Awaiting Action', 'Awaiting Action'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Posted', 'Posted'),
    ('Released', 'Released'),
)
class InboxRequest(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)

    def __str__(self):
        return u'%s' % (self.name)

    class Admin:
        pass

class TaskBox(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)

    def __str__(self):
        return u'%s' % (self.name)

    class Admin:
        pass

class InboxEntry(models.Model):
        job_number = models.CharField(max_length=14, unique=False, blank=False, null=False)
        cell_number = models.CharField(max_length=20, unique=False, blank=True, null=True)
        job_name = models.CharField(max_length=64, unique=False, blank=False, null=False)
        request = models.ForeignKey(InboxRequest, blank=True, null=True)
        priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default="Normal")
        date_in = models.DateField(("Date"), auto_now=True)
        date_due = models.DateTimeField(("Due"),auto_now=False)
        note = models.TextField(max_length=1000, unique=False, blank=True, null=True)
        assigned_by = models.ForeignKey(UserProfile, blank=False, null=False, default=User)
        box = models.ForeignKey(TaskBox, blank=True, null=True)
        assigned_to = models.ManyToManyField(UserProfile, related_name='name', blank=True)
        assigned_team = models.ManyToManyField(ProjectTeam, blank=True)
        status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Awaiting Action")
        accepted_by = models.ForeignKey(UserProfile, related_name='+', blank=True, null=True)
        completed_on = models.DateTimeField(("Completed"),auto_now=False, blank=True, null=True)

        def __str__(self):
            return u'%s %s' % (self.job_number, self.job_name)

        class Admin: 
            pass
            
        class Meta:
            ordering = ['status']



