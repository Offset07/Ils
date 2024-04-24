from highrise import *
from highrise.models import *
from config.config import loggers, config


async def on_reaction(self: BaseBot, user: User, reaction: Reaction, receiver: User) -> None:
    if loggers.reactions:
        print(f"{user.username} send {reaction} to {receiver.username}")
    if user.id == config.botID:
        return  # Ignore reactions initiated by the bot itself
    if receiver.id == config.botID:
        await self.highrise.react(reaction, user.id)
    else:
        await self.highrise.chat(f" @{user.username} send {reaction} to @{receiver.username}")