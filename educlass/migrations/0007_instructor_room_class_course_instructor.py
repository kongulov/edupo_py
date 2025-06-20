# Generated by Django 4.2 on 2025-05-10 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educlass', '0006_alter_course_options_course_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1200, verbose_name='Full name')),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructors',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1200, verbose_name='Room name')),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1200, verbose_name='Class name')),
                ('number', models.CharField(max_length=1200, verbose_name='Class number')),
                ('duration', models.CharField(max_length=1200, verbose_name='Duration')),
                ('duration_type', models.IntegerField(choices=[(1, 'Day'), (2, 'Week'), (3, 'Month')], null=True, verbose_name='Duration Type')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('status', models.IntegerField(choices=[(1, 'Enable'), (0, 'Disable')], verbose_name='Status')),
                ('class_capacity', models.IntegerField(verbose_name='Class capacity')),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_course', to='educlass.course', verbose_name='Class course')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='educlass.instructor', verbose_name='Instructor')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='educlass.room', verbose_name='Room')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Class',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='educlass.instructor'),
        ),
    ]
