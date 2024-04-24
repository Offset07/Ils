from highrise import *
from highrise.models import *
from config.config import permissions

async def eqinv(self: BaseBot, user: User, message: str)-> None:

    room_permissions = await self.highrise.get_room_privilege(user.id)
    if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
        if message.lower().startswith("/eqinv "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.send_whisper(user.id, "Invalid command. Usage: /eqinv <category> [<number>]")
                return

            category = parts[1].lower()

            try:
                # Get the inventory items.
                inventory_response = await self.highrise.get_inventory()
                inventory_items = inventory_response.items

                # Filter the items of the specified category.
                category_items = [item for item in inventory_items if item.id.split('-')[0] == category]

                if not category_items:
                    await self.highrise.send_whisper(user.id, f"No items found in the inventory for category '{category}'.")
                    return

                # Check if a number is provided to equip a specific item.
                if len(parts) == 3:
                    try:
                        item_number = int(parts[2]) - 1  # Adjust for 0-based indexing.
                        if 0 <= item_number < len(category_items):
                            # Get the selected item.
                            selected_item = category_items[item_number]

                            # Get the current outfit of the bot.
                            outfit_response = await self.highrise.get_my_outfit()
                            current_outfit = outfit_response.outfit

                            # Find the index of the item category that matches the selected item's category.
                            replace_index = None
                            for i, item in enumerate(current_outfit):
                                if item.id.split('-')[0] == category:
                                    replace_index = i
                                    break

                            # If the category is not in the current outfit, add the selected item to the outfit.
                            if replace_index is None:
                                current_outfit.append(selected_item)

                            # Preserve the original active_palette if not specified in the selected item.
                            if selected_item.active_palette == -1 and replace_index is not None:
                                selected_item.active_palette = current_outfit[replace_index].active_palette

                            # Replace the item in the current outfit with the selected item.
                            if replace_index is not None:
                                current_outfit[replace_index] = selected_item

                            # Apply the updated outfit.
                            resp = await self.highrise.set_outfit(outfit=current_outfit)
                            await self.highrise.send_whisper(user.id, f"Successfully equipped item {item_number+1} of category '{category}'.\nstatus: {resp}")
                        else:
                            await self.highrise.send_whisper(user.id, f"Invalid item number. Please choose a number between 1 and {len(category_items)}.")
                    except ValueError:
                        await self.highrise.send_whisper(user.id, "Invalid item number. Please provide a valid number.")
                else:
                    # Print all items of the category with numbers.
                    item_list = "\n".join([f"{i+1}. {item.id}" for i, item in enumerate(category_items)])
                    await self.highrise.send_whisper(user.id, f"Items of category '{category}':\n{item_list}")

            except Exception as e:
                await self.highrise.send_whisper(user.id, f"Error: {e}")