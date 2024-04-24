from highrise import *
from highrise.models import *
from config.config import permissions
import asyncio
import time
from datetime import datetime, timedelta
from main import Bot

async def uptime(self: BaseBot, user: User, message: str)-> None:

    if message.lower().startswith("/uptime"):
        reply = await get_uptime(self)
        await self.highrise.chat(reply)

async def get_uptime(self):
    current_time = time.time()
    uptime = current_time - Bot.start_time

    # Convert uptime to timedelta object for easier calculations
    uptime_timedelta = timedelta(seconds=uptime)

    # Extract different time components
    days = uptime_timedelta.days
    hours, remainder = divmod(uptime_timedelta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Create a human-readable uptime string
    uptime_string = await format_time_component(days, "days")
    uptime_string += " " + await format_time_component(hours, "hours")
    uptime_string += " " + await format_time_component(minutes, "minutes")
    uptime_string += " " + await format_time_component(seconds, "seconds")
    uptime_string = uptime_string.strip()

    return f"Uptime: {uptime_string}"

async def format_time_component(value, unit):
    if value > 0:
        if value == 1:
            unit = unit[:-1]  # Remove plural form if the value is 1
        return f"{value} {unit}"
    return ""