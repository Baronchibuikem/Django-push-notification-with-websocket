from notification.models import BroadcastNotification

def notifications(request):
    all_notifications = BroadcastNotification.objects.all()
    print(all_notifications, '-------------')
    return {
        'notifications': all_notifications
    }