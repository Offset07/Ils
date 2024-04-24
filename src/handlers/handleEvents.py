from highrise import *
from highrise.models import *
from src.eventHandle import start, join, chat, react, tips

async def handle_start(self, session_metadata: SessionMetadata) -> None:
    try:
        await start.on_start(self, session_metadata)
    except Exception as e:
        print(f"An Error Occured: {e}")

async def handle_join(bot, user: User) -> None:
    try:
        await join.on_join(bot, user)
    except Exception as e:
        print(f"An Error Occurred: {e}")

async def handle_chat(bot, user: User, message: str) -> None:
    try:
        await chat.on_chat(bot, user, message)
    except Exception as e:
        print(f"An Error Occured: {e}")

async def handle_reactions(bot, user: User, reaction: Reaction, receiver: User) -> None:
    try:
        await react.on_reaction(bot, user, reaction, receiver)
    except Exception as e:
        print(f"An Error Occured: {e}")

async def handle_tips(bot, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
    try:
        await tips.on_tip(bot, sender, receiver, tip)
    except Exception as e:
        print(f"An Error Occured: {e}")
