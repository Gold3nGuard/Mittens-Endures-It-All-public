# Snails
screen snails():
    modal False

    frame:
        background Solid("#075a07c7")

        xpos 1750
        ypos 169
        xpadding 18
        ypadding -7
        xsize 170
        
        # hbox:
        grid 2 1:
            # spacing -26
            add "bg snail":
                xpos -28
                ypos -1
            text "{size=30}{color=#ffe921}[inventory.snails: >6]":
                xpos -85
                ypos 10


screen hud():
    modal False

    # Press E to open inventory
    key "K_e" action [Show("inventory"), Hide("hud")]
    # Controller guide button opens inventory
    key "pad_back_press" action [Show("inventory"), Hide("hud")]

    # Inventory icon
    imagebutton auto "bg_inventory_luzs_bag_closed_%s.png":
        id "inventory_open_button"
        focus_mask True
        keyboard_focus False
        hovered SetVariable("screen_tooltip", "Inventory")
        unhovered SetVariable("screen_tooltip", "")
        action Show("inventory"), Hide("hud")


screen inventory():
    add "minecraft_inventory"
    modal True

    # Press E to close inventory
    key "K_e" action [Show("hud"), Hide("inventory")]
    # Controller guide button closes inventory
    key "pad_back_press" action [Show("hud"), Hide("inventory")]

    # Display items
    vbox:
        pos 0.1, 0.25
        text "[inventory.list_items(withNewlines=True)]"

    # Close inventory icon
    imagebutton auto "bg_inventory_luzs_bag_open_%s.png":
        id "inventory_close_button"
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip", "")
        action Show("hud"), Hide("inventory")
