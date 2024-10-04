define Merchant = Character("Merchant", color="#37f146")

# label promptForQuantityInput(item):
#     renpy.input(prompt="How much [item.name] do you want to purchase?")
#     $ itemPurchasedSuccessfully = inventory.attemptPurchaseItem(item_water)


label BonesboroughMarketPlace:

    # Display marketplace background
    show bg bonesborough marketplace

    # Display Luz
    show luz happy:
        xalign 0.1
        yalign 0.9

    "What should I purchase?"

    menu:
        
        # TODO: Make it so that you can buy in bulk at once!

        "A bottle of water ($[item_water.cost])":
            # call promptForQuantityInput(item_water)
            $ quantityPurchased = inventory.attemptPurchaseItem(item_water)
            call updateTimeAndStats() from _call_updateTimeAndStats_10
            if quantityPurchased == 1:
                "A water bottle was purchased for $[item_water.cost]."
            elif quantityPurchased > 1:
                "[quantityPurchased] bottles of water were purchased for $[item_water.cost * quantityPurchased]."

        "A bottle of water and a diuretic medicine ($[item_diur.cost])":
            $ quantityPurchased = inventory.attemptPurchaseItem(item_diur)
            call updateTimeAndStats() from _call_updateTimeAndStats_11
            if quantityPurchased == 1:
                "A bottle of diuretic laced water was purchased for $[item_diur.cost]."
            elif quantityPurchased > 1:###############################################################################
                "[quantityPurchased] bottles of diuretic laced water were purchased for $[item_diur.cost * quantityPurchased]."

        "An extra large cup of Hot Brown Morning Potion ($[item_hbmp.cost])":
            Merchant "You're in luck! A premium batch was imported from Xadia this afternoon!"
            $ quantityPurchased = inventory.attemptPurchaseItem(item_hbmp)
            call updateTimeAndStats() from _call_updateTimeAndStats_12
            if quantityPurchased == 1:
                "A Hot Brown Morning Potion was purchased for $[item_hbmp.cost]."
            elif quantityPurchased > 1:
                "[quantityPurchased] bottles of Hot Brown Morning Potions were purchased for $[item_hbmp.cost * quantityPurchased]."

        "(Doesn't do much yet) A bouquet of red roses ($[item_rose.cost])":
            $ quantityPurchased = inventory.attemptPurchaseItem(item_rose)
            call updateTimeAndStats() from _call_updateTimeAndStats_13
            if quantityPurchased == 1:
                "A bouquet of roses were purchased for $[item_rose.cost]."
            elif quantityPurchased > 1:
                "[quantityPurchased] bouquets of roses were purchased for $[item_rose.cost * quantityPurchased]."

        "(Doesn't do much yet) A pair of Azura themed diamond earrings ($[item_diam.cost])":
            $ quantityPurchased = inventory.attemptPurchaseItem(item_diam)
            call updateTimeAndStats() from _call_updateTimeAndStats_14
            if quantityPurchased >= 1:
                if quantityPurchased == 1:
                    "A pair of Azura themed diamond earrings were purchased for $[item_diam.cost]."
                else:
                    "[quantityPurchased] pairs of Azura themed diamond earrings purchased for $[item_diam.cost * quantityPurchased]."
                mainCharacter "[girlfriend.name] already has a bunch of diamond earrings, but she's gonna love these Azura themed ones!"

        "(Doesn't do much yet) A flower vase ($[item_vase.cost])":
            $ quantityPurchased = inventory.attemptPurchaseItem(item_vase)
            call updateTimeAndStats() from _call_updateTimeAndStats_15
            if quantityPurchased == 1:
                "A flower vase was purchased for $[item_vase.cost]."
            elif quantityPurchased > 1:
                "[quantityPurchased] flower vases were purchased for $[item_vase.cost * quantityPurchased]."

        "(Doesn't do much yet) A shot glass ($[item_shot.cost])":
            $ quantityPurchased = inventory.attemptPurchaseItem(item_shot)
            call updateTimeAndStats() from _call_updateTimeAndStats_16
            if quantityPurchased == 1:
                "A shot glass was purchased for $[item_shot.cost]."
            elif quantityPurchased > 1:
                "[quantityPurchased] shot glasses were purchased for $[item_shot.cost * quantityPurchased]."

        "A roll of paper towels ($[item_roll.cost])": # Needs further implementation as a container item
            $ quantityPurchased = inventory.attemptPurchaseItem(item_roll)
            call updateTimeAndStats() from _call_updateTimeAndStats_17
            if quantityPurchased == 1:
                "A roll of paper towels was purchased for $[item_roll.cost]."
            elif quantityPurchased > 1:
                "[quantityPurchased] rolls of paper towels were purchased for $[item_roll.cost * quantityPurchased]."

        "A pair of sexy panties ($[item_panties.cost])":
            $ quantityPurchased = inventory.attemptPurchaseItem(item_panties)
            call updateTimeAndStats() from _call_updateTimeAndStats_18
            if quantityPurchased >= 1:
                if quantityPurchased == 1:
                    "A pair of sexy panties were purchased for $[item_panties.cost]."
                else:
                    "[quantityPurchased] pairs of sexy panties were purchased for $[item_panties.cost * quantityPurchased]."
                mainCharacter "I wonder how [girlfriend.name] will look wearing this?..."

        "(Doesn't do much yet) Artisan Grape Blood ($[item_wine.cost])":
            $ quantityPurchased = inventory.attemptPurchaseItem(item_wine)
            call updateTimeAndStats() from _call_updateTimeAndStats_19
            if quantityPurchased == 1:
                "A bottle of Artisan Grape Blood was purchased for $[item_wine.cost]."
            elif quantityPurchased > 1:
                "[quantityPurchased] bottles of Artisan Grape Blood were purchased for $[item_wine.cost * quantityPurchased]."
        
        "Leave the market":
            call updateTimeAndStats() from _call_updateTimeAndStats_20
            # Merchant "Hey GoldenGuard, Remember to implement a better inventory GUI for this game!..."
            jump PrepareForDate

    if quantityPurchased == -1:
        jump NotEnoughSnails
    elif quantityPurchased == 0:
        Merchant "Titan! What good are you to me if you won't buy anything?"
        jump BonesboroughMarketPlace
    else:
        jump BonesboroughMarketPlace
        
label NotEnoughSnails:
    Merchant "Ay, you don't have enough snails to buy that."
    jump BonesboroughMarketPlace