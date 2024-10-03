default buddyCalled = buddyCalledOptions.NOBODY

label PhoneFriend:
    # TODO: Make this a menu and add multiple friends to call
    # TODO: Make sure I also implement the long-term consequences of calling a buddy

    menu whoToCall:

        "Who should I call?"

        "Emira":
            define Emira = Character("Emira", color="#0f6d49")
            Emira "Ooh, you and Mittens share {i}that{/i} kink. I'll help you out."
            Emira "I'll hog the bathroom this evening so that she can't use it before your date tonight."
            $ girlfriend.bladder = max(ceil(0.9 * girlfriend.bladder_need), girlfriend.bladder + 200)
            "Emira hangs up. You wonder how full Amity's bladder will be at the start of your date"
            "And also how long it'll be until she asks for a bathroom break..."
            $ buddyCalled = buddyCalledOptions.EMIRA 
            # TODO: There should be special dialogue of Amity admitting that she didn't get a chance to use the washroom due to Emira hogging it
    
        "Edric":
            define Edric = Character("Edric", color="#0f6d49")
            Edric "Sounds like you need some help pranking Mittens."
            Edric "I'll send you a few snails to help you out."
            "Edric hangs up. A few minutes later, the crow returns with 2000 snails."
            $ inventory.snails += 2000
            $ buddyCalled = buddyCalledOptions.EDRIC


    
    jump PrepareForDate