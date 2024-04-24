from highrise import *
from highrise.models import *
from config.config import permissions

async def unequip(self: BaseBot, user: User, message: str)-> None:

    room_permissions = await self.highrise.get_room_privilege(user.id)
    if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
        if message.lower().startswith("/unequip "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.send_whisper(user.id, "Invalid command. Usage: /unequip <category>")
                return

            category = parts[1].lower()
            # Get the current outfit of the bot.
            outfit_response = await self.highrise.get_my_outfit()
            current_outfit = outfit_response.outfit

            # Find the index of the item category that matches the specified category.
            unequip_index = None
            for i, item in enumerate(current_outfit):
                if item.id.split('-')[0] == category:
                    unequip_index = i
                    break

            if unequip_index is not None:
                # Remove the item from the current outfit.
                unequipped_item = current_outfit.pop(unequip_index)

                # Apply the updated outfit.
                resp = await self.highrise.set_outfit(outfit=current_outfit)
                await self.highrise.send_whisper(user.id, f"Successfully unequipped {category}.\nstatus: {resp}")
            else:
                await self.highrise.send_whisper(user.id, f"No item of category '{category}' found in the outfit.")