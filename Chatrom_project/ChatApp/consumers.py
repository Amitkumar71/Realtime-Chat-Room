import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from ChatApp.models import *

class ChatConsumer(AsyncWebsocketConsumer):
     
     connected_users={}

     async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        self.username = self.scope['url_route']['kwargs']['username']
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

               # Adds user to connected_users
        if self.room_name not in self.connected_users:
            self.connected_users[self.room_name] = set()
        self.connected_users[self.room_name].add(self.username)


                # Send updated user list to all clients in the room
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'user_list_changed',
                'users': list(self.connected_users[self.room_name])
            }
        )

     async def user_list_changed(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': event['users']
        }))
        print(f"Connected to {self.room_name}")

     async def disconnect(self, close_code):
        self.connected_users[self.room_name].remove(self.username)
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
    

                # Send updated user list to all clients in the room
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'user_list_changed',
                'users': list(self.connected_users[self.room_name])
            }
        )

        async def user_list_changed(self, event):
            await self.send(text_data=json.dumps({
                'type': 'user_list',
                'users': event['users']
            }))
     async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json

        # print(message)
        event={
            'type': 'send_message',
            'message': message,
        }

        await self.channel_layer.group_send(self.room_name, event)

     async def send_message(self, event):
        data = event['message']
        await self.create_message(data=data)
        response_data = {
            'sender': data['sender'],
            'message': data['message']
        }
        await self.send(text_data=json.dumps({'message': response_data}))
     @database_sync_to_async
     def create_message(self, data):
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(room=get_room_by_name, sender=data['sender'], message=data['message'])
            new_message.save()