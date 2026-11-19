# This module is for various interactions you can have with your girlfriend asking her about her need to pee
define CLOSED_AFTER_DARK_LOCATIONS = [Location.DARK_BAR, Location.DARK_COVENTION, Location.DARK_CLUB]
define MAX_P_STORY = 8
default pstorycounter = renpy.random.randint(1,MAX_P_STORY) - 1

label askPeeFollowUpQuestions(girlfriend):

    # I combined multiple bits of code from the original, 
    # most of them came from the function preventpee()
    # This label is called from the label displayGottaGoVocalization from the module displayNeed.rpy

    menu askPeeFollowUpQuestionsMenu:

        "Ask her to share her pee desperation experiences" if (((girlfriend.shyness < 50) and (girlfriend.bladder > girlfriend.bladder_need)) or (girlfriend.bladder > girlfriend.bladder_emergency)):
            call updateTimeAndStats() from _call_updateTimeAndStats_40
            call pStory(girlfriend) from _call_pStory

        # Ask to hold prompts

        "Deny her request to use the toilet. (NOT IMPLEMENTED)" if (girlfriend.gotta_go_flag and girlfriend.is_submissive):
            call updateTimeAndStats() from _call_updateTimeAndStats_41
            call holdits() from _call_holdits

        "Ask her to hold it in." if (girlfriend.gotta_go_flag and (not girlfriend.is_submissive)):
            call updateTimeAndStats() from _call_updateTimeAndStats_42
            call holdIt() from _call_holdIt

        # Special peeing requests based on venue

        "Ask her not to leave you alone. (NOT IMPLEMENTED)" if currentLocation == Location.CURRENTLY_DANCING:
            call updateTimeAndStats() from _call_updateTimeAndStats_43
            "3"

        "Tell her it would be sexy if you could watch. (NOT IMPLEMENTED)" if (currentLocation in CLOSED_AFTER_DARK_LOCATIONS):
            call updateTimeAndStats() from _call_updateTimeAndStats_44
            "4"

        "Tell her she can go, but not in the restrooms. (NOT IMPLEMENTED)" if currentLocation == Location.DARK_COVENTION:
            call updateTimeAndStats() from _call_updateTimeAndStats_45
            "5"

        "Tell her she can go, but afterwards you'd like her to do a holding challenge for you. (NOT IMPLEMENTED)" if currentLocation == Location.DARK_BAR:
            call updateTimeAndStats() from _call_updateTimeAndStats_46
            "6"

        "Tell her she can go, but you want to take a couple pictures first. (NOT IMPLEMENTED)" if currentLocation == Location.DARK_CLUB:
            call updateTimeAndStats() from _call_updateTimeAndStats_47
            "7"

        "Tell her you'll stop at the next place you see. (NOT IMPLEMENTED)" if currentLocation == Location.BROOM:
            call updateTimeAndStats() from _call_updateTimeAndStats_48
            "8"

        # gf attempts to use the bathroom

        "Tell her she's better go, then.":
            call updateTimeAndStats() from _call_updateTimeAndStats_49
            call allowPee() from _call_allowPee

        "Ignore her request to use the toilet.":
            call updateTimeAndStats() from _call_updateTimeAndStats_50
            call indePee() from _call_indePee

    
    # // If she's not in obviously dire straits, your
    # // admonitions, whatever they are, will effectly
    # // have answered her request to pee.  So the flag
    # // will be cleared.
    if (girlfriend.bladder < girlfriend.bladder_lose - 60):
        $ girlfriend.gotta_go_flag = False

    return 

define videoGameStoryAmity2 = "When I finally realized I had to pee, it was an emergency! I got up and rushed to the bathroom, only to find it was hogged by Emira. The manor has multiple bathrooms, but I couldn't make it to any of them because my poor bladder just gave out then and there. I completely soaked my panties and jeans and there was a huge puddle on the floor. I quickly summoned an abomination to clean it up because if Ed or Em ever found out about it, I'd never hear the end of it."
define videoGameStoryLuz2 = "When I finally realized I had to pee, it was an emergency! I got up and rushed to the bathroom, only to find it was hogged by Eda. My poor bladder just gave out then and there. I completely soaked my panties and jeans and there was a huge puddle on the floor. I quickly cleaned it up because if Eda ever found out about it, I'd never hear the end of it."


