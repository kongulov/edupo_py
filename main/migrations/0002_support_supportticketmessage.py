# Generated by Django 4.2 on 2025-03-16 08:49

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_remove_myuser_adress_myuser_position'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(editable=False, max_length=20, null=True, unique=True, verbose_name='Ticket ID')),
                ('title', models.CharField(max_length=1200, verbose_name='Subject')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('ticket_type', models.IntegerField(choices=[(1, 'Technical'), (2, 'Feedback'), (3, 'Bug Report'), (4, 'Feature Request'), (5, 'Account Issue'), (6, 'Billing & Payment'), (7, 'General Inquiry')], verbose_name='Type')),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'Closed')], verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('file', models.FileField(upload_to='support_files/', verbose_name='Attachment')),
                ('priority', models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], verbose_name='Priority')),
                ('slug', models.SlugField(editable=False, max_length=150, null=True, unique=True, verbose_name='Slug')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Course Author')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company', verbose_name='Course Company')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SupportTicketMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('file', models.FileField(blank=True, null=True, upload_to='ticket_messages/', verbose_name='Attachment')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='main.support', verbose_name='Ticket')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
