# Generated by Django 4.2 on 2025-02-23 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1500, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('position', models.CharField(max_length=1500, verbose_name='Position')),
                ('reg_date', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
                ('slug', models.SlugField(editable=False, max_length=150, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Contact Person',
                'verbose_name_plural': 'Contact Persons',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1500, verbose_name='Course Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Customer'), (2, 'Company'), (3, 'Order'), (4, 'Task'), (5, 'Calendar')], null=True, verbose_name='Type')),
                ('action_type', models.IntegerField(choices=[(1, 'Add'), (2, 'Edit')], null=True, verbose_name='Type')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('is_read', models.BooleanField(default=False, verbose_name='is Read')),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True, verbose_name='Slug')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='Receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(editable=False, max_length=20, null=True, unique=True, verbose_name='Company ID')),
                ('name', models.CharField(max_length=1500, verbose_name='Company Name')),
                ('industry', models.IntegerField(choices=[(1, 'Technology'), (2, 'Healthcare'), (3, 'Finance'), (4, 'Education'), (5, 'Retail'), (6, 'Manufacturing'), (7, 'Real Estate'), (8, 'Entertainment'), (9, 'Energy'), (10, 'Transportation'), (11, 'Telecommunications'), (12, 'Hospitality'), (13, 'Construction'), (14, 'Legal'), (15, 'Agriculture'), (16, 'Automotive'), (17, 'Aerospace'), (18, 'Pharmaceutical'), (19, 'Insurance'), (20, 'Media'), (21, 'Consumer Goods'), (22, 'Food & Beverage'), (23, 'Mining'), (24, 'Utilities'), (25, 'Non-profit'), (26, 'Environmental'), (27, 'Government'), (28, 'Sports'), (29, 'Arts & Culture'), (30, 'Security')], null=True, verbose_name='Industry')),
                ('first_name', models.CharField(blank=True, max_length=1500, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Last Name')),
                ('position', models.CharField(blank=True, max_length=1500, verbose_name='Position')),
                ('email', models.EmailField(blank=True, max_length=1500, verbose_name='Email')),
                ('mobile_number', models.CharField(blank=True, max_length=15, verbose_name='Mobile Number')),
                ('contract_number', models.CharField(max_length=50, verbose_name='Total contract')),
                ('sales', models.CharField(max_length=255, verbose_name='Total Sales')),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(editable=False, max_length=20, null=True, unique=True, verbose_name='Task ID')),
                ('title', models.CharField(max_length=1200, verbose_name='Title')),
                ('task_type', models.IntegerField(choices=[(1, 'Personal'), (2, 'Phone Call'), (3, 'Message'), (4, 'Email')], verbose_name='Task Type')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('deadline', models.DateTimeField(verbose_name='Due Date')),
                ('priority', models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], verbose_name='Priority')),
                ('status', models.IntegerField(choices=[(1, 'To Do'), (2, 'In Progress'), (3, 'Done')], verbose_name='Task Status')),
                ('set_today', models.BooleanField(default=False, verbose_name='Set Today')),
                ('slug', models.SlugField(editable=False, max_length=150, null=True, unique=True, verbose_name='Slug')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Task Author')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company', verbose_name='Task Company')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(editable=False, max_length=20, null=True, unique=True, verbose_name='Order ID')),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'Qualified'), (3, 'Processing'), (4, 'Postponed'), (5, 'Contracted'), (6, 'Rejected')], null=True, verbose_name='Status')),
                ('participants', models.CharField(max_length=1200, verbose_name='Participants')),
                ('order_date', models.DateField(auto_now_add=True, null=True, verbose_name='Order Date')),
                ('slug', models.SlugField(editable=False, max_length=150, null=True, unique=True, verbose_name='Slug')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_owner', to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company', verbose_name='Company')),
                ('contact_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_person', to='crm.contactperson', verbose_name='Contact Person')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_orders', to='crm.course', verbose_name='Course')),
                ('user_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='crm.usercompany', verbose_name='User Company')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NotificationView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewnotification', to='crm.notification', verbose_name='Notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewuser', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Notification view',
                'verbose_name_plural': 'Notifications view',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(editable=False, max_length=20, null=True, unique=True, verbose_name='Customer ID')),
                ('first_name', models.CharField(max_length=1500, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=1500, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=1500, verbose_name='Mobile number')),
                ('email', models.EmailField(max_length=1500, verbose_name='Email')),
                ('location', models.IntegerField(choices=[(1, 'Abşeron (Xırdalan şəhəri)'), (2, 'Ağcabədi'), (3, 'Ağdam (Quzanlı qəsəbəsi)'), (4, 'Ağdaş'), (5, 'Ağdərə'), (6, 'Ağstafa'), (7, 'Ağsu'), (8, 'Astara'), (9, 'Babək'), (10, 'Balakən'), (11, 'Beyləqan'), (12, 'Bərdə'), (13, 'Biləsuvar'), (14, 'Cəbrayıl'), (15, 'Cəlilabad'), (16, 'Culfa'), (17, 'Daşkəsən'), (18, 'Füzuli'), (19, 'Gədəbəy'), (20, 'Goranboy'), (21, 'Göyçay'), (22, 'Göygöl'), (23, 'Hacıqabul'), (24, 'Xaçmaz'), (25, 'Xızı'), (26, 'Xocalı'), (27, 'Xocavənd'), (28, 'İmişli'), (29, 'İsmayıllı'), (30, 'Kəlbəcər'), (31, 'Kəngərli (Qıvraq qəsəbəsi)'), (32, 'Kürdəmir'), (33, 'Qax'), (34, 'Qazax'), (35, 'Qəbələ'), (36, 'Qobustan'), (37, 'Quba'), (38, 'Qubadlı'), (39, 'Qusar'), (40, 'Laçın'), (41, 'Lerik'), (42, 'Lənkəran'), (43, 'Masallı'), (44, 'Neftçala'), (45, 'Oğuz'), (46, 'Ordubad'), (47, 'Saatlı'), (48, 'Sabirabad'), (49, 'Salyan'), (50, 'Samux'), (51, 'Sədərək (Heydərabad qəsəbəsi)'), (52, 'Siyəzən'), (53, 'Şabran'), (54, 'Şahbuz'), (55, 'Şamaxı'), (56, 'Şəki'), (57, 'Şəmkir'), (58, 'Şərur'), (59, 'Şuşa'), (60, 'Tərtər'), (61, 'Tovuz'), (62, 'Ucar'), (63, 'Yardımlı'), (64, 'Yevlax'), (65, 'Zaqatala'), (66, 'Zəngilan'), (67, 'Zərdab')], null=True, verbose_name='Location')),
                ('stage', models.IntegerField(choices=[(1, 'Lead'), (2, 'Qualified'), (3, 'Pending'), (4, 'Postponed'), (5, 'Contracted'), (6, 'Canceled'), (7, 'Rejected')], verbose_name='Stage')),
                ('course_or_trainings', models.IntegerField(choices=[(1, 'Course'), (2, 'Training')], verbose_name='Course/Trainings')),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], verbose_name='Gender')),
                ('next_step', models.IntegerField(choices=[(1, 'Follow up'), (2, 'Retarget'), (3, 'Closed')], verbose_name='Next Step')),
                ('status', models.IntegerField(choices=[(1, 'Student'), (2, 'Employed'), (3, 'Unemployed')], verbose_name='Status')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers_company', to='accounts.company')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='contactperson',
            name='user_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_company_contact', to='crm.usercompany', verbose_name='Company'),
        ),
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('event_type', models.CharField(choices=[(1, 'Meeting'), (2, 'Appointment'), (3, 'Event')], max_length=10, null=True, verbose_name='Event Type')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('attendees', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Attendees email')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('color', models.CharField(blank=True, choices=[('#007bff', 'Blue'), ('#28a745', 'Green'), ('#dc3545', 'Red'), ('#ffc107', 'Yellow'), ('#17a2b8', 'Cyan'), ('#6f42c1', 'Purple'), ('#fd7e14', 'Orange'), ('#e83e8c', 'Pink'), ('#20c997', 'Teal'), ('#343a40', 'Dark'), ('#6c757d', 'Gray')], max_length=10)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Task Author')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company', verbose_name='Task Company')),
            ],
            options={
                'verbose_name': 'Calendar',
                'verbose_name_plural': 'Calendars',
                'ordering': ['-id'],
            },
        ),
    ]
