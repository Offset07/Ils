from highrise import *
from highrise.models import *
from config.config import permissions

async def palette(self: BaseBot, user: User, message: str)-> None:

    room_permissions = await self.highrise.get_room_privilege(user.id)
    if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
        if message.lower().startswith("/palette "):
            parts = message.split(" ")
            if len(parts) < 3:
                await self.highrise.send_whisper(user.id, "Invalid command. Usage: /palette <category> <value>")
                return

            category = parts[1].lower()
            new_palette_value = int(parts[2])

            # Get the current outfit of the bot.
            outfit_response = await self.highrise.get_my_outfit()
            current_outfit = outfit_response.outfit

            # Find the index of the item category that matches the specified category.
            category_index = None
            for i, item in enumerate(current_outfit):
                if item.id.split('-')[0] == category:
                    category_index = i
                    break

            if category_index is not None:
                # Update the active_palette value for the item category.
                current_outfit[category_index].active_palette = new_palette_value

                # Apply the updated outfit.
                resp = await self.highrise.set_outfit(outfit=current_outfit)
                await self.highrise.send_whisper(user.id, f"Successfully updated active_palette for category '{category}' to {new_palette_value}.\nstatus: {resp}")
            else:
                await self.highrise.send_whisper(user.id, f"No item of category '{category}' found in the outfit.")