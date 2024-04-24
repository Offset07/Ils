from highrise import *
from highrise.models import *
import asyncio
from config.config import permissions, authorization

async def invite(self: BaseBot, user: User, message: str)-> None:

    if message.lower().startswith("/invite"):
        if user.username in permissions.exception:
            parts = message.split()
            num = parts[1]
            if not num:
                await self.highrise.send_whisper(user.id, f"Invalid command. Usage: /invite <Number of Users>")
            else:
                await self.highrise.send_whisper(user.id, "Starting invitation process!")
                task = asyncio.create_task(send_messages_to_conversations(self, authorization.room, user.id, num))
                await task

async def send_messages_to_conversations(self: BaseBot, roomid, userid, number):
    try:
        conversation_ids = []
        
        last_id = None
        while len(conversation_ids) < int(number):
            resp = await self.highrise.get_conversations(False, last_id)
            conversation_ids.extend([conversation.id for conversation in resp.conversations])
            if len(resp.conversations) == 20:
                last_id = resp.conversations[-1].id
            else:
                break
        
        # Send messages to each conversation ID
        for conversation_id in conversation_ids:
            await self.highrise.send_message(conversation_id, "shared a room invite", "invite", roomid)

        await self.highrise.send_whisper(userid, "Invitation Done!!")
    except Exception as e:
        print(f"An error occurred in send_messages_to_conversations: {e}")