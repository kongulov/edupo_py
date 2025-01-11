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
