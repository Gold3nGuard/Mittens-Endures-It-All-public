# # ========== START OF BOILERPLATE ==========
# # boilerplate

# ## Text option to display
# default txtOption = "txtOption" # Note: for nested text interpolation, 
# # the outermost text must have the format [var!i] with suffix !i

# ## Conditional that decides whether option appears
# init python:
#     def txtOptionConditional():
#         return True

# ## Result of choice
# label txtOptionResult():
#     return

# # in the menu script, the menu should look like this:
# menu: # it's fine that this statement is unreachable!
#     "[txtOption]" if txtOptionConditional():
#         call txtOptionResult()
# # ========== END OF BOILERPLATE ==========

# complimentGirlfriend

## Text option to display
default complimentGirlfriend = "Compliment [girlfriend.name]"

## Conditional that decides whether option appears
init python:
    def complimentGirlfriendConditional():
        return True

## Result of choice
label complimentGirlfriendResult(girlfriend, on_phone = False):
    call compliment(girlfriend) from _call_compliment 
    call updateTimeAndStats() from _call_updateTimeAndStats_33 
    girlfriend "You're so sweet [character.mainCharacter.name]"

    if not on_phone:
        call showNeed(character.mainCharacter, girlfriend) from _call_showNeed_3 
    return

# ---

# askPeeOption

## Text option to display
default askPeeOption = "Ask if she needs to pee" # Note: for nested text interpolation, 
# the outermost text must have the format [var!i] with suffix !i

## Conditional that decides whether the "ask if she needs to pee" option appears
init python:
    def askPeeConditional(girlfriend):
        # if (randomchoice(5) && gottagoflag < 1 && showedneed > 0 && !askholditcounter)
        return (
            rng.randomChoice(50)
            and 
            not(girlfriend.gotta_go_flag)
            and 
            girlfriend.showed_need 
            and 
            girlfriend.ask_hold_it_counter == 0
            )

## Result of choice
label askPeeResult():
    call updateTimeAndStats() from _call_updateTimeAndStats_34 
    call askPee(character.mainCharacter, girlfriend) from _call_askPee
    return

# ---
