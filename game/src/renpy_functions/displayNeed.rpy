# Import statements
init python:
    from random import random

# Constants for this module
define TWO_TURNS_FROM_WETTING = 60

# Every label here needs a return statement and should only be called to, not jumped to!
label showNeed(mainCharacter, girlfriend, changeVenue = False):
    # Displays a series of texts that describes how your girlfriend is feeling about her bladder.
    # Original game is much more complicated than this. TODO: replicate original game system later
    # call displayGottaGoVocalization()
    # call interpBladder()
    # call displayNeed()
    # call checkWetHerself(mainCharacter, girlfriend)

    #  How this should work:
    #  Outer IFs determine LOCATION/SCENARIO.
    #  Inner IFs determine pee request parameters
    #  Upper IFs are emergencies

    # === CONTROL FLOW === #
    # If she's within 2 turns of wetting and not too shy,
    # (+ she's mentioned needing to pee before), 
    # she will vocalize no matter what.
    if ((girlfriend.bladder >= girlfriend.bladder_lose - TWO_TURNS_FROM_WETTING) and
        (girlfriend.shyness < 90) and 
        (girlfriend.broke_ice == False)
        ):
        call displayGottaGoVocalization() from _call_displayGottaGoVocalization

    # If she's within 2 turns of wetting, it'll look obvious
    elif ((girlfriend.bladder >= girlfriend.bladder_lose - TWO_TURNS_FROM_WETTING) and
        (girlfriend.shyness >= 90) 
        ):
        "{i}[girlfriend.name] looks so desperate for the toilet like she is about to wet herself any moment, but she doesn't say anything{/i}."

    # If you're about to leave a location, she'll almost always ask
    elif (changeVenue):
        if ((girlfriend.bladder >= girlfriend.bladder_emergency) or 
            (girlfriend.bladder >= girlfriend.bladder_need and girlfriend.shyness < 70)
        ):
            if (girlfriend.turns_to_wait_before_asking == 0):
                girlfriend "Hey [character.mainCharacter.name], before we go..."
                $ girlfriend.turns_to_wait_before_asking = 4
                call displayGottaGoVocalization() from _call_displayGottaGoVocalization_1
            else:
                "[girlfriend.name] looks like she really has to pee, but she doesn't say anything."
                if (girlfriend.ask_hold_it_counter > 0):
                    "After all, you did ask her to hold it."

    # Generic instances of her asking to use the bathroom
    # She'll try to hold it if you flirted with somebody at that location
    elif (girlfriend.turns_to_wait_before_asking == 0 and 
        not(girlfriend.external_flirt)
    ):

        # Shyness < 80 is enough to ask if she's having a bladder emergency
        if ((girlfriend.shyness < 80) and 
            (girlfriend.bladder > girlfriend.bladder_emergency)
        ):
            $ girlfriend.turns_to_wait_before_asking = 6
            call displayGottaGoVocalization() from _call_displayGottaGoVocalization_2

        # Shyness < 60 is enough to ask if she's merely needing to pee bad
        elif ((girlfriend.shyness < 60) and 
            (girlfriend.bladder > girlfriend.bladder_need)
        ):
            $ girlfriend.turns_to_wait_before_asking = 10
            call displayGottaGoVocalization() from _call_displayGottaGoVocalization_3

        # Shyness < 40 and she's letting you know at 1st urge.
        elif ((girlfriend.shyness < 40) and 
            (girlfriend.bladder > girlfriend.bladder_urge)
        ):
            $ girlfriend.turns_to_wait_before_asking = 12
            call displayGottaGoVocalization() from _call_displayGottaGoVocalization_4

        # Otherwise, she may or may not show symptoms of having to go
        elif (random() * girlfriend.bladder_lose < girlfriend.bladder):
            call displayNeed() from _call_displayNeed
        
    # Otherwise, she may or may not show symptoms of having to go
    elif (random() * girlfriend.bladder_lose < girlfriend.bladder):
        call displayNeed() from _call_displayNeed_1

    # The original doesn't have this here... TODO: figure out what i wanna do with this function
    call checkWetHerself(character.mainCharacter, girlfriend) from _call_checkWetHerself

    return

label displayNeed():
    # Displays text that describes how your girlfriend is reacting to the state of her bladder.
    $ randInt = renpy.random.randint(0,5)
    if girlfriend.peeUrgencyLevel == PeeUrgencyLevel.FIRST_URGE:
        "[needUrge[randInt]]"
    elif girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_NEED:
        "[needNeed[randInt]]"
    elif girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_EMERGENCY:
        "[needEmer[randInt]]"
    elif (girlfriend.peeUrgencyLevel.value >= PeeUrgencyLevel.BLADDER_LOSE.value
    ):
        "[needLose[randInt]]"
    
    return

label interpBladder():
    # Displays narration text that shows your internal thoughts about seeing your girlfriend's potty dance.
    $ randInt = renpy.random.randint(0,5)
    if girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_NEED:
        "[interpNeed[randInt]]"
    elif girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_EMERGENCY:
        "[interpEmer[randInt]]"
    elif (girlfriend.peeUrgencyLevel.value >= PeeUrgencyLevel.BLADDER_LOSE.value
    ):
        "[interpLose[randInt]]"
    
    return

