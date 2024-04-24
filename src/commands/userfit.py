from highrise import *
from highrise.models import *
from config.config import permissions

async def userfit(self: BaseBot, user: User, message: str)-> None:

    room_permissions = await self.highrise.get_room_privilege(user.id)
    if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
        if message.lower().startswith("/userfit "):
            args = message.split(' ')
            if len(args) > 1:
                name = args[1]
                if name.startswith('@'):
                    name = name[1:]
                fetch = await self.highrise.get_room_users()
                index = next((i for i, item in enumerate(fetch.content) if item[0].username == name), -1)
                if index != -1:
                    target = fetch.content[index][0]
                    inventory = await self.highrise.get_user_outfit(target.id)
                    for item in inventory.outfit: 
                        await self.highrise.send_whisper(user.id, item.id)