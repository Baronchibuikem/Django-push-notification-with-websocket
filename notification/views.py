from django.shortcuts import render, HttpResponse
import requests

from channels.layers import get_channel_layer
import json

def index(request):
    return render(request, 'index.html', {'room_name': 'broadcast'})


from asgiref.sync import async_to_sync
def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': "Notification"
        }
    )
    return HttpResponse("Done")