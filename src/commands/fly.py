from highrise import *
from highrise.models import *
from config.config import permissions
import asyncio, time, random


async def fly(self: BaseBot, user: User, message: str)-> None:
    room_permissions = await self.highrise.get_room_privilege(user.id)
    if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
        if message.lower().startswith("/fly"):
            parts = message.split() #seperating the text
            if len(parts) < 3:
                await self.highrise.send_whisper(user.id, "Invalid command. Usage: /fly <x> <y> <z>")
                return
            x = parts[1] #seperating the x coordinate
            y = parts[2] #seperating the y coordinate
            z = parts[3] #seperating the z coordinate
            if not x or not y or not z:
                await self.highrise.send_whisper(user.id, f"Invalid command. Usage: /fly <x> <y> <z>")
            else:
                await self.highrise.teleport(user.id, Position(x,y,z))
        else:
            await self.highrise.chat(f"Sorry! But Only room moderators can use the /fly command @{user.username}")