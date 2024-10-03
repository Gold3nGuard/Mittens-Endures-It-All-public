# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define character.Luz = Character("Luz", color="#d79260")
default currentLocation = Location.PRE_DATE
# define character.mainCharacter = character.Luz

# init python:
#     from src.InventorySystem import Inventory
#     from src.GirlfriendStats import Girlfriend


# The game starts here.
label start:

    # Show inventory and snails icon
    show screen hud
    show screen snails

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg luzs room

    # Play Grom music
    play music "audio/enchanting_grom_fright.mp3"

    # Display Luz
    show luz happy:
        xalign 0.5
        yalign 0.9

    # Initialize girlfriend stats and display
    $ girlfriend = Amity # Alias between two saved vars is ok. This is the girlfriend object, not girlfriend the Character()
    define character.mainCharacter = character.Luz 
    $ character.girlfriend = character.Amity # This is girlfriend the Character()

    show screen girlfriend_stats

    # Initialize dynamic variales


    # $ renpy.notify("This is a notification!")

    # call updateTimeAndStats()
    # "[gametime.display()]"
    # call updateTimeAndStats()
    # "[gametime.display()]"
    # call updateTimeAndStats()
    # "[gametime.display()]"
    # call updateTimeAndStats()
    # "[gametime.display()]"
    # call updateTimeAndStats()
    # "[gametime.display()]"
    # call updateTimeAndStats()
    # "[gametime.display()]"
    # call updateTimeAndStats()
    # "[gametime.display()]"


    # # Initialize Inventory
    # $ inventory.add_item_without_purchase(item_diur)
    # $ inventory.add_item_without_purchase(item_hbmp)
    # $ inventory.add_item_without_purchase(item_hbmp)
    # $ inventory.add_item_without_purchase(item_hbmp)
    # $ inventory.add_item_without_purchase(item_rose)
    # $ inventory.add_item_without_purchase(item_rose)
    # $ inventory.add_item_without_purchase(item_rose)
    # $ inventory.add_item_without_purchase(item_diam)
    # $ inventory.add_item_without_purchase(item_diam)
    # "Inventory initialized with \{[str(inventory)]\}"


    

    # # Output a Python string as narration
    # $ line = inventory.list_items()
    # "[line]"

    # Output a Python string as dialogue
    # Luz "[line]"

    # Luz's initial narration
    Luz "Today marks the sixth anniversary of when Amity and I started dating!"
    Luz "I am so excited for tonight!"
    Luz "I recently found out that both Amity and I share a kink. An omorashi kink..."
    Luz "She's still quite shy about it though."
    Luz "Despite that, I know she frequently holds her pee until she's bursting during our dates in secret."
    Luz "It's not that hard to figure out when she's all squirmy by the end of the night after all..."
    Luz "But I wonder if I can convince her to do more tonight?"
    
    jump PrepareForDate

    # This ends the game.
    return
