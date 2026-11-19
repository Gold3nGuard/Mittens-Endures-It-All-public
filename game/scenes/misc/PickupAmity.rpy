label PickupAmity:

    scene bg blight manor day
    show amity happy smaller facing right:
        xalign 0.18
        yalign 1.1

    # Change location flag
    $ currentLocation = Location.PICKUP_AMITYS_HOUSE

    Amity "Hi Luz! I'm so happy to see you! Ready for our date?"

    menu readyForDate:

        # Check standobjs() and askpee(). I will probably use a flag instead
        # "Ask if she needs to pee":
        #     call updateTimeAndStats() from _call_updateTimeAndStats_5
        #     Amity "N- nope! Not at all!"
        #     "[girlfriend.peeUrgencyLevel]"
        #     call showNeed(character.mainCharacter, girlfriend) from _call_showNeed_3

        # TODO: Find a way to centralize all menu choices
        "[askPeeOption]" if askPeeConditional(girlfriend):
            call askPeeResult() from _call_askPeeResult_1

        "Give her something to drink" if inventory.hasUniversalConsumableLiquid:
            call updateTimeAndStats() from _call_updateTimeAndStats_6
            call universalConsumableLiquidMenuChoices() from _call_universalConsumableLiquidMenuChoices_1
            call showNeed(character.mainCharacter, girlfriend) from _call_showNeed_4

        "Give her a present" if inventory.hasMoodAlteringItem:
            call updateTimeAndStats() from _call_updateTimeAndStats_7
            call moodAlteringItemChoices() from _call_moodAlteringItemChoices
            call showNeed(character.mainCharacter, girlfriend) from _call_showNeed_5
        
        # "Compliment [girlfriend.name]":
        #     call compliment(girlfriend) from _call_compliment
        #     call updateTimeAndStats() from _call_updateTimeAndStats_8
        #     Amity "You're so sweet Luz!"
        #     call showNeed(character.mainCharacter, girlfriend) from _call_showNeed_6

        "[complimentGirlfriend!i]" if complimentGirlfriendConditional():
            call complimentGirlfriendResult(girlfriend) from _call_complimentGirlfriendResult_1

        "\"Let's get going!\"":
            call updateTimeAndStats() from _call_updateTimeAndStats_9
            "We leave her house."
            jump GoToBroom
            # call changeLocation(character.mainCharacter, girlfriend, newLocation = "BroomRide")
            # call showNeed(character.mainCharacter, girlfriend)

    jump readyForDate
