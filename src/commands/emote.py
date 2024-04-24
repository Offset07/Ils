from highrise import *
from highrise.models import *
from config.config import permissions, emotes
import random

async def emote(self: BaseBot, user: User, message: str)-> None:

    if message.lower().startswith("/emote"):
        random_cmd, random_emote = random.choice(emotes.command_emote_pairs)
        await self.highrise.send_emote(random_emote, user.id)