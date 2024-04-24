from highrise import *
from highrise.models import *
from config.config import permissions, config
import asyncio, time, random


async def help(self: BaseBot, user: User, message: str)-> None:
    await self.highrise.chat("These are the bot commands!\n\n/emote-name for using emote\n/list for getting the list of all emote commands\n/floor <floor number> for using elevator\nUsage: /floor 1")