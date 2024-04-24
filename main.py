from highrise import *
from highrise.models import *
from src.handlers.handleEvents import handle_start, handle_chat, handle_join, handle_reactions, handle_tips
from config.config import authorization
import time
from highrise import __main__
from asyncio import run as arun

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token

class Bot(BaseBot):
    start_time = time.time()
    
    def __init__(self):
        super().__init__()

    async def on_start(self: BaseBot, session_metadata: SessionMetadata) -> None:
        await handle_start(self, session_metadata)

    async def on_chat(self: BaseBot, user: User, message: str) -> None:
        await handle_chat(self, user, message)

    async def on_user_join(self: BaseBot, user: User) -> None:
        await handle_join(self, user)

    async def on_tip(self: BaseBot, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        await handle_tips(self, sender, receiver, tip)

    async def on_reaction(self: BaseBot, user: User, reaction: Reaction, receiver: User) -> None:
        await handle_reactions(self, user, reaction, receiver)

    async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)


if __name__ == "__main__":
    room_id = authorization.room
    token = authorization.token

    if not room_id or not token:
        print("Please set the room ID and token in the authorization config.")
    else:
        arun(Bot().run(room_id, token))