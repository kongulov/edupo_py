from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from accounts.models import *
from accounts.options.options import *
from crm.models import *


class Faq(models.Model):
    title = models.CharField(max_length=1200, verbose_name="Sual")
    content = RichTextField(config_name='default', verbose_name="Cavab")
    place = models.IntegerField(verbose_name="Sıra nömrəsi", null=True)
    draft = models.BooleanField(default=True, verbose_name="Saytda yayımlansın?")

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
        ordering = ['place']


class Support(models.Model):
    company = models.ForeignKey(Company, verbose_name=_('Company'), on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(MyUser, verbose_name=_('Author'), on_delete=models.SET_NULL, null=True)

    ticket_id = models.CharField(max_length=20, unique=True, editable=False, null=True, verbose_name=_('Ticket ID'))
    title = models.CharField(max_length=1200, verbose_name="Subject")
    content = RichTextField(config_name='default', verbose_name="Content")
    ticket_type = models.IntegerField(choices=TicketType, verbose_name='Type')
    status = models.IntegerField(choices=TicketStatusType, verbose_name='Status')
    created = models.DateTimeField(auto_now_add=True
                                   , verbose_name='Created date')
    file = models.FileField(upload_to='support_files/', verbose_name='Attachment',blank=True)
    priority = models.IntegerField(choices=TICKET_PRIORITY_LEVEL, verbose_name='Priority')
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_('Slug'), null=True, editable=False)

    def __str__(self):
        return self.ticket_id

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super(Support, self).save(*args, **kwargs)
        if not self.ticket_id:
            while True:
                random_number = random.randint(100000, 999999)
                new_ticket_id = f"TK-{random_number}"
                if not Support.objects.filter(ticket_id=new_ticket_id).exists():
                    self.ticket_id = new_ticket_id
                    break
        self.slug = slugify(str(self.ticket_id))
        super(Support, self).save(*args, **kwargs)


class SupportTicketMessage(models.Model):
    ticket = models.ForeignKey(Support, on_delete=models.CASCADE, related_name='messages', verbose_name=_('Ticket'))
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name=_('Sender'))
    message = models.TextField(verbose_name=_('Message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    file = models.FileField(upload_to='ticket_messages/', blank=True, null=True, verbose_name=_('Attachment'))

    def __str__(self):
        return f"Message from {self.sender} in {self.ticket.ticket_id}"

    class Meta:
        ordering = ['created_at']