label displayGottaGoVocalization():
    # Originally `displaygottavoc`
    # Prints text of girlfriend vocalizing that she hopes to find a bathroom soon.


    # For cases when Amity is at PeeUrgencyLevel.BLADDER_LOSE, have the program
    # include her voice audio from Wing It Like Witches saying "I GOTTA GO!"
    if (girlfriend.broke_ice and girlfriend.name == "Amity"):
        if ((girlfriend.bladder >= girlfriend.bladder_lose) or
            ((girlfriend.bladder >= girlfriend.bladder_emergency) and 
                (randomChoice(80))
            ) or
            ((girlfriend.bladder >= girlfriend.bladder_need) and 
                (randomChoice(40))
            )
        ):
            voice "audio/Amity_I_Gotta_Go.mp3"
            Amity "I GOTTA GO!!!"
            voice sustain

    # If you've asked gf to hold it, and she feels an urge to pee, 
    # there's a 30% chance that she'll ask anyways. 
    if ((girlfriend.ask_hold_it_counter > 0) and
        (girlfriend.bladder > girlfriend.bladder_urge) and 
        (randomChoice(30))
    ):
        $ randInt = renpy.random.randint(0,5)
        girlfriend "[wantHold[randInt]]"
        voice sustain

    # If this is the first time she's vocalized her need 
    # and she didn't agree to hold it before you picked her up, 
    # then she'll be embarrassed to vocalize her need
    if ((girlfriend.bladder >= girlfriend.bladder_need) and
        not(girlfriend.broke_ice) and
        (girlfriend.pre_hold == False)
    ):
        "{i}[girlfriend.name] looks embarrassed.{/i}"
        voice sustain
        girlfriend "Titan, I'm sorry. I don't know how to say this to you, but..."
        voice sustain


    # Vocalization during broom ride
    # TODO: In first iteration of game, I've decided to ignore the option
    # of included submissive dialogue. If I decide in the future to add that
    # in, this is where to add it in. See `displaygottavoc()` for original implementation
    if currentLocation == Location.BROOM:
        $ randInt = renpy.random.randint(0,5)
        if (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.FIRST_URGE):
            girlfriend "[broomUrgeGottaGoVocalization[randInt]]"
        elif (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_NEED):
            girlfriend "[broomNeedGottaGoVocalization[randInt]]"
        elif (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_EMERGENCY):
            girlfriend "[broomEmerGottaGoVocalization[randInt]]"
        elif (girlfriend.peeUrgencyLevel.value >= PeeUrgencyLevel.BLADDER_LOSE.value
        ):
            # "Amity looks like she's about to LUZ bladder control!"
            # voice sustain
            girlfriend "[broomLoseGottaGoVocalization[randInt]]"
            voice sustain

    # Vocalization everywhere else
    else:
        $ randInt = renpy.random.randint(0,5)
        if (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.FIRST_URGE):
            girlfriend "[urgeGottaGoVocalization[randInt]]"
        elif (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_NEED):
            girlfriend "[needGottaGoVocalization[randInt]]"
        elif (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_EMERGENCY):
            girlfriend "[emerGottaGoVocalization[randInt]]"
        elif (girlfriend.peeUrgencyLevel.value >= PeeUrgencyLevel.BLADDER_LOSE.value
        ):
            # "Amity looks like she's about to LUZ bladder control!"
            # voice sustain
            girlfriend "[loseGottaGoVocalization[randInt]]"
            voice sustain


    # Update gotta_go_flag and broke_ice flag.
    # TODO: Ensure that these flags actually get updated when they're supposed to
    # I think gotta_go_flag is fine
    # But there's a possibility that broke_ice gets toggled when it's not supposed to
    # She needs to have vocalized that she needs to pee...
    if (girlfriend.bladder >= girlfriend.bladder_need): 
        $ girlfriend.gotta_go_flag = True

    # I think this should be toggled to true at the end everytime the function is called
    $ girlfriend.broke_ice = True 
    # if (girlfriend.bladder >= girlfriend.bladder_urge): 
    #     $ girlfriend.broke_ice = True

    return

# TODO: Implement wetHerself() and spurtedHerself()

label askSpurted(mainCharacter, girlfriend):

    mainCharacter "Did you just pee yourself?"
    $ randInt = renpy.random.randint(0,5)
    "[spurtQuote[randInt]]"
    $ randInt = renpy.random.randint(0,5)
    girlfriend "[spurtDenyQuote[randInt]]"
    return

label spurtedHerself(mainCharacter, girlfriend):

    $ girlfriend.pees(50)

    $ randInt = renpy.random.randint(0,5)
    "[spurtQuote[randInt]]"

    menu:
        "Ask her if she peed herself.":
            call updateTimeAndStats() from _call_updateTimeAndStats_33
            call askSpurted(mainCharacter, girlfriend) from _call_askSpurted

        "Continue ...":
            call updateTimeAndStats() from _call_updateTimeAndStats_34

    return


label checkWetHerself(mainCharacter, girlfriend):
    # Check if girlfriend's bladder is full enough to lose control, then execute the actions.

    #  She loses control
    $ wetQuote = ["Suddenly, " + girlfriend.name + " squeals and then gasps!",
        "Suddenly, " + girlfriend.name + " freezes in place and her face turns bright red.",
        girlfriend.name + " gasps and grabs at her pussy.",
        girlfriend.name + " squeals and doubles over.",
        girlfriend.name + " suddenly gasps and her face turns red.",
        girlfriend.name + " suddenly shudders and her face turns red."]


    if (girlfriend.bladder > girlfriend.bladder_lose):

        call spurtedHerself(mainCharacter, girlfriend) from _call_spurtedHerself

        $ randInt = renpy.random.randint(0,5)
        "[wetQuote[randInt]]"
        "Suddenly, you hear the loud hissing as her bladder uncontrollably empties itself."
        $ girlfriend.pees()

        $ randInt = renpy.random.randint(0,5)
        girlfriend "[embarQuote[randInt]]"

    return
