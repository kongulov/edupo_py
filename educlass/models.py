from django.db import models
import random
import uuid

from django.utils.translation import gettext_lazy as _

from accounts.helper import slugify
from accounts.options.options import *
from accounts.models import *


class Category(models.Model):
    company = models.ForeignKey(Company, verbose_name=_('Course Company'), on_delete=models.SET_NULL, null=True,related_name='category_company')
    author = models.ForeignKey(MyUser, verbose_name=_('Course Author'), on_delete=models.SET_NULL, null=True,related_name='category_user')
    name = models.CharField(max_length=1200, verbose_name="Category name")
    slug = models.SlugField(unique=True, editable=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = "{}.{}".format(slugify(self.name), self.id)
        super(Category, self).save(*args, **kwargs)


class Course(models.Model):
    author = models.ForeignKey(MyUser, verbose_name=_('Course Author'), on_delete=models.SET_NULL, null=True,related_name='course_author')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name=_('Company'), related_name='course_company')
    name = models.CharField(max_length=1200, verbose_name="Class name")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Category',
                                 related_name='course_category')
    duration = models.CharField(max_length=1200, verbose_name="Duration")
    duration_type = models.IntegerField(choices=DurationType, verbose_name=_("Duration Type"), null=True)
    description = models.TextField(max_length=1200, verbose_name="Description")
    level = models.IntegerField(choices=CourseLevel, verbose_name='Level')
    status = models.IntegerField(choices=CourseStatus, verbose_name='Status')
    slug = models.SlugField(unique=True, editable=False, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)
        self.slug = "{}.{}".format(slugify(self.name), self.id)
        super(Course, self).save(*args, **kwargs)
