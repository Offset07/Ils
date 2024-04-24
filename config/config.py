class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = '65e77b8c73aeeb403b0e95da'
    botName = 'STEP.11'
    ownerName = 'daniel_offset'
    roomName = 'change-me'
    coordinates = {
        'x': 13.0,
        'y': 7.5,
        'z': 13.5,
        'facing': 'FrontRight'
    }
    floor1 = {
        'x': 11.5,
        'y': 0,
        'z': 2.5,
        'facing': 'FrontRight'
    }
    floor2 = {
        'x': 8.5,
        'y': 9.5,
        'z': 5.5,
        'facing': 'FrontRight'
    }
    floor3 = {
        'x': 7.5,
        'y': 16.5,
        'z': 5.5,
        'facing': 'FrontRight'
    }


class loggers:
    # The following settings are related to events. Each event log can be enabled or disabled. Note that turning these off will not affect their usage in the game.
    SessionMetadata = True
    cmdChat = True
    messages = True
    whispers = True
    joins = True
    leave = True
    tips = True
    emotes = False
    reactions = False
    userMovement = False

class emotes:
    command_emote_pairs = [
        ("/model", "emote-model"),
        ("/dont start now", "dance-tiktok2"),
        ("/russian dance", "dance-russian"),
        ("/teleport", "emote-teleporting"),
        ("/curtsy", "emote-curtsy"),
        ("/lets go shopping", "dance-shoppingcart"),
        ("/greedy", "emote-greedy"),
        ("/flex", "emoji-flex"),
        ("/sing along", "idle_singing"),
        ("/pennys dance", "dance-pennywise"),
        ("/bow", "emote-bow"),
        ("/snowball fight", "emote-snowball"),
        ("/confused", "emote-confused"),
        ("/charging", "emote-charging"),
        ("/floating", "emote-float"),
        ("/frog hop", "emote-frog"),
        ("/enthused", "idle-enthusiastic"),
        ("/grave dance", "dance-weird"),
        ("/lambi pose", "emote-superpose"),
        ("/sword fight", "emote-swordfight"),
        ("/do the worm", "emote-snake"),
        ("/viral groove", "dance-tiktok9"),
        ("/shuffle dance", "dance-tiktok10"),
        ("/cursing", "emoji-cursing"),
        ("/raise the roof", "emoji-celebrate"),
        ("/emote cute", "emote-cute"),
        ("/telekinesis", "emote-telekinesis"),
        ("/energy ball", "emote-energyball"),
        ("/maniac", "emote-maniac"),
        ("/snow angel", "emote-snowangel"),
        ("/sweating", "emote-hot"),
        ("/kpop dance", "dance-blackpink"),
        ("/flirty wave", "emote-lust"),
        ("/cutey", "emote-cutey"),
        ("/dance", "idle-dance-casual"),
        ("/pose 1", "emote-pose1"),
        ("/pose 3", "emote-pose3"),
        ("/pose 5", "emote-pose5"),
        ("/pose 7", "emote-pose7"),
        ("/pose 8", "emote-pose8"),
        ("/gagging", "emoji-gagging"),
        ("/savage dance", "dance-tiktok8"),
        ("/say so dance", "idle-dance-tiktok4"),
        ("/fashion", "emote-fashionista"),
        ("/gravity", "emote-gravity"),
        ("/uwu", "idle-uwu")
    ]


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Your position could not be determined."
    invalidPlayer = "{user} is not in the room."
    invalidUser = "User {user} is not found."
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."


class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['']
    moderators = ['']
    exception = ["daniel_offset"]


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '64e99ff81188da64f8889bfa'
    token = '4b8b677b307f3e356bdaccb659b4e62b6a1c4eb85d7137117095bef82d971bbb'