define peestory=["I used to never want to go to the restroom at school, and I'd hold it until I got home, which usually worked okay.  But one day, I was late for the Eggbus and I didn't have a chance to pee in the morning after I got up.  I was {b}so{/b} desperate all day.",
    "I really hate those porta-potties they have at fairs.  I remember one time I went to the county fair and I really had to pee, but I didn't want to leave.  I kept wandering around looking for a real restroom, getting more and more desperate.",
    "I went on a boating trip with some friends on spring break.  We all dressed up in our bikinis, drank a bunch of beer, and teased the guys on the river.  Nobody told us the boat didn't have a restroom.  We all had to pee {i}so{/i} badly, but we were trying to act all cool about it.",
    "One time, there was a bomb scare on campus.  No one was allowed to leave their classrooms.  I had just finished my morning coffee and started feeling an urge to pee.",
    "I hid this from you because it was so embarrassing at the time.  Remember that time when you fell asleep on my shoulder while we were watching the Tenth Azura Movie?  I had to pee so badly by the end of the movie, but I didn't want to wake you up.",
    "One time, I absentmindedly drank 2 whole litres of pop as I was immersed playing Azura's Gate. I totally ignored all of my body's needs for hours while I was playing the campaign.",
    "Story6",
    "Story7",
]

label pStory(girlfriend):
    # gf tells you about a time she was really desperate to pee.
    
    mainCharacter "Do you have any stories about a time when you were {b}really{/b} desperate to pee?"
    call displayNeed() from _call_displayNeed_5
    call superLongDialogue(character.girlfriend, peestory[pstorycounter]) from _call_superLongDialogue
    # girlfriend "[peestory[pstorycounter]]"

    $ videoGameStoryPt2 = videoGameStoryAmity2 if girlfriend.name == "Amity" else videoGameStoryLuz2
    $ peestory2=["I almost made it.  I was walking back home and I just couldn't hold it anymore - I always thought I could just try a little harder and hold it in, but it just started coming out.  There was nothing I could do.  I soaked my panties right outside my front door.",
        "I ended up almost wetting myself - I just {b}had{/b} to go.  It got so bad I couldn't walk and hold myself at the same time. Then, I started leaking, so I finally went in one of the portapotties.  It was sooo gross.",
        "Well - finally my friend couldn't hold it anymore, and jumped in the water to pee.  We all ended up peeing in our bikinis in the river.",
        "It turns out, the bomb scare was just a prank, but we didn't know that at the time.  They kept us locked in our classroom for hours without telling us what was going on.  It was agony, the coffee went through me so fast and I was desperate the entire time.  It was so embarrassing holding myself in front of all my classmates, but I had no choice, at that moment, the most likely explosion to happen was my bursting bladder.  After 5 hours of nursing my full bladder, the bomb squad finally cleared my classroom and allowed us to leave.  I hobbled towards the bathroom so slowly and leaked a bit on the way, but thankfully, I was able to get most of my pee in the toilet.",
        "Well, it seemed like you were having a dream about me, because you started saying my name, and hugging me - really really tight.  The pressure was too much for my poor bladder that I let out a big leak then and there, my bum was warm and soaked.  Then, you let go of me and started squishing the couch pillow really hard, so I took that opportunity to relieve myself and changed out of my soiled clothes before you woke up.",
        videoGameStoryPt2,
        "Story6Contd",
        "Story7Contd",
]

    menu continuePeeStory:

        "Ask [girlfriend.name] what happened.":
            mainCharacter "So... did you make it?"
            if girlfriend.name == "Amity":
                "[girlfriend.name] blushes and grabs the hem of her skirt." # TODO: implement clothing changes
            elif girlfriend.name == "Luz":
                "[girlfriend.name] blushes and looks down at her feet." 
            call superLongDialogue(character.girlfriend, peestory2[pstorycounter]) from _call_superLongDialogue_1
            call displayNeed() from _call_displayNeed_6

        "Continue...":
            "This story sounds familiar. I nod and smile because [girlfriend.name] must've told me about it already..."

    $ pstorycounter = (pstorycounter + 1) % MAX_P_STORY


    return


