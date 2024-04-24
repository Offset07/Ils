from highrise import *
from highrise.models import *
from config.config import permissions
import asyncio, time, random


async def em(self: BaseBot, user: User, message: str)-> None:

    if message.lower().startswith("/em"):
        if user.username in permissions.exception:
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.send_whisper(user.id, "Invalid command. Usage: /em <time in seconds>")
                return
            tm = parts[1].lower()
            tm = float(tm)
            
            await self.highrise.send_whisper(user.id, f"Emoting Bot for {tm/60} minutes")
            task = asyncio.create_task(emote_bot(self, tm))
            await task
    else:
        await self.highrise.send_whisper(user.id, "This is only Moderator command")

async def emote_bot(self: BaseBot, tm):
    start_time = time.time()
    tm = float(tm)
    while True:
        emoid = ["idle_singing", "dance-russian", "dance-tiktok8", "dance-tiktok2"]
        random_emote = random.choice(emoid)
        await self.highrise.send_emote(random_emote)
        await asyncio.sleep(8.5)
        
        if  (time.time() - start_time) >= tm:
            print(f"em Stopped, {tm/60} minutes over")
            break