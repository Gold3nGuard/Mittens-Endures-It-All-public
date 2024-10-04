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

    call displayNeed() from _call_displayNeed_2

    # TODO: add check if she's wet...

    return

label spurtedHerself(mainCharacter, girlfriend):

    $ girlfriend.pees(gametime = gametime, amount = 50)
    $ spurt_threshold -= 0.1 * spurt_threshold
    $ girlfriend.spurted = True

    $ randInt = renpy.random.randint(0,5)
    "[spurtQuote[randInt]]"

    call displayNeed() from _call_displayNeed_3

    menu:
        "Ask her if she peed herself.":
            # call updateTimeAndStats() from _call_updateTimeAndStats_33
            call askSpurted(mainCharacter, girlfriend) from _call_askSpurted

        "Continue ...":
            pass
            # call updateTimeAndStats() from _call_updateTimeAndStats_34

    return


label checkWetHerself(mainCharacter, girlfriend):
    # Originally `wetherself`
    # Check if girlfriend's bladder is full enough to lose control, then execute the actions.

    # Check if she loses control
    if (girlfriend.bladder > girlfriend.bladder_lose):

        # Indicate that gf is currently wetting
        $ girlfriend.now_wetting = True

        # Define her wetting actions
        $ wetQuote = ["Suddenly, " + girlfriend.name + " squeals and then gasps!",
            "Suddenly, " + girlfriend.name + " freezes in place and her face turns bright red.",
            girlfriend.name + " gasps and grabs at her pussy.",
            girlfriend.name + " squeals and doubles over.",
            girlfriend.name + " suddenly gasps and her face turns red.",
            girlfriend.name + " suddenly shudders and her face turns red."]

        # Display her wetting action
        $ randInt = renpy.random.randint(0,5)
        "[wetQuote[randInt]]"

        # Check if she spurts rather than wets
        if ((randomChoice(spurt_threshold)) and 
            (currentLocation != Location.THE_HOT_TUB) and
            (not girlfriend.spurted)
        ):
            call spurtedHerself(mainCharacter, girlfriend) from _call_spurtedHerself
        
        else:
            $ spurt_threshold = 50

            # menu:
            #     "Continue...":
            #         pass

            call wetHerself2(mainCharacter, girlfriend) from _call_wetHerself2

            # "Suddenly, you hear the loud hissing as her bladder uncontrollably empties itself."
            # $ girlfriend.pees(gametime = gametime)

            # $ randInt = renpy.random.randint(0,5)
            # girlfriend "[embarQuote[randInt]]"

    return


label wetHerself2(mainCharacter, girlfriend):

    if currentLocation == Location.BROOM:
        "[girlfriend.name] suddenly and frantically looks around."
        girlfriend "Oh no! [mainCharactersPalisman]!"
        "She arches her back, lifting her ass off the staff."
        "You hear the loud hissing as her bladder uncontrollably empties itself."
        "You feel drops of her urine as the wind blows the cascading liquid in your direction."
        "It feels like a warm rain drizzling on your back."
        $ girlfriend.pees(gametime = gametime)
        $ girlfriend.wet_legs = True 
        $ girlfriend.wet_her_panties = True
        $ girlfriend.wet_the_car = True
       
    # seatbelt doesn't make sense when they're on a staff
    # elif currentLocation == Location.MAKEOUT_LOCATION:
    #     pass 
    elif currentLocation == Location.THE_HOT_TUB:
        "[girlfriend.name] suddenly stiffens and whispers:"
        girlfriend "Oh no!" 
        $ girlfriend.pees(gametime = gametime)
        "She sighs and slumps back in the tub, lost in her own little world for a minute or so."
        "There's complete silence aside from her heavy breathing and some crickets in the distance."
    else:
        "Suddenly, you hear the loud hissing as her bladder uncontrollably empties itself."
        $ girlfriend.pees(gametime = gametime)
        $ girlfriend.wet_legs = True 
        $ girlfriend.wet_her_panties = True

        $ randInt = renpy.random.randint(0,5)
        girlfriend "[embarQuote[randInt]]"


    call wetHerself3(mainCharacter, girlfriend) from _call_wetHerself3
    return

label wetHerself3(mainCharacter, girlfriend):

    if currentLocation == Location.BROOM:
        girlfriend "I'm {b}so{/b} sorry about [mainCharactersPalisman]..."
        "She settles unhappily feeling her soaked, squishy pants on the damp staff."
        $ girlfriend.shyness += 20
        $ girlfriend.mood -= 20
    elif currentLocation == Location.THE_HOT_TUB:
        girlfriend "I'm {b}so{/b} sorry... I just couldn't hold it."
        "The faint scent of her urine rises from the water."
        girlfriend "I peed in the tub."
        $ girlfriend.shyness += 20
        $ girlfriend.mood -= 20 
    else:
        if ((girlfriend.panty_colour_name is not None) and
            (girlfriend.shyness < 70)
        ):
            # TODO: This part is supposed to be dependent on jeans vs skirt. 
            # I decided not to implement for now.  
            "She takes off her jeans and slowly peels her soaked [girlfriend.panty_colour_name] panties down her dripping legs, holding them daintily between her thumb and forefinger."

            if (girlfriend.mood > 40):
                "[girlfriend.name] hands you the wet panties, soaked with her fragrant urine."
                girlfriend "Is there someplace you can put these?"
                # TODO: Add wet panties to inventory system
                $ girlfriend.panty_colour_name = None # She's now not wearing panties!
        elif (girlfriend.panty_colour_name is None):
            girlfriend "Good thing I wasn't wearing panties, I guess."
        
        $ randInt = renpy.random.randint(0,5)
        girlfriend "[triesToDryCrotchQuote[randInt]]"

        menu OfferTowelsOrPanties:

            "Offer her paper towels" if item_roll in inventory:
                call givePaperTowels() from _call_givePaperTowels 

            "Offer her a clean pair of panties" if item_panties in inventory:
                call giveDryPanties() from _call_giveDryPanties

            "Continue...":
                call updateTimeAndStats() from _call_updateTimeAndStats_33

    $ girlfriend.now_wetting = False
    return

label givePaperTowels():
    
    girlfriend "Thanks!"
    "She wipes the pee from her legs and pussy."
    $ girlfriend.mood += 5 
    $ inventory.attemptUseItem(item_roll)
    $ girlfriend.wet_legs = False 

    menu OfferPanties:

        "Offer her a clean pair of panties" if item_panties in inventory:
            call giveDryPanties() from _call_giveDryPanties_1

        "Continue...":
            call updateTimeAndStats() from _call_updateTimeAndStats_34

    return 

label giveDryPanties():

    girlfriend "Where did you get those?"
    "She slips into the clean panties with a smile."
    $ inventory.attemptUseItem(item_panties)
    $ girlfriend.panty_colour_name = "sexy"

    if (girlfriend.wet_legs):
        "Her still dripping pussy dampens the crotch of the new panties."
    else:
        $ girlfriend.mood += 5
    $ girlfriend.wet_legs = False 

    menu:
        "Continue...":
            call updateTimeAndStats() from _call_updateTimeAndStats_39

    return 