label allowPee():
    # You allowed your gf to go pee

    $ girlfriend.gotta_go_flag = False 
    $ girlfriend.ask_hold_it_counter = 0

    mainCharacter "Well, if you need to pee that badly [girlfriend.pet_name], then I guess you can go."
    girlfriend "Thanks! I do really have to go.  You're so sweet."
    call indePee() from _call_indePee_1

    return 

define locations_with_private_bathrooms = [
    Location.PICKUP_AMITYS_HOUSE,
    Location.PICKUP_LUZS_HOUSE,
    Location.AMITYS_BEDROOM_NIGHT,
    Location.LUZS_BEDROOM_NIGHT,
    Location.AMITYS_NIGHT_SEX_6,
    Location.LUZS_NIGHT_SEX_6,
]

define locations_with_no_toilets_around = [
    Location.BROOM,
    Location.MAKEOUT_LOCATION,
    Location.THE_HOT_TUB,
    Location.ROMANTIC_WALK,
    Location.THE_YARD,
    Location.LAKE_LACUNA_BEACH,
]

define gfs_home = [
    Location.AMITYS_BEDROOM_NIGHT,
    Location.AMITYS_LIVING_ROOM_NIGHT,
    Location.AMITYS_NIGHT_SEX_6,
    Location.LUZS_BEDROOM_NIGHT,
    Location.LUZS_LIVING_ROOM_NIGHT,
    Location.LUZS_NIGHT_SEX_6,
]

define a_location_where_gf_cannot_beg_for_toilet = [
    Location.THE_HOT_TUB,
]

define valid_pee_outside_venue_locations = [
    Location.GRIMGRUBS_PUB,
    Location.NIGHTCLUB_DANCE_VENUE,
    Location.CURRENTLY_DANCING,
    Location.COVENTION_HALL_PLAY,
    Location.WATCHING_COVENTION_PLAY,
]

define PICKUP_LOCATIONS = [
    Location.PICKUP_AMITYS_HOUSE,
    Location.PICKUP_LUZS_HOUSE,
]

define pre_date_locations = [
    Location.PICKUP_AMITYS_HOUSE,
    Location.PICKUP_LUZS_HOUSE,
    Location.PRE_DATE,
    Location.ON_CALL_WITH_GF,
    Location.BONESBOROUGH_MARKET,
]

