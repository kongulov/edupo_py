import random

from django.utils.translation import gettext_lazy as _

from accounts.models import *


class Customers(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name='customers_company', null=True)
    customer_id = models.CharField(max_length=20, unique=True, editable=False, null=True, verbose_name=_('Customer ID'))
    first_name = models.CharField(_('First Name'), max_length=1500, )
    last_name = models.CharField(_('Last Name'), max_length=1500)
    phone_number = models.CharField(_('Mobile number'), max_length=1500)
    email = models.EmailField(_('Email'), max_length=1500)
    location = models.IntegerField(choices=COUNTRY_CITIES, verbose_name=_('Location'), null=True)
    stage = models.IntegerField(choices=STAGES, verbose_name=_('Stage'))
    course_or_trainings = models.IntegerField(choices=PRODUCT, verbose_name=_('Course/Trainings'))
    gender = models.IntegerField(choices=GENDER, verbose_name=_('Gender'))
    next_step = models.IntegerField(choices=NEXT_STEP, verbose_name=_('Next Step'))
    status = models.IntegerField(choices=STATUS, verbose_name=_('Status'))
    price = models.DecimalField(_('Price'), max_digits=1000000000, decimal_places=1)
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


class Course(models.Model):
    name = models.CharField(max_length=1500, verbose_name=_("Course Name"))
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)
        self.slug = slugify(str(self.name))
        super(Course, self).save(*args, **kwargs)


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
    COLOR_CHOICES = [
        ('#007bff', 'Blue'),  # Primary
        ('#28a745', 'Green'),  # Success
        ('#dc3545', 'Red'),  # Danger
    ]

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='#007bff')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Calendar')
        verbose_name_plural = _('Calendars')
        ordering = ['-id']
