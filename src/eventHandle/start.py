from highrise import *
from highrise.models import *
from src.eventHandle import cmdChat
from config.config import config, loggers
import asyncio


async def on_start(self: BaseBot, session_metadata: SessionMetadata) -> None:
    if loggers.SessionMetadata:
        rate_limits = session_metadata.rate_limits
        formatted_rate_limits = ', '.join(
            str(value) for value in rate_limits.values())
        print(f"Bot ID: {session_metadata.user_id}\nRate Limits: {formatted_rate_limits}\nConnection ID: {session_metadata.connection_id}\nSDK Version: {session_metadata.sdk_version}")

    coords = config.coordinates
    await self.highrise.walk_to(Position(coords['x'], coords['y'], coords['z'], coords['facing']))
    print(f"{config.botName} is now ready.")

    if loggers.cmdChat:
        task = asyncio.create_task(cmdChat.read_and_process_commands(self))
        await task