label indePee():
    # Formerly indepee()
    # "Independent Pee" Is what I think this is supposed to be short for 
    # Your gf goes to seek a toilet

    # Girlfriend initially heads to the toilet
    $ girlfriend.gotta_go_flag = False 
    if (currentLocation in locations_with_private_bathrooms) and (buddyCalled != buddyCalledOptions.EMIRA):
        "[girlfriend.name] heads for the bathroom, leaving the door slightly ajar."
    elif currentLocation in locations_with_no_toilets_around:
        "[girlfriend.name] wants to go to the toilet, but then realizes..."
    else:
        "[girlfriend.name] runs towards the toilets."

    # Bathrooms might be locked or there might be a long line
    # TODO: Add a "short bathroom line" scenario where you have a chance of seeing her do a potty dance 
    #       or see her wet herself in line.
    # if (locstack[0] === "thebar" && rng.randomChoice(rrlockedthresh)) {
    if (currentLocation == Location.GRIMGRUBS_PUB and rng.randomChoice(rrlockedthresh)):
        call bathroomLocked() from _call_bathroomLocked
        if (girlfriend.checked_locked_restroom_counter > 3):
            girlfriend "It's {b}{i}still{/i}{/b} fucking locked!!"
        elif (girlfriend.checked_locked_restroom_counter > 2):
            girlfriend "It's {b}{i}still{/i}{/b} locked! What's taking so long?!"
        elif (girlfriend.checked_locked_restroom_counter > 0):
            girlfriend "It's still locked!"
        else:
            girlfriend "It was locked!"
        $ girlfriend.checked_locked_restroom_counter += 1
        call displayNeed() from _call_displayNeed_7
    # } else if (locstack[0] === "theclub" && rng.randomChoice(rrlinethresh)) {
    elif (currentLocation == Location.NIGHTCLUB_DANCE_VENUE and rng.randomChoice(restroom_line)):
        call bathroomLocked() from _call_bathroomLocked_1
        if (girlfriend.checked_locked_restroom_counter > 0):
            girlfriend "The line's not getting any smaller."
        else:
            girlfriend "There was a huge line."
        $ girlfriend.checked_locked_restroom_counter += 1
        call displayNeed() from _call_displayNeed_8
    # } else if (locstack[0] === "dodance" && rng.randomChoice(rrlinethresh)) {...
    elif (currentLocation == Location.CURRENTLY_DANCING and rng.randomChoice(restroom_line)):
        call bathroomLocked() from _call_bathroomLocked_2
        if (girlfriend.checked_locked_restroom_counter > 3):
            girlfriend "The line's still really fucking long."
        elif (girlfriend.checked_locked_restroom_counter > 2):
            girlfriend "I think the line's getting longer..."
        elif (girlfriend.checked_locked_restroom_counter > 0):
            girlfriend "The line's still really really long."
        else:
            girlfriend "There was a huge line."
        $ girlfriend.checked_locked_restroom_counter += 1
        call displayNeed() from _call_displayNeed_9
    # } else if (locstack[0] === "themovie" && rng.randomChoice(rrmovielinethresh) || locstack[0] === "domovie"rng.randomChoice(ice(rrmovielinethresh)) {
    elif (currentLocation == Location.COVENTION_HALL_PLAY and rng.randomChoice(restroom_covention_line)):
        call bathroomLocked() from _call_bathroomLocked_3
        if (girlfriend.checked_locked_restroom_counter > 3):
            girlfriend "The line's still really fucking long."
        elif (girlfriend.checked_locked_restroom_counter > 2):
            girlfriend "I think the line's getting longer..."
        elif (girlfriend.checked_locked_restroom_counter > 0):
            girlfriend "The line's still really really long."
        else:
            girlfriend "There was a huge line."
        $ girlfriend.checked_locked_restroom_counter += 1
        call displayNeed() from _call_displayNeed_10
    # } else if (locstack[0] === "themakeout") {
    elif (currentLocation == Location.MAKEOUT_LOCATION):
        "There are no toilets out here..."
        call displayNeed() from _call_displayNeed_11
    # } else if (locstack[0] === "driveout") {
    elif (currentLocation == Location.BROOM):
        "There are no toilets around and there's surely nowhere to pee on the broom."
        call displayNeed() from _call_displayNeed_12
    # } else if (locstack[0] === "thewalk" || locstack[0] === "theyard" || locstack[0] === "thebeach" || locstack[0] === "thehottub") {
    elif (currentLocation in locations_with_no_toilets_around):
        "There are no toilets around."
        call displayNeed() from _call_displayNeed_13
        call interpBladder() from _call_interpBladder_2
    # } else if (locstack[0] === "thehome" ||
    #     locstack[0] === "thebedroom" ||
    #     locstack[0] === "fuckher6") 
    elif (currentLocation in gfs_home):
        "You hear a quick clatter and a gasp as she lifts the toilet lid.  She starts to pee violently, a loud hiss accompanying the splash of the urine in the bowl.  You imagine being in there with her as she relieves her bladder."
        $ girlfriend.pees(gametime=gametime)

    # } else if (locstack[0] === "pickup" && buddywaterfavor == 0) {
    elif ((currentLocation == Location.PICKUP_AMITYS_HOUSE) and 
            (buddyCalled != buddyCalledOptions.EMIRA) # originally buddywaterfavor == 0
            ):
        "You hear a quick clatter of the toilet lid, and then the hissing and splashing of her urine in the bowl."
        $ girlfriend.pees(gametime=gametime)

    # } else if (locstack[0] === "pickup" && buddywaterfavor == 1 || locstack[0] === "callher" && buddywaterfavor == 1 || locstack[0] === "gostore" && buddywaterfavor == 1) {
    elif ((currentLocation in pre_date_locations) and (buddyCalled == buddyCalledOptions.EMIRA)): # originally buddywaterfavor == 1
        "You can hear her disappointed sigh realizing all her bathrooms are still locked thanks to Emira."
        girlfriend "All the bathrooms in the manor were locked. I couldn't go."
    
    # else
    else:
        $ randInt = renpy.random.randint(0,5)
        if (girlfriend.bladder > girlfriend.bladder_emergency):
            "[peeprivate[randInt]]"
        else: 
            "[peeprivate2[randInt]]"
        $ girlfriend.pees(gametime=gametime)


    # if (bladder >= bladlose - 60 && locstack[0] !== "thehottub" && locstack[0] !== "callher" && locstack[0] !== "gostore") begtoilet();
    if ((girlfriend.bladder >= girlfriend.bladder_lose - THREE_TURNS_FROM_WETTING) and 
        not(girlfriend in a_location_where_gf_cannot_beg_for_toilet)):
        call begToilet() from _call_begToilet # Not Implemented yet!!!
        # # $ raise NotImplemented("You need to implement begToilet()!")
        
    call updateTimeAndStats() from _call_updateTimeAndStats_51
    
    return


