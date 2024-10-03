label GoToBroom:

    # (not on broomride yet) Have gf show need as you leave current venue
    call showNeed(character.mainCharacter, girlfriend, changeVenue = True) from _call_showNeed
    "I haven't made art for this next part yet, so use your imagination lol"

    jump BroomRide

label BroomRide:

    # TODO: Change the scene
    $ currentLocation = Location.BROOM
    "We're flying on Stringbean..."

    menu whereToGo:

        "Where shall we fly to next?"

        "Just fly around":
            call updateTimeAndStats() from _call_updateTimeAndStats
            call showNeed(character.mainCharacter, girlfriend) from _call_showNeed_1
            jump JustFlyAround

        "Give her something to drink" if inventory.hasUniversalConsumableLiquid:
            call updateTimeAndStats() from _call_updateTimeAndStats_1
            call universalConsumableLiquidMenuChoices() from _call_universalConsumableLiquidMenuChoices
            call showNeed(character.mainCharacter, girlfriend) from _call_showNeed_2
        
        "(NOT IMPLEMENTED YET!) Go to the Covention Hall to watch a play":
            call updateTimeAndStats() from _call_updateTimeAndStats_2
            jump CoventionHallPlay # equiv to movie

        "(NOT IMPLEMENTED YET!) Go to Grimgrub's Pub":
            call updateTimeAndStats() from _call_updateTimeAndStats_3
            jump GrimgrubsPub # equiv to bar

        "(NOT IMPLEMENTED YET!) Go to the Grom Tree":
            call updateTimeAndStats() from _call_updateTimeAndStats_4
            jump GromTree # equiv to nightclub

label JustFlyAround:

    jump BroomRide