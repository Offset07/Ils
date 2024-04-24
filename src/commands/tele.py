from highrise import *
from highrise.models import *
from config.config import permissions

async def tele(self: BaseBot, user: User, message: str) -> None:
    room_permissions = await self.highrise.get_room_privilege(user.id)
    if room_permissions.moderator or room_permissions.designer or user.username in permissions.exception:
        if message.startswith('/tele'):
            # Split the message into parts using whitespace as a separator
            parts = message.split()

            if len(parts) < 4:
                # Incorrect number of arguments, inform the user about the correct usage
                await self.highrise.send_whisper(user.id, "Usage: /tele <@username> <x> <y> <z>")
                return

            _, username, x, y, z = parts

            # Remove the "@" symbol if present in the provided username
            if username.startswith('@'):
                username = username[1:]

            # Extract the user IDs from the room
            response = await self.highrise.get_room_users()
            users = [content[0] for content in response.content]  # Extract the user objects

            # Search for the user object matching the provided username
            target_user = None
            for u in users:
                if u.username == username:
                    target_user = u
                    break

            if target_user is None:
                # User not found, inform the user
                await self.highrise.send_whisper(user.id, f"User '{username}' not found.")
                return

            try:
                # Teleport the user to the specified coordinates
                await self.highrise.teleport(user_id=target_user.id, dest=Position(float(x), float(y), float(z)))
                await self.highrise.send_whisper(user.id, f"Teleported {username} to ({x}, {y}, {z}).")
            except Exception as e:
                print(e)
                await self.highrise.send_whisper(user.id, f"Error teleporting {username}: {str(e)}")