label bathroomLocked():
    # Narrates how your gf acts after discovering that bathroom is locked

    if (girlfriend.bladder > girlfriend.bladder_emergency):
        "[girlfriend.name] quickly runs back looking shaken."
    elif (girlfriend.bladder > girlfriend.bladder_emergency):
        "Momentarily, [girlfriend.name] returns looking uncomfortable."
    else:
        "[girlfriend.name] returns looking unfulfilled."

    return 


label begToilet():

    "[girlfriend.name] looks intently into your eyes:"
    # # $ raise NotImplemented("You need to implement begToilet()!")
    
    # if (peedvase)
    if (girlfriend.peed_vase):
        girlfriend "I've absolutely got to go.  I {i}need{/i} your vase again. {b}NOW!{/b}"
    # else if (peedshot)
    elif (girlfriend.peed_shot):
        girlfriend "I'm gonna pee myself!  I {i}need{/i} that shot glass again. {b}NOW!{/b}"
    # else if (peedtowels)
    elif (girlfriend.peed_towels):
        girlfriend "I just {b}can't{/b} hold it - you don't have any more paper towels, do you?"
    # else
    else:
        girlfriend "I'm {i}begging{/i} you - find me somewhere to pee.  {b}NOW!{/b}"

    menu EmergencyPeeOptions:
        # TODO: implement dialogue for all EmergencyPeeOptions!

        # if (shotglass > 0) c("peeshot", "Offer her the shot glass.");
        "Offer her the shot glass" if (item_shot in inventory):
            call peeShot() from _call_peeShot
        # if (ptowels > 0) c("peetowels", "Offer her the roll of paper towels.");
        "(Not implemented yet!) Offer her the roll of paper towels." if (item_roll in inventory):
            "Implement dialogue for gf peeing on paper towels!"
            call peeTowels() from _call_peeTowels
        # if (vase > 0) c("peevase", "Offer her the vase.");
        "Offer her the vase." if (item_vase in inventory):
            "Implement dialogue for gf peeing in vase!"
            # call peeVase() # Uncomment after this function is implemented
        # if (locstack[0] === "themakeout" ) c("peeoutside", "Suggest she pee outside.");
        "Suggest she pee outside." if (currentLocation == Location.MAKEOUT_LOCATION):
            "Implement dialogue for gf peeing outside!"
            # call peeOutdoors() # Uncomment after this function is implemented
        # if (locstack[0] === "thebar") c("peeoutsidevenue", "Suggest she pee outside.");
        # if (locstack[0] === "theclub" || locstack[0] === "godance") c("peeoutsidevenue", "Suggest she pee outside.");
        # if (locstack[0] === "themovie" || locstack[0] === "domovie") c("peeoutsidevenue", "Suggest she pee outside.");
        "Suggest she pee outside." if (currentLocation in valid_pee_outside_venue_locations):
            "Implement dialogue for gf peeing outside!"
            # call peeOutsideVenue() # Uncomment after this function is implemented
        # c(locstack[0], "Stand by helplessly.");
        "Stand by helplessly":
            # So as far as I can tell, the original extracts the most recent location from the locstack 
            # and calls the function corresponding to that location... 
            # I haven't implemented locations very well yet...
            # But I'm pretty sure my return statement already accomplishes that...
            return
            # "Implement dialogue for gf about to lose bladder control."
            # $ raise NotImplemented("`Stand by helplessly` dialogue has not been implemented yet!")


    return

