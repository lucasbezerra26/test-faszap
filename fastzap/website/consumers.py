#
# import json
# from asgiref.sync import async_to_sync, sync_to_async
#
# from channels.generic.websocket import AsyncWebsocketConsumer
from fastzap.chat.models import *
from channels.db import database_sync_to_async

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def create_message_attendance(self, **kargs):
        return Message.objects.create(**kargs).save()

    @database_sync_to_async
    def get_attendance(self):
        return Attendance.objects.get(id=int(self.room_name))\

    @database_sync_to_async
    def close_attendance(self):
        self.attendance.status = "Finalizado"
        self.attendance.save()

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['attendance']
        self.room_group_name = 'chat_%s' % self.room_name
        self.attendance = await self.get_attendance()

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
            self.close_attendance()

            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        type_message = text_data_json['type_message']
        bot = text_data_json['bot']

        await self.create_message_attendance(
            attendance=self.attendance,
            text=message,
            type=type_message,
            status="enviado"
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'type_message': type_message,
                'status': "enviado"
            }
        )

        if bot == True:
            if "menu" == message:
                new_message = "1 - Hamburger \n 2 - pizza"
                await self.create_message_attendance(
                    attendance=self.attendance,
                    text=new_message,
                    type="recebido",
                    status="enviado"
                )

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': new_message,
                        'type_message': type_message,
                        'status': "enviado"
                    }
                )

            if "1" == message or "2" == message:
                new_message = "ok"
                await self.create_message_attendance(
                    attendance=self.attendance,
                    text=new_message,
                    type="recebido",
                    status="enviado"
                )

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': new_message,
                        'type_message': type_message,
                        'status': "enviado"
                    }
                )



    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        type_message = event['type_message']
        status = event['status']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'type_message': type_message,
            'status': status,
        }))
