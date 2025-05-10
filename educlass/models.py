from django.db import models
import random
import uuid

from django.utils.translation import gettext_lazy as _

from accounts.helper import slugify
from accounts.options.options import *
from accounts.models import *


class Category(models.Model):
    company = models.ForeignKey(Company, verbose_name=_('Course Company'), on_delete=models.SET_NULL, null=True,
                                related_name='category_company')
    author = models.ForeignKey(MyUser, verbose_name=_('Course Author'), on_delete=models.SET_NULL, null=True,
                               related_name='category_user')
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


class Instructor(models.Model):
    author = models.ForeignKey(MyUser, verbose_name=_('Course Author'), on_delete=models.SET_NULL, null=True,
                               related_name='instructor_author')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name=_('Company'),
                                related_name='instructor_company')
    full_name = models.CharField(max_length=1200, verbose_name="Full name")
    slug = models.SlugField(unique=True, editable=False, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Instructor')
        verbose_name_plural = _('Instructors')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Instructor, self).save(*args, **kwargs)
        self.slug = "{}.{}".format(slugify(self.full_name), self.id)
        super(Instructor, self).save(*args, **kwargs)


class Room(models.Model):
    author = models.ForeignKey(MyUser, verbose_name=_('Course Author'), on_delete=models.SET_NULL, null=True,
                               related_name='room_author')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name=_('Company'),
                                related_name='room_company')
    name = models.CharField(max_length=1200, verbose_name="Room name")
    slug = models.SlugField(unique=True, editable=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)
        self.slug = "{}.{}".format(slugify(self.name), self.id)
        super(Room, self).save(*args, **kwargs)


class Course(models.Model):
    author = models.ForeignKey(MyUser, verbose_name=_('Course Author'), on_delete=models.SET_NULL, null=True,
                               related_name='course_author')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name=_('Company'),
                                related_name='course_company')
    name = models.CharField(max_length=1200, verbose_name="Class name")
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
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


class Class(models.Model):
    author = models.ForeignKey(MyUser, verbose_name=_('Course Author'), on_delete=models.SET_NULL, null=True,
                               related_name='class_author')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name=_('Company'),
                                related_name='class_company')
    name = models.CharField(max_length=1200, verbose_name="Class name")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='class_course',
                               verbose_name="Class course")
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, verbose_name='Instructor')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, verbose_name='Room')
    number = models.CharField(max_length=1200, verbose_name='Class number')
    duration = models.CharField(max_length=1200, verbose_name="Duration")
    duration_type = models.IntegerField(choices=DurationType, verbose_name=_("Duration Type"), null=True)
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    status = models.IntegerField(choices=CourseStatus, verbose_name='Status')
    class_capacity = models.IntegerField(verbose_name="Class capacity")
    slug = models.SlugField(unique=True, editable=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Class')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Class, self).save(*args, **kwargs)
        self.slug = "{}.{}".format(slugify(self.name), self.id)
        super(Class, self).save(*args, **kwargs)