label peeShot():

    if (girlfriend.mood > 30):
        if ((girlfriend.bladder > girlfriend.bladder_emergency and girlfriend.shyness < 60) or
            (girlfriend.bladder >= girlfriend.bladder_lose - TWO_TURNS_FROM_WETTING)
        ):
            $ girlfriend.gotta_go_flag = False
            if (not(girlfriend.peed_shot)):
                $ additional_text = " Noceda" if girlfriend.name == "Amity" else ""
                girlfriend "{i}*smirks*{/i} I didn't realize you were so naughty[additional_text]."
                girlfriend "I'm gonna wet my panties if I don't go....."
            $ girlfriend.peed_shot = True
            call displayNeed() from _call_displayNeed_14
            girlfriend "Titan! I can't wait any longer!"
            call peeShot2() from _call_peeShot2
        else: 
            # $ girlfriend.gotta_go_flag = False 
            girlfriend "I think maybe not. At least not yet..."
    else: # I refactored the if else tree here
        if (girlfriend.name == "Amity"):
            default multi_line_dialogue = "{i}Amity's face turns crimson{/i}\n"
            $ multi_line_dialogue += "LUZ! It's way too embarrassing to expose myself like that!"
            girlfriend "[multi_line_dialogue]"
        else:
            girlfriend "Somehow, I don't think that's happening."
        if (currentLocation not in locations_with_no_toilets_around):
            "She runs to the bathroom with her hands jammed to her crotch."
            "You are left to ponder your situation."
            $ girlfriend.flush_drank_inventory(gametime)
            $ girlfriend.mood -= 3
            # TODO: The original removes your shot glass in this scenario, 
            # I decided it's too painful to implement that with 
            # the way I structured the InventorySystem
        
    return 

label peeShot2(): 


    if (girlfriend.panty_colour_name is not None):
        # The dialogue below was formerly known as `peeshotquote`
        "She hurriedly grabs the shot glass and quickly rips down her tight jeans and [girlfriend.panty_colour_name] panties as she holds the edge of the glass against her pink pussy lips."
    else:
        "[peeshotquotebare]"
    call itsComingOut() from _call_itsComingOut
    call peeShot3() from _call_peeShot3

    return 

label peeShot3(): 

    $ inventory.attemptUseItem(item_shot, girlfriend, gametime)

    "The pee hisses out and the glass is filled in no time.  [girlfriend.name] bends over and jams her hand between her legs, gasping in the effort to stop the flow."
    girlfriend "Damn.  That's not much better..."

    $ girlfriend.mood += 3
    $ girlfriend.turns_to_wait_before_asking = 4
    $ girlfriend.saw_her_pee = True

    call updateTimeAndStats() from _call_updateTimeAndStats_52
    return 

label peeTowels():
    "Note: This option hasn't been properly implemented yet."
    "Amity takes the entire roll of paper towels and stuffs it down her pants."
    "The pee hisses out and is mostly absorbed by the paper towels, just a small trickle running down her left leg."
    girlfriend "{i}Ohh~~{/i}"
    "After about 2 minutes, Amity pulls the roll out of her pants. It's completely soaked."
    girlfriend "Thanks, I {b}really{/b} needed that!"
    $ girlfriend.pees(gametime=gametime)
    call updateTimeAndStats() from _call_updateTimeAndStats_53 # temp, to be replaced with whatever the html has
    # $ raise NotImplemented("peeTowels() has not been implemented yet!")
    return 

label peeVase():
    $ raise NotImplemented("peeVase() has not been implemented yet!")
    return 

label peeOutdoors():
    # Formerly peeoutside()
    $ raise NotImplemented("peeOutdoors() has not been implemented yet!")
    return 

label peeOutsideVenue():
    $ raise NotImplemented("peeOutsideVenue() has not been implemented yet!")
    return 

label itsComingOut():
    # It's coming out and she can't stop it
    # used to help describe various pees.
    $ randInt = renpy.random.randint(0,5)
    if not(girlfriend.saw_her_pee):
        girlfriend "[outPeeLook[randInt]]"
    else:
        girlfriend "[outPeeHide[randInt]]"
    $ randInt = renpy.random.randint(0,5)
    girlfriend "[outPeeCtrl[randInt]]"
    $ randInt = renpy.random.randint(0,5)
    girlfriend "[outPeeCome[randInt]]"
    
    return 

