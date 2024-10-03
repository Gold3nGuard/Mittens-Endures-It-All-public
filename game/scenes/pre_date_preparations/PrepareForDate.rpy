label PrepareForDate:

    # Back to Luz's room
    scene bg luzs room

    # Display Luz
    show luz happy:
        xalign 0.5
        yalign 0.9

    # Play Grom music
    queue music "audio/enchanting_grom_fright.mp3"
    
    # Luz's narration
    "I wonder how I should prepare for my date tonight?..."

    # Prepare for the date tonight 
    menu:

        "Go to the Bonesborough Market Place":
            call updateTimeAndStats() from _call_updateTimeAndStats_29
            jump BonesboroughMarketPlace

        "Phone a friend" if buddyCalled == buddyCalledOptions.NOBODY:
            call updateTimeAndStats() from _call_updateTimeAndStats_30
            jump PhoneFriend

        "Call [girlfriend.name]":
            call updateTimeAndStats() from _call_updateTimeAndStats_31
            jump CallAmity

        "Pickup [girlfriend.name]":
            call updateTimeAndStats() from _call_updateTimeAndStats_32
            jump PickupAmity