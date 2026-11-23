# Necessary to create a dynamic variable accessible by the screen
# This overrides the default value in renpy.input(), 
# but I only use it for purchase screens so all good

default quantity = "1" 
default min_quantity = 0

init python:

    def increment_quantity():

        if store.quantity == "":
            updated_quantity = "0"
        else:
            updated_quantity = str(int(store.quantity) + 1)

        return SetVariable(
                "quantity",
                updated_quantity,
            )

    def decrement_quantity():

        if store.quantity == "":
            updated_quantity = "0"
        else:
            updated_quantity = str(max(store.min_quantity, int(store.quantity) - 1))

        return SetVariable(
                "quantity",
                updated_quantity,
            )


screen purchase_item_input_screen(prompt):
    # Provides the screen that asks for quantity input for item purchases
    
    on "show" action SetVariable("quantity", "1")
    style_prefix "input"

    # Extract the item price and prompt from the prompt string
    python:
        item_price = int(prompt.split('$')[1])
        prompt = prompt.split('$')[0]

    window:

        vbox:
            # Apply text positioning
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos (gui.dialogue_ypos - 60)

            # Show prompt
            text prompt style "input_prompt"

            # # Dynamically show the price
            text "Total Cost: ${} ".format(item_price * int(quantity) if (isinstance(quantity, int) or quantity.isdigit()) else 0) style "input_prompt"

            # Dynamically update quantity, which updates the price
            input value VariableInputValue("quantity") id "input" 


            # Up arrow: increment
            key "K_UP" action increment_quantity()
            key "pad_dpup_press" action increment_quantity()

            # Down arrow: decrement
            key "K_DOWN" action decrement_quantity()
            key "pad_dpdown_press" action decrement_quantity()

            # Confirm the purchase with the enter key
            key "K_RETURN" action Return(quantity)
            key "pad_a_press" action Return(quantity)