label display_hold_quip():
    # Formerly `displayholdquip`

    $ randInt = renpy.random.randint(0,5)
    if (girlfriend.peeUrgencyLevel.value >= PeeUrgencyLevel.BLADDER_LOSE.value):
        girlfriend "[quiplose[randInt]]"
    elif (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_EMERGENCY):
        girlfriend "[quipemer[randInt]]"
    elif (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_NEED):
        girlfriend "[quipneed[randInt]]"
    elif (girlfriend.peeUrgencyLevel == PeeUrgencyLevel.FIRST_URGE):
        girlfriend "[quipurge[randInt]]"
    else:
        girlfriend "I'm a big girl now - I can handle it."
    return

label display_drank():
    # Formerly `displaydrank`
    # She says how much she's drank since she last peed.

    $ randInt = renpy.random.randint(0,5)
    girlfriend "I drank [girlfriend.drank_inventory.list_drinks()] [drankburst[randInt]]"

    if (
        girlfriend.pre_peed == False
        and 
        currentLocation != Location.ON_CALL_WITH_GF
    ):
        girlfriend "I didn't even use the toilet before leaving!"
        $ girlfriend.pre_peed = True
    
    return

label display_waited():
    # Formerly `displaywaited`
    # She says how long she's been waiting to pee.
    girlfriend "[girlfriend.timeSinceLastPee(gametime)]"

    return

label convinceher():
    # You try to convince her to hold it.

    menu convince_her_menu:
        "How do I convince her to hold it?"

        "Try to bribe her with roses." if item_rose in inventory:
            call briberoses() from _call_briberoses

        "Try to bribe her with Azura Themed Diamond Earrings." if item_diam in inventory:
            call bribeearrings() from _call_bribeearrings

        "Call in a favor." if girlfriend.owed_favour:
            call bribefavor() from _call_bribefavor

        "Ask her nicely":
            call bribeask() from _call_bribeask

        "Just let her go...":
            call indePee() from _call_indePee_2

    return

label briberoses():

    mainCharacter "Pretty please!  I'll give you roses!"
    girlfriend "Okay.  For roses."
    $ girlfriend.ask_hold_it_counter += 1
    $ inventory._remove_item(item_rose)
    call display_hold_quip() from _call_display_hold_quip
    call updateTimeAndStats() from _call_updateTimeAndStats_54
    return

label bribeearrings():

    mainCharacter "Pretty please!  I'll give you a set of Azura Themed Diamond Earrings if you can hold it!"
    girlfriend "OMG! For Azura diamonds, I'd do much more than hold it.  But okay."
    $ girlfriend.ask_hold_it_counter += 1
    $ inventory._remove_item(item_diam)
    call display_hold_quip() from _call_display_hold_quip_1
    call updateTimeAndStats() from _call_updateTimeAndStats_55
    return

label bribefavor():

    mainCharacter "Pretty please!  Remember you promised to do me a favor!"
    girlfriend "Well... Okay.  But just a little bit.  I did promise you a favor."
    call display_hold_quip() from _call_display_hold_quip_2
    call interpBladder() from _call_interpBladder_3
    $ girlfriend.owed_favour = False
    $ girlfriend.ask_hold_it_counter += 1
    call updateTimeAndStats() from _call_updateTimeAndStats_56
    return

label bribeask():

    mainCharacter "Pretty please!"
    $ girlfriend.bribe_ask_threshold -= girlfriend.ask_hold_it_counter
    if rng.randomChoice(girlfriend.bribe_ask_threshold) and girlfriend.moodGreaterThanUrge:
        $ randInt = renpy.random.randint(0,5)
        girlfriend "[okayforyou[randInt]]"
        $ girlfriend.ask_hold_it_counter += 1
        call display_hold_quip() from _call_display_hold_quip_3
        call updateTimeAndStats() from _call_updateTimeAndStats_57
    else:
        girlfriend "You've already asked me to hold it [girlfriend.ask_hold_it_counter] times."
        call displayGottaGoVocalization() from _call_displayGottaGoVocalization_7
        call updateTimeAndStats() from _call_updateTimeAndStats_58
        call indePee() from _call_indePee_3
    return

