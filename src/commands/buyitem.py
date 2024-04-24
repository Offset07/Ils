from highrise import *
from highrise.models import *
from config.config import permissions

async def buyitem(self: BaseBot, user: User, message: str)-> None:

    room_permissions = await self.highrise.get_room_privilege(user.id)
    if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
        if message.lower().startswith("/buyitem "):
            parts = message.split(" ")
            if len(parts) != 2:
                await self.highrise.send_whisper(user.id, "Invalid command")
                return
            item_id = parts[1]
            try:
                response = await self.highrise.buy_item(item_id)
                await self.highrise.send_whisper(user.id, f"Item bought: {response}")
            except Exception as e:
                await self.highrise.send_whisper(user.id, f"Error: {e}")