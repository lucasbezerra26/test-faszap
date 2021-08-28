
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from fastzap.chat.models import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['attendance']
        self.room_group_name = 'chat_%s' % self.room_name
        self.attendance = Attendance.objects.get(id=int(self.room_name))

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        self.attendance.status = "Finalizado"
        self.attendance.save()

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        type_message = text_data_json['type_message']
        print(message)
        message_object = Message.objects.create(
            attendance=self.attendance,
            text=message,
            type=type_message,
            status="enviado"
        )

        message_object.save()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'type_message': type_message,
                'status': message_object.status
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        type_message = event['type_message']
        status = event['status']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'type_message': type_message,
            'status': status,
        }))
