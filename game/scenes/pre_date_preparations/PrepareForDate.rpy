label TardyTextMessageFromGirlfriend(girlfriend):
    # Girlfriend texts you if you're late
    if not girlfriend.tardy_text_sent and gametime >= Time(hour=19, minute=0):
        $ renpy.notify("{b}Penstagram{/b}\n" + f"{girlfriend.pet_name}: Heyy~ are you on your way?")
        $ girlfriend.tardy_text_sent = True
    return

label PrepareForDate:

    # Back to Luz's room
    scene bg luzs room

    # Display Luz
    show luz happy:
        xalign 0.5
        yalign 0.9

    # Play Grom music
    queue music "audio/enchanting_grom_fright.mp3"

    # Update Location Flag
    $ currentLocation = Location.PRE_DATE
    
    # Luz's narration
    "I wonder how I should prepare for my date tonight?..."

    # Text notification from Amity if you're late
    call TardyTextMessageFromGirlfriend(girlfriend) from _call_TardyTextMessageFromGirlfriend

    # Prepare for the date tonight 
    menu prep_for_date_menu:

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