label holdIt():
    # TODO: Maybe I revamp the inventory system? or use some subset of it as a sort of drinks counter for both main character and gf. Either way, I think it will no longer be a singleton...
    # Formerly holdit()

    # MC dialogue asking gf to hold it
    $ randInt = renpy.random.randint(0,5)
    mainCharacter "[askHold[randInt]]"

    # Set flags
    $ girlfriend.gotta_go_flag = False
    $ girlfriend.turns_to_wait_before_asking = 6

    # if (locstack[0] == "pickup" && prehold == 1 || locstack[0] == "pickup" && drankdiuretics == 1) {
    # If you're picking up gf and either she's already been holding, 
        # or she drank diuretics (not implemented), 
        # then display a quip response
    if (currentLocation in PICKUP_LOCATIONS) and (girlfriend.pre_hold):
        call display_hold_quip() from _call_display_hold_quip_4
        $ girlfriend.ask_hold_it_counter += 1
        call updateTimeAndStats() from _call_updateTimeAndStats_59

    # } else if ((bladder >= bladlose && attraction > holditlosethresh) ||
    elif girlfriend.moodGreaterThanUrge:

        # Temporary dialogue
        girlfriend "You're lucky I love you more than I need to pee right now. But..."

        # if (bladder >= blademer) {
        if girlfriend.peeUrgencyLevel.value >= PeeUrgencyLevel.BLADDER_EMERGENCY.value:

            $ randInt = renpy.random.randint(0,5)
            girlfriend "[surpriseexcl[randInt]]"

            # if (randomchoice(5))
            if rng.randomChoice(50): 
                call display_drank() from _call_display_drank
            else:
                call display_waited() from _call_display_waited

            girlfriend "I don't know..."

            # if (locstack[0] !== "gostore") displayneed();
            if currentLocation != Location.BONESBOROUGH_MARKET:
                call displayNeed() from _call_displayNeed_15
            # else displaygottavoc();
            else: 
                call displayGottaGoVocalization() from _call_displayGottaGoVocalization_8

            call convinceher() from _call_convinceher

        else:
            call display_hold_quip() from _call_display_hold_quip_5
            $ girlfriend.ask_hold_it_counter += 1

            # if (bladder >= bladlose) {
            # I don't think this block ever gets reached...
            if (girlfriend.bladder >= girlfriend.bladder_lose):
                # if (locstack[0] === "gostore") {
                if (currentLocation == Location.BONESBOROUGH_MARKET):
                    girlfriend "Ummm...  Oh.   Oh.  Uh. ohmygod.  ohmygod. ohmygod."
                    girlfriend "{i}gasps{/i} I can't hold it - it's - it's coming out!"
                    $ girlfriend.pees(gametime)
                    $ girlfriend.mood = 0
                    girlfriend "I'm so embarassed - I'll go clean up."
                # } else {
                else:
                    call displayNeed() from _call_displayNeed_16
    # } else {
    else:
        # if (locstack[0] === "gostore") {
        if currentLocation == Location.BONESBOROUGH_MARKET:
            girlfriend "Sorry."
            "She's hung up on you."
            $ girlfriend.mood -= 5
            $ girlfriend.pees(gametime)
        # } else {
        else:
            girlfriend "Not gonna happen, sweet potato."
            $ girlfriend.mood -= 5
            call indePee() from _call_indePee_4
        # }
    # }

    return

label holdits():
    # Telling girlfriend to hold it when she's submissive.
    # TODO: This branch is untested, I need to do a test for submissive dialogue!
    $ randInt = renpy.random.randint(0,8)
    mainCharacter "[tellhold[randInt]]"
    $ girlfriend.gotta_go_flag = False
    $ girlfriend.turns_to_wait_before_asking = 6
    call display_hold_quip() from _call_display_hold_quip_6
    $ girlfriend.ask_hold_it_counter += 1

    if (girlfriend.bladder >= girlfriend.bladder_lose):
        if currentLocation == Location.BONESBOROUGH_MARKET:
            girlfriend "Ummm...  Oh.   Oh.  Uh. ohmygod.  ohmygod. ohmygod."
            girlfriend "{i}gasps{/i} I can't hold it - it's - it's coming out!"
            $ girlfriend.pees(gametime)
            $ girlfriend.mood = 0
            girlfriend "I'm so embarassed - I'll go clean up."
        else:
            call displayNeed() from _call_displayNeed_17

    call updateTimeAndStats() from _call_updateTimeAndStats_60
    return

