from highrise import *
from highrise.models import *
import logging
from config.config import loggers


# Set up the logger for join messages
log_file = "lib\playerJoined.log"
join_logger = logging.getLogger("join_logger")  # Create a new logger with the name "join_logger"
join_logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
join_logger.addHandler(file_handler)


async def on_join(self: BaseBot, user: User) -> None:
    if loggers.joins:
        message = f"User joined: {user.username}:{user.id}"
        print(message)  # This will still print the message to the console
        join_logger.info(message)  # This will log the message to the playerJoined.log file

    await self.highrise.chat(f"\nWELCOME TO BESTIE CLUB Friend 💕 @{user.username}")
    
    await self.highrise.send_whisper(user.id, "Follow room owner @daniel_offset and @Silencieuxx\nUse /help in room chat for the commands or read my Bio.\n\n/If any problem then PM @DANIEL_OFFSET")

    content = f"For buying bots PM @DANIEL or PM him on discord daniel_offset"
    await self.highrise.send_whisper(user.id, content)