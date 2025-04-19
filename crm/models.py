import random
import uuid

from django.utils.translation import gettext_lazy as _

from accounts.models import *


class Course(models.Model):
    company = models.ForeignKey(Company, verbose_name=_('Course Company'), on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(MyUser, verbose_name=_('Course Author'), on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=1500, verbose_name=_("Course Name"))
    status = models.IntegerField(choices=CourseStatus, verbose_name=_("Course Status"), default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(choices=Currency, verbose_name=_('Currency'), null=True, max_length=5)
    duration = models.CharField(verbose_name=_("Duration"), null=True, max_length=1200)
    duration_type = models.IntegerField(choices=DurationType, verbose_name=_("Duration Type"), null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.id:
            super(Course, self).save(*args, **kwargs)
            self.slug = slugify(f"{self.name}-{self.id}")
            super(Course, self).save(*args, **kwargs)
        else:
            self.slug = slugify(f"{self.name}-{self.id}")
            super(Course, self).save(*args, **kwargs)


class Customers(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name='customers_company', null=True)
    customer_id = models.CharField(max_length=20, unique=True, editable=False, null=True, verbose_name=_('Customer ID'))
    first_name = models.CharField(_('First Name'), max_length=1500, )
    last_name = models.CharField(_('Last Name'), max_length=1500)
    phone_number = models.CharField(_('Mobile number'), max_length=1500)
    email = models.EmailField(_('Email'), max_length=1500)
    location = models.IntegerField(choices=COUNTRY_CITIES, verbose_name=_('Location'), null=True)
    stage = models.IntegerField(choices=STAGES, verbose_name=_('Stage'))
    course_or_trainings = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name=_('Course or Trainings'),
                                            null=True)
    gender = models.IntegerField(choices=GENDER, verbose_name=_('Gender'))
    next_step = models.IntegerField(choices=NEXT_STEP, verbose_name=_('Next Step'))
    status = models.IntegerField(choices=STATUS, verbose_name=_('Status'))
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, editable=False, null=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Customers, self).save(*args, **kwargs)
        if not self.customer_id:
            while True:
                random_number = random.randint(100000, 999999)
                new_customer_id = f"IC-{random_number}"
                if not Customers.objects.filter(customer_id=new_customer_id).exists():
                    self.customer_id = new_customer_id
                    break
        self.slug = "{}.{}".format(slugify(self.first_name + "-" + self.last_name), self.id)
        super(Customers, self).save(*args, **kwargs)


class UserCompany(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    company_id = models.CharField(max_length=20, unique=True, editable=False, null=True, verbose_name=_('Company ID'))
    name = models.CharField(max_length=1500, verbose_name=_('Company Name'))
    industry = models.IntegerField(choices=INDUSTRY_CHOICES, verbose_name=_('Industry'), null=True)
    first_name = models.CharField(max_length=1500, verbose_name=_('First Name'), blank=True)
    last_name = models.CharField(max_length=1500, verbose_name=_('Last Name'), null=True, blank=True)
    position = models.CharField(max_length=1500, verbose_name=_('Position'), blank=True)
    email = models.EmailField(_('Email'), max_length=1500, blank=True)
    mobile_number = models.CharField(_('Mobile Number'), max_length=15, blank=True)

    contract_number = models.CharField(_('Total contract'), max_length=50)
    sales = models.CharField(_('Total Sales'), max_length=255)
    slug = models.SlugField(unique=True, editable=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
        ordering = ['-id']

    def get_last_contact_person(self):
        return self.user_company_contact.order_by('-id').first()

    def save(self, *args, **kwargs):
        super(UserCompany, self).save(*args, **kwargs)
        if not self.company_id:
            while True:
                random_number = random.randint(100000, 999999)
                new_company_id = f"IC-{random_number}"
                if not UserCompany.objects.filter(company_id=new_company_id).exists():
                    self.company_id = new_company_id
                    break
        self.slug = "{}.{}".format(slugify(self.name), self.id)
        super(UserCompany, self).save(*args, **kwargs)


class ContactPerson(models.Model):
    user_company = models.ForeignKey(UserCompany, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='user_company_contact', verbose_name=_('Company'))
    first_name = models.CharField(max_length=1500, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=1500, verbose_name=_('Last Name'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=15, verbose_name=_('Phone'))
    position = models.CharField(max_length=1500, verbose_name=_('Position'))
    reg_date = models.DateField(auto_now_add=True, verbose_name=_('Registration Date'))
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_('Slug'), editable=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Contact Person')
        verbose_name_plural = _('Contact Persons')
        ordering = ['-id']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                str(self.id * 232421) if self.id else str(self.first_name))
        super(ContactPerson, self).save(*args, **kwargs)


class Order(models.Model):
    company = models.ForeignKey(Company, verbose_name=_('Company'), on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_owner')
    user_company = models.ForeignKey(UserCompany, on_delete=models.SET_NULL, null=True, verbose_name=_('User Company'),
                                     related_name='order')

    order_id = models.CharField(max_length=20, unique=True, editable=False, null=True, verbose_name=_('Order ID'))
    status = models.IntegerField(choices=ORDER_STATUS, verbose_name=_('Status'), null=True)
    contact_person = models.ForeignKey(ContactPerson, verbose_name=_('Contact Person'), on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='contact_person')
    course = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='course_orders')
    participants = models.CharField(max_length=1200, verbose_name=_('Participants'))
    order_date = models.DateField(auto_now_add=True, verbose_name=_('Order Date'), null=True)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2,null=True)
    total_amount = models.DecimalField(_('Total Amount'),null=True, blank=True, max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_('Slug'), null=True, editable=False)

    def __str__(self):
        return u'%s %s' % (self.user_company, self.order_id)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        if not self.order_id:
            while True:
                random_number = random.randint(100000, 999999)
                new_order_id = f"CO-{random_number}"
                if not Order.objects.filter(order_id=new_order_id).exists():
                    self.order_id = new_order_id
                    break

        self.slug = slugify(str(self.course.name) + '-' + str(self.order_id))
        super(Order, self).save(*args, **kwargs)


class Task(models.Model):
    company = models.ForeignKey(Company, verbose_name=_('Task Company'), on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(MyUser, verbose_name=_('Task Author'), on_delete=models.SET_NULL, null=True)
    task_id = models.CharField(max_length=20, unique=True, editable=False, null=True, verbose_name=_('Task ID'))
    title = models.CharField(max_length=1200, verbose_name=_('Title'))
    task_type = models.IntegerField(choices=TASK_TYPE, verbose_name=_('Task Type'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    deadline = models.DateTimeField(verbose_name=_('Due Date'))
    priority = models.IntegerField(choices=PRIORITY_LEVEL, verbose_name=_('Priority'))
    status = models.IntegerField(choices=TASK_STATUS, verbose_name=_('Task Status'))
    set_today = models.BooleanField(default=False, verbose_name=_('Set Today'))
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_('Slug'), null=True, editable=False)

    def __str__(self):
        return self.task_id

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
        if not self.task_id:
            while True:
                random_number = random.randint(100000, 999999)
                new_task_id = f"T-{random_number}"
                if not Task.objects.filter(task_id=new_task_id).exists():
                    self.task_id = new_task_id
                    break

        self.slug = slugify(str(self.task_id))
        super(Task, self).save(*args, **kwargs)


class CalendarEvent(models.Model):
    COLOR_CHOICES = (
        ('#007bff', 'Blue'),
        ('#28a745', 'Green'),
        ('#dc3545', 'Red'),
        ('#ffc107', 'Yellow'),
        ('#17a2b8', 'Cyan'),
        ('#6f42c1', 'Purple'),
        ('#fd7e14', 'Orange'),
        ('#e83e8c', 'Pink'),
        ('#20c997', 'Teal'),
        ('#343a40', 'Dark'),
        ('#6c757d', 'Gray'),
    )

    company = models.ForeignKey(Company, verbose_name=_('Task Company'), on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(MyUser, verbose_name=_('Task Author'), on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    event_type = models.IntegerField(choices=Event_Type, verbose_name=_('Event Type'), null=True)
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Location'))
    attendees = models.EmailField(blank=True, null=True, verbose_name=_('Attendees email'))
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, blank=True)

    def save(self, *args, **kwargs):
        if not self.color:
            self.color = random.choice([color[0] for color in self.COLOR_CHOICES])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Calendar')
        verbose_name_plural = _('Calendars')
        ordering = ['-id']


class Notification(models.Model):
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sender', verbose_name='Sender')
    receiver = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='receiver', verbose_name='Receiver')
    type = models.IntegerField(choices=NotificationType, verbose_name='Type', null=True)
    action_type = models.IntegerField(choices=NotificationActionType, verbose_name='Type', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    is_read = models.BooleanField(default=False, verbose_name='is Read')
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug", editable=False)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Notification, self).save(*args, **kwargs)


class NotificationView(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='viewnotification',
                                     verbose_name="Notification")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='viewuser', verbose_name="User")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    def __str__(self):
        return ('%s') % (self.id)

    class Meta:
        verbose_name = "Notification view"
        verbose_name_plural = "Notifications view"
        ordering = ('-created',)
