from django.db.models import Q

from crm.models import Notification


def extras(request):
    context = {}
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(Q(receiver=request.user) | Q(sender=request.user))[
                        :10]
        context['notification_list'] = notifications

        notification_count = Notification.objects.filter(Q(receiver=request.user) | Q(sender=request.user),
                                                         is_read=False)
        context['notification_count'] = notification_count.count()

    return context
