from highrise import *
from highrise.models import *
import importlib.util

async def reload(self: BaseBot, user: User, message: str) -> None:
    args = message.split()  # Split the message into command and arguments
    if len(args) != 2:
        await self.highrise.send_whisper(user.id, 'Invalid args.\nExample: /reload <commandName>')
        return

    category_name = args[0].lower()
    command_name = args[1].lower()

    try:
        """ # Get the existing module corresponding to the command
        command_module = self.commands.get(command_name)
        if not command_module:
            await self.highrise.send_whisper(user.id, f'Command "{command_name}" not found')
            return """

        # Get the file path of the module
        module_path = f'src/commands/{command_name}.py'

        # Use importlib to reload the module
        spec = importlib.util.spec_from_file_location(command_name, module_path)
        new_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(new_module)

        """ # Update the commands dictionary with the new module
        self.commands[command_name] = new_module """

        await self.highrise.send_whisper(user.id, f'Command "{command_name}" has been reloaded')

    except Exception as e:
        await self.highrise.send_whisper(user.id, f'Error reloading "{command_name}" command: {str(e)}')

# Usage: Call this function when you receive the "/reload <commandName>" message
# Example:
# await reload(self, user, "/reload command_name_to_reload")
