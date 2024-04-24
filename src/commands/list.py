from highrise import *
from highrise.models import *
from config.config import permissions, emotes, config

async def list(self: BaseBot, user: User, message: str)-> None:

    if message.lower().startswith("/list"):
        conversation_id = f"1_on_1:{user.id}:{config.botID}" #replace bot id
        content = f"This is the list of emote commands!\n"
        for cmd, emote in emotes.command_emote_pairs:
            content += cmd + "\n"

        await self.highrise.send_message(conversation_id, content, "text")