from highrise import *
from highrise.models import *
from config.config import permissions

async def equip(self: BaseBot, user: User, message: str)-> None:

    room_permissions = await self.highrise.get_room_privilege(user.id)
    if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
        if message.lower().startswith("/equip "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.send_whisper(user.id, "Invalid command. Usage: /equip <item_name>")
                return

            item_name = " ".join(parts[1:])  # Combine all parts after "/equip" to get the full item name.


            item_response = await self.webapi.get_items(item_name=item_name)
            if not item_response.items:
                await self.highrise.send_whisper(user.id, f"Item '{item_name}' not found.")
                return

            # Assume we only take the first matching item found in the response.
            item_data = item_response.items[0]

            # Extract the category from the item ID
            category = item_data.category

            new_item = Item(
                type='clothing',
                amount=1,
                id=item_data.item_id,
                account_bound=False,
                active_palette=-1  # Set the desired palette here or modify the value as needed.
            )

            # Get the current outfit of the bot.
            outfit_response = await self.highrise.get_my_outfit()
            current_outfit = outfit_response.outfit

            # Find the index of the item category that matches the new item's category.
            replace_index = None
            for i, item in enumerate(current_outfit):
                if item.id.split('-')[0] == category:
                    replace_index = i
                    break

            if replace_index is not None:
                # Preserve the original active_palette if not specified in the new item.
                if new_item.active_palette == -1:
                    new_item.active_palette = current_outfit[replace_index].active_palette

                # Replace the item in the current outfit with the new item.
                current_outfit[replace_index] = new_item

                # Apply the updated outfit.
                resp = await self.highrise.set_outfit(outfit=current_outfit)
                await self.highrise.send_whisper(user.id, f"Successfully equipped {item_name}.\nstatus: {resp}")
            else:
                # Add the new item to the current outfit.
                current_outfit.append(new_item)

                # Apply the updated outfit.
                resp = await self.highrise.set_outfit(outfit=current_outfit)
                await self.highrise.send_whisper(user.id, f"Successfully equipped {item_name}.\nstatus: {resp}")
