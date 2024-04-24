from highrise import *
from highrise.models import *
from config.config import permissions, config
import asyncio

async def goback(self: BaseBot, user: User, message: str)-> None:

    if message.lower().startswith("/goback"):
        room_permissions = await self.highrise.get_room_privilege(user.id)
        if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
            coords = config.coordinates
            await self.highrise.walk_to(Position(coords['x'], coords['y'], coords['z'], coords['facing']))