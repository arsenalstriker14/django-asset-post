# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import assetpost.models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountGroup',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('client', models.CharField(choices=[('amz', 'Amazon'), ('apl', 'Apple'), ('goog', 'Google'), ('int', 'Intel'), ('msft', 'Microsoft'), ('pps', 'PepsiCo'), ('vzn', 'Verizon'), ('wdc', 'Disney')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ClientList',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=64, null=True, blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fname', models.CharField(max_length=64, null=True, blank=True)),
                ('lname', models.CharField(max_length=64, null=True, blank=True)),
                ('group', models.CharField(choices=[('Account', 'Account'), ('Administration', 'Administration'), ('Creative', 'Creative'), ('Interactive', 'Interactive'), ('IT', 'IT'), ('Studio', 'Studio')], max_length=50)),
                ('position', models.CharField(max_length=64, null=True, blank=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('fax', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FreelanceProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fullname', models.CharField(max_length=64)),
                ('company', models.CharField(max_length=64, null=True, blank=True)),
                ('position', models.CharField(max_length=64, null=True, blank=True)),
                ('address1', models.CharField(max_length=130, null=True, blank=True)),
                ('address2', models.CharField(max_length=30, null=True, blank=True)),
                ('city', models.CharField(max_length=64, null=True, blank=True)),
                ('state', models.CharField(max_length=64, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=15, null=True, blank=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('extension', models.CharField(max_length=15, null=True, blank=True)),
                ('hphone', models.CharField(max_length=15, null=True, blank=True)),
                ('mobile', models.CharField(max_length=15, null=True, blank=True)),
                ('fax', models.CharField(max_length=15, null=True, blank=True)),
                ('notes', models.TextField(max_length=2000, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['fullname'],
            },
        ),
        migrations.CreateModel(
            name='InboxEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('job_number', models.CharField(max_length=14)),
                ('cell_number', models.CharField(max_length=20, null=True, blank=True)),
                ('job_name', models.CharField(max_length=64)),
                ('request', models.CharField(choices=[('comp', 'comp'), ('creative execution', 'creative execution'), ('mechanical set', 'mechanical set'), ('mechanical revision', 'mechanical revision'), ('revise & post', 'revise & post'), ('post', 'post'), ('queue to release', 'queue to release'), ('release', 'release'), ('post release revision', 'post release revision'), ('re-release', 're-release'), ('retouching', 'retouching')], null=True, blank=True, max_length=64)),
                ('date_in', models.DateField(verbose_name='Date', auto_now=True)),
                ('date_due', models.DateTimeField(verbose_name='Due')),
                ('basecamp_link', models.URLField(max_length=300, validators=[django.core.validators.RegexValidator(code='nomatch', message='url must begin with http or https', regex='^(http|https)://')], blank=True)),
                ('note', models.TextField(max_length=1000, null=True, blank=True)),
                ('box', models.CharField(choices=[('Studio', 'Studio'), ('Creative', 'Creative'), ('Personal', 'Personal')], max_length=64)),
                ('status', models.CharField(choices=[('Awaiting Action', 'Awaiting Action'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Posted', 'Posted'), ('Released', 'Released')], default='Awaiting Action', max_length=30)),
                ('completed_on', models.DateTimeField(verbose_name='Completed', null=True, blank=True)),
            ],
            options={
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='JobContact',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=64, null=True, blank=True)),
                ('position', models.CharField(max_length=64, null=True, blank=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('fax', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('visibility', models.CharField(choices=[('visible', 'visible'), ('hidden', 'hidden')], default='visible', max_length=7)),
                ('job_number', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='nomatch', message='Please enter a valid job number', regex='^\\w{8}$')])),
                ('cell_number', models.CharField(max_length=4, null=True, blank=True)),
                ('post_title', models.CharField(max_length=64, null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('post_type', models.CharField(choices=[('cd_round', 'Concept Development Round'), ('ce_round', 'Creative Execution Round'), ('cm_round', 'Coded Project Round'), ('m_round', 'Print Mechanical Round'), ('FinalRelease', 'Final Release')], max_length=64)),
                ('post_round', models.CharField(max_length=20)),
                ('is_rerelease', models.BooleanField(default=False)),
                ('docfile', models.FileField(max_length=300, null=True, blank=True, storage=assetpost.models.OverwriteStorage(), upload_to=assetpost.models.content_file_name)),
                ('url_link', models.URLField(max_length=300, blank=True)),
                ('add_misc', models.NullBooleanField()),
                ('misc_link', models.CharField(max_length=64, null=True, blank=True)),
                ('link_misc', models.FileField(max_length=300, null=True, blank=True, upload_to=assetpost.models.content_file_name)),
                ('add_misc2', models.NullBooleanField()),
                ('misc_link2', models.CharField(max_length=64, null=True, blank=True)),
                ('link_misc2', models.FileField(max_length=300, null=True, blank=True, upload_to=assetpost.models.content_file_name)),
                ('add_mobile_view', models.NullBooleanField()),
                ('mobile_view_url', models.URLField(max_length=300, validators=[django.core.validators.RegexValidator(code='nomatch', message='url must begin with http or https', regex='^(http|https)://')], blank=True)),
                ('add_pdf', models.NullBooleanField()),
                ('link_pdf', models.FileField(max_length=300, null=True, blank=True, upload_to=assetpost.models.content_file_name)),
                ('add_html', models.NullBooleanField()),
                ('link_html', models.FileField(max_length=300, null=True, blank=True, upload_to=assetpost.models.content_file_name)),
                ('add_report', models.NullBooleanField()),
                ('link_report', models.FileField(max_length=300, null=True, blank=True, upload_to=assetpost.models.content_file_name)),
                ('add_text', models.NullBooleanField()),
                ('link_text', models.FileField(max_length=300, null=True, blank=True, upload_to=assetpost.models.content_file_name)),
                ('add_zip', models.NullBooleanField()),
                ('link_zip', models.FileField(max_length=300, null=True, blank=True, upload_to=assetpost.models.content_file_name)),
                ('client', models.ForeignKey(null=True, to='assetpost.ClientList', on_delete=django.db.models.deletion.SET_NULL, db_column='client')),
            ],
            options={
                'ordering': ['-date', 'cell_number'],
            },
        ),
        migrations.CreateModel(
            name='PostPage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('job_number', models.CharField(max_length=8, unique=True)),
                ('job_name', models.CharField(max_length=64)),
                ('page_type', models.CharField(max_length=50, default='POST')),
                ('create_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('client', models.ForeignKey(null=True, to='assetpost.ClientList', on_delete=django.db.models.deletion.SET_NULL, db_column='client')),
                ('contact', models.ManyToManyField(to='assetpost.AccountGroup')),
            ],
            options={
                'permissions': (('view_postpage', 'View postpage'),),
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('team_name', models.CharField(choices=[('Charter Business', 'Charter Business'), ('Charter Communications', 'Charter Communications'), ('Kaiser Permanente', 'Kaiser Permanente'), ('Mastercard', 'Mastercard'), ('Studio', 'Studio'), ('Wells Fargo', 'Wells Fargo'), ('All Users', 'All Users')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TaskEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('project', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='nomatch', message='Please enter a valid job number', regex='^\\w{8}$')])),
                ('project_type', models.CharField(choices=[('Set Mechanical', 'Set Mechanical'), ('Revise Mechanical', 'Revise Mechanical'), ('Package Release', 'Package Release'), ('Other', 'Other')], max_length=64)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('message', models.TextField(max_length=500, null=True, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('returned', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskGroup',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('group_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fullname', models.CharField(max_length=64)),
                ('company', models.CharField(choices=[('amz', 'Amazon'), ('apl', 'Apple'), ('goog', 'Google'), ('int', 'Intel'), ('msft', 'Microsoft'), ('pps', 'PepsiCo'), ('vzn', 'Verizon'), ('wdc', 'Disney')], max_length=50)),
                ('position', models.CharField(max_length=64, null=True, blank=True)),
                ('egroup', models.CharField(choices=[('Account', 'Account'), ('Administration', 'Administration'), ('Creative', 'Creative'), ('Interactive', 'Interactive'), ('IT', 'IT'), ('Studio', 'Studio')], max_length=50)),
                ('address1', models.CharField(max_length=130, null=True, blank=True)),
                ('address2', models.CharField(max_length=30, null=True, blank=True)),
                ('city', models.CharField(max_length=64, null=True, blank=True)),
                ('state', models.CharField(max_length=64, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=15, null=True, blank=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('extension', models.CharField(max_length=15, null=True, blank=True)),
                ('hphone', models.CharField(max_length=15, null=True, blank=True)),
                ('mobile', models.CharField(max_length=15, null=True, blank=True)),
                ('fax', models.CharField(max_length=15, null=True, blank=True)),
                ('notes', models.TextField(max_length=2000, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'ordering': ['fullname'],
            },
        ),
        migrations.AddField(
            model_name='taskgroup',
            name='member',
            field=models.ManyToManyField(to='assetpost.UserProfile'),
        ),
        migrations.AddField(
            model_name='taskentry',
            name='assigned_member',
            field=models.ForeignKey(null=True, blank=True, to='assetpost.UserProfile', related_name='+', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='taskentry',
            name='assigned_team',
            field=models.ForeignKey(null=True, blank=True, to='assetpost.UserProfile', related_name='+', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='taskentry',
            name='completed_by',
            field=models.ForeignKey(null=True, blank=True, to='assetpost.UserProfile', related_name='+', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='taskentry',
            name='created_by',
            field=models.ForeignKey(null=True, blank=True, to='assetpost.UserProfile', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='projectteam',
            name='team_member',
            field=models.ManyToManyField(to='assetpost.UserProfile'),
        ),
        migrations.AddField(
            model_name='inboxentry',
            name='accepted_by',
            field=models.ForeignKey(null=True, blank=True, to='assetpost.UserProfile', related_name='+'),
        ),
        migrations.AddField(
            model_name='inboxentry',
            name='assigned_by',
            field=models.ForeignKey(to='assetpost.UserProfile'),
        ),
        migrations.AddField(
            model_name='inboxentry',
            name='assigned_team',
            field=models.ManyToManyField(to='assetpost.ProjectTeam', blank=True),
        ),
        migrations.AddField(
            model_name='inboxentry',
            name='assigned_to',
            field=models.ManyToManyField(to='assetpost.UserProfile', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='accountgroup',
            name='member',
            field=models.ManyToManyField(to='assetpost.UserProfile'),
        ),
    ]
