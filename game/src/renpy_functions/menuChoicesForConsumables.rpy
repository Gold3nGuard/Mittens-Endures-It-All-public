# Do not jump to any of these labels, only call!
label universalConsumableLiquidMenuChoices():
    menu: 
        "What should I give her to drink?"

        "[item_water.menu_option_text]" if item_water in inventory:
            call universalConsumableLiquidResponses(consumableLiquid=item_water, girlfriend=girlfriend) from _call_universalConsumableLiquidResponses

        "[item_diur.menu_option_text]" if item_diur in inventory:
            call universalConsumableLiquidResponses(consumableLiquid=item_diur, girlfriend=girlfriend) from _call_universalConsumableLiquidResponses_1

        "[item_hbmp.menu_option_text]" if item_hbmp in inventory:
            call universalConsumableLiquidResponses(consumableLiquid=item_hbmp, girlfriend=girlfriend) from _call_universalConsumableLiquidResponses_2 

        "Nevermind...":
            call updateTimeAndStats() from _call_updateTimeAndStats_37
            
    return 


label universalConsumableLiquidResponses(consumableLiquid, girlfriend): 

    $ liquid_drank_confirmation = inventory.attemptUseItem(consumableLiquid, girlfriend=girlfriend)
    call updateTimeAndStats() from _call_updateTimeAndStats_35
    if liquid_drank_confirmation == RemoveItemConfirmationState.ITEM_CONSUMED_SUCCESSFULLY:
        "[girlfriend.name] drank the [consumableLiquid.name.lower()], all [consumableLiquid.volume] mL of it."
        girlfriend "[consumableLiquid.consumption_confirmation_response]"
    elif liquid_drank_confirmation == RemoveItemConfirmationState.GIRLFRIEND_REFUSED_CONSUMPTION:
        girlfriend "I'm not thirsty right now."
    elif liquid_drank_confirmation == RemoveItemConfirmationState.ITEM_NOT_IN_INVENTORY:
        "I don't have any [consumableLiquid.name]"
    else:
        "ERROR: Check the code, something went wrong!"

    return

label moodAlteringItemChoices():
    menu PresentToGive:
        "What should I gift to her?"

        "[item_rose.menu_option_text]" if item_rose in inventory:
            call MoodAlteringItemResponses(item_rose, girlfriend) from _call_MoodAlteringItemResponses 

        "[item_diam.menu_option_text]" if item_diam in inventory:
            call MoodAlteringItemResponses(item_diam, girlfriend) from _call_MoodAlteringItemResponses_1  

        "Nevermind...":
            call updateTimeAndStats() from _call_updateTimeAndStats_38

    return

label MoodAlteringItemResponses(moodAlteringItem, girlfriend):

    $ item_use_confirmation = inventory.attemptUseItem(moodAlteringItem, girlfriend)
    call updateTimeAndStats() from _call_updateTimeAndStats_36
    if item_use_confirmation == RemoveItemConfirmationState.ITEM_CONSUMED_SUCCESSFULLY:
        if (girlfriend.bladder < girlfriend.bladder_emergency):
            girlfriend "[moodAlteringItem.consumption_confirmation_response]"
        else:
            girlfriend "[moodAlteringItem.consumption_emergency_response]"
            "{i}She takes the [moodAlteringItem.name], but it seems that she can only think about the toilet right now.{/i}"        
    elif item_use_confirmation == RemoveItemConfirmationState.ITEM_NOT_IN_INVENTORY:
        "I don't have any [consumableLiquid.name]"
    else:
        "ERROR: Check the code, something went wrong!"

    return

     