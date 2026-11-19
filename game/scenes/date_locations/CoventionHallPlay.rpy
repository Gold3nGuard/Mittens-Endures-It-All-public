label CoventionHallPlay:

    if gametime < theater_closing_time:

        image amity happy smaller facing left covention = Image("images/amity happy smaller facing left@3.5.webp", oversample=3)
        scene bg covention hall entrance day
        show amity happy smaller facing left covention:
            xalign 0.99
            yalign 0.95

        jump CoventionHallPlayDay

    else:

        image amity happy smaller facing left covention = Image("images/amity happy smaller facing left@3.5.webp", oversample=3)
        scene bg covention hall entrance night
        show amity happy smaller facing left covention:
            xalign 0.99
            yalign 0.95

        jump CoventionHallPlayNight

label CoventionHallPlayDay:


    # This replaces the movie theatre
    $ currentLocation = Location.COVENTION_HALL_PLAY
    "We arrive at the Covention Hall to watch a play."

    "Since this location is not implemented yet, we immediately hopped back on Stringbean"
    jump GoToBroom

label CoventionHallPlayNight:

    $ currentLocation = Location.DARK_COVENTION
    call itsclosed(character.mainCharacter, girlfriend) from _call_itsclosed

    menu:
        "Try to break in with your key" if item_covention_key in inventory:
            call updateTimeAndStats() from _call_updateTimeAndStats_5
            call break_covention() from _call_break_covention
        "Continue":
            call updateTimeAndStats() from _call_updateTimeAndStats_8

    jump GoToBroom

label break_covention():

    "break_covention() has not been implemented yet!"
    return