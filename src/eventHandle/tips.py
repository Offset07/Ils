from highrise import *
from highrise.models import *
from config.config import loggers, config
import random


async def on_tip(self: BaseBot, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
    if loggers.tips:
        print(f"{sender.username} tipped {receiver.username} {tip.amount} {tip.type}!")
    if receiver.id == config.botID:
            await self.highrise.chat(f"Thanks for giving {tip.amount} gold to me @{sender.username} !")
            options = ['heart', 'thumbs', 'wink']
            random_choice = random.choice(options)
            await self.highrise.react(random_choice, sender.id)
    else:
        await self.highrise.chat(f" @{sender.username} tipped {tip.amount} gold to @{receiver.username} !")
