from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.helper import slugify
from accounts.options.options import *

# from ckeditor.fields import RichTextField


USER_MODEL = settings.AUTH_USER_MODEL


class Company(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                              related_name="company_owner")
    name = models.CharField(max_length=1500, verbose_name="Company name")
    company_logo = models.ImageField(verbose_name=_('Company logo'), upload_to='companies/', null=True, blank=True)
    address = models.CharField(max_length=1500, verbose_name="Company address", null=True)
    email = models.EmailField(verbose_name=_('Email'), null=True)
    phone_number = models.CharField(max_length=12000, verbose_name="Phone number", null=True)
    website = models.CharField(max_length=1200, verbose_name="Website", null=True, blank=True)
    package_company = models.IntegerField(
        choices=PACKAGES, verbose_name="Company Package", null=True, blank=True)
    tax_id = models.CharField(max_length=1200, verbose_name="Tax id")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['-reg_date']


class MyUser(AbstractBaseUser, PermissionsMixin):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Company", related_name="user_company",
                                null=True)
    username = models.CharField(_('username'), null=True, max_length=100, unique=False)
    first_name = models.CharField(_('Ad'), max_length=255, blank=True, )
    last_name = models.CharField(_('Soyad'), max_length=255, blank=True)
    user_image = models.ImageField(_('Profil şəkli'), upload_to='user_cdn_profie', blank=True, null=True,
                                   max_length=5000)
    activation_code = models.CharField(max_length=120, blank=True, null=True)
    password_reset_code = models.CharField(max_length=120, blank=True, null=True)

    email = models.EmailField(_('email address'), unique=True, max_length=255, blank=False)

    slug = models.SlugField(unique=True, editable=False, null=True)

    usertype = models.IntegerField(choices=USERTYPE, verbose_name="İstifadəçi növü", null=True)
    phone_number = models.CharField(max_length=1200, verbose_name="Telefon nömrəsi", blank=True, null=True)

    description = models.TextField(_('Ətraflı məlumat'), null=True)
    adress = models.CharField(_('Ünvan'), max_length=5000, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Hesab'
        verbose_name_plural = 'Hesablar'
        ordering = ['-id']

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)
        self.slug = "{}.{}".format(slugify(self.first_name + "-" + self.last_name), self.id)
        super(MyUser, self).save(*args, **kwargs)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_avatar(self):
        if self.user_image:
            return self.user_image.url
        else:
            return "/static/assets/m-student.png"
