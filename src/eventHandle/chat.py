from highrise import *
from highrise.models import *
from src.handlers.handleCommands import command_handler
from config.config import loggers, config, emotes
from src.commands.emtn import emoting
import logging, re

# Set up the logger for chat messages
log_file = "lib\playerChat.log"
chat_logger = logging.getLogger("chat_logger")  # Create a new logger with the name "chat_logger"
chat_logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
chat_logger.addHandler(file_handler)


async def on_chat(self: BaseBot, user: User, message: str) -> None:
    if loggers.messages:
        msg = f"{user.username}: {message}"
        print(msg)  # This will still print the message to the console
        chat_logger.info(msg)  # This will log the message to the playerChat.log file
    
    for cmd, emote in emotes.command_emote_pairs:
        match = re.match(f"{cmd}\s+@(\w+)", message)
        await emoting(self, match, cmd, emote, user, message)

    if message.lstrip().startswith(config.prefix):
        await command_handler(self, user, message)