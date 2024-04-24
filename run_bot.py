from highrise.__main__ import *
import time
from config.config import authorization

bot_file_name = "main"
bot_class_name = "Bot"
room_id = authorization.room
bot_token = authorization.token

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)


while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occourred: {e}")
        time.sleep(5)
