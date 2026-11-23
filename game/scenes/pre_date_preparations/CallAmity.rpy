label CallAmity:
    # Does the work of function formerly callher()
    # TODO: generalize this function!

    # Update Location Flag
    $ currentLocation = Location.ON_CALL_WITH_GF

    "I send a crow towards Blight Manor and await a response."
    Amity "Hola Batata, how are you doing?"
    Luz "I'm doing great! I am so excited for tonight!"
    jump CallAmityChoices


label CallAmityChoices:

    menu:

        "Ask for a favour":
            call updateTimeAndStats() from _call_updateTimeAndStats_21
            jump PhoneFavours

        "[complimentGirlfriend!i]" if complimentGirlfriendConditional():
            call complimentGirlfriendResult(girlfriend, on_phone = True) from _call_complimentGirlfriendResult_2
            jump CallAmityAnythingElse

        "Say \"See you soon!\" and hang up":
            call updateTimeAndStats() from _call_updateTimeAndStats_23
            Luz "See you soon!"
            "I hang up before Amity has the chance to play the \"You hang up first\" game with me again."
            "I was late to our date that night and she still got upset with me! (It was the playful type of upset, but still...)"
            jump PrepareForDate

    # jump PrepareForDate


label PhoneFavours: # TODO: I haven't completely implemented this yet, 
    # look at the functions favor() and gotta() from the original html

    Luz "Could I ask please for a favour before our date?"
    Amity "Oh alright, since you're asking so nicely Batata."

    menu:

        "Do you need to pee right now?":

            Amity "N- Nope! Not at all, w- why do you ask, Luz?"
            "I hear a hint of nervousness in her voice as she said that."
            call updateTimeAndStats() from _call_updateTimeAndStats_24

            menu:

                "You just sound distracted is all.":
                    Amity "Oh, really?"
                    call updateTimeAndStats() from _call_updateTimeAndStats_25

                "Could you hold it until I come pick you up?":
                    # Amity "N- Nope. Sorry Luz, I- I just don't {i}want{/i} to be... bursting... during our date..."
                    # "She sounded really flustered as she said that."
                    call waitpickup(girlfriend) from _call_waitpickup
                    call updateTimeAndStats() from _call_updateTimeAndStats_26

        "Could you drink a glass of water?":
            if girlfriend.tummy <= girlfriend.tummy_capacity:
                $ girlfriend.tummy += 1000
                $ girlfriend.drank_inventory.add_drink(item_water, 2)
                Amity "Yep, I'll drink 2! It's always good to stay hydrated!"
            else:
                Amity "I'm not thirsty right now."
            call updateTimeAndStats() from _call_updateTimeAndStats_27

        "Nevermind...":
            call updateTimeAndStats() from _call_updateTimeAndStats_28
            jump CallAmityAnythingElse

    jump CallAmityAnythingElse


label CallAmityAnythingElse:

    Amity "Anything else Batata?"
    jump CallAmityChoices

define BUDDY_BATHROOM_HOGS = [
    buddyCalledOptions.EMIRA, 
    buddyCalledOptions.KING, 
]

label waitpickup(girlfriend):

    # if (drankdiuretics > 0 && !buddywaterfavor && !buddysubfavor) {
    # If gf drank diuretics (NYI) and none of the relevant buddy favours are active

    # } else if (buddywaterfavor == 1 && shyness <= 80 && !buddysubfavor) {
    # If gf can't access bathroom anyways and isn't too shy. buddysubfavor is NYI
    if (buddyCalled in BUDDY_BATHROOM_HOGS):
        if buddyCalled == buddyCalledOptions.EMIRA:
            girlfriend "Fine."
            girlfriend "Emira is currently hogging the bathroom, so it's not like I'd be able to use it anyways. Just please hurry up, okay?"
        elif buddyCalled == buddyCalledOptions.KING:
            girlfriend "Fine."
            girlfriend "King is currently hogging the bathroom, so it's not like I'd be able to anyways. Just please hurry up, okay?"
        $ girlfriend.shyness -= 10
        $ girlfriend.ask_hold_it_counter += 1
        $ girlfriend.pre_hold = True 

    # } else if (buddysubfavor == 1 && !buddywaterfavor) {
    # If gf is submissive

    # } else if (attraction > 13) {
    # If gf is in a decent mood

    # } else {
    else:
        if girlfriend.name == "Amity":
            girlfriend "N- Nope. Sorry Luz, I- I just don't {i}want{/i} to be... bursting... during our date..."
            "She sounded really flustered as she said that."
        elif girlfriend.name == "Luz":
            $ raise NotImplemented("Dialogue for shy Luz declining to hold it before date is NYI!")
        $ girlfriend.pees(gametime=gametime)
        $ girlfriend.mood = 0
        call updateTimeAndStats() from _call_updateTimeAndStats_22

    return 
