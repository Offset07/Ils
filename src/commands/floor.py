from highrise import *
from highrise.models import *
from config.config import permissions, config
import asyncio, time, random


async def floor(self: BaseBot, user: User, message: str)-> None:

    if message.lower().startswith("/floor"):
        parts = message.split()
        num = parts[1]
        num = int(num)
        if not num:
            await self.highrise.send_whisper(user.id, f"Invalid command. Usage: /floor <Floor Number>\nFloor can be (1, 2, 3)")
            return
        else:
            if num == 1:
                coords = config.floor1
                await self.highrise.teleport(user.id, Position(coords['x'], coords['y'], coords['z'], coords['facing']))
            if num == 2:
                coords = config.floor2
                await self.highrise.teleport(user.id, Position(coords['x'], coords['y'], coords['z'], coords['facing']))
            if num == 3:
                coords = config.floor3
                await self.highrise.teleport(user.id, Position(coords['x'], coords['y'], coords['z'], coords['facing']))