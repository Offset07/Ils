from highrise import *
from highrise.models import *
import os
import importlib.util

async def command_handler(self:BaseBot, user: User, message: str):
    parts = message.split(" ")
    command = parts[0][1:]
    functions_folder = "src/commands"
    if not os.path.exists(functions_folder):
        print("The 'src\\commands' directory does not exist.")
        await self.highrise.send_whisper(user.id, "The 'src\\commands' directory does not exist.")
        return
    # Check if the function exists in the module
    for file_name in os.listdir(functions_folder):
        if file_name.endswith(".py"):
            module_name = file_name[:-3]  # Remove the '.py' extension
            module_path = os.path.join(functions_folder, file_name)
            
            # Load the module
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Check if the function exists in the module
            if hasattr(module, command) and callable(getattr(module, command)):
                function = getattr(module, command)
                await function(self, user, message)
    
    # If no matching function is found
    return
