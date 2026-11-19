testsuite timewaited:
    setup:
        click "start"
        skip until screen "choice"

    testcase timewaited:

        # Go to market and fill up inventory
        click "Go to the Bonesborough Market Place"
        skip until screen "choice"
        click "An extra large cup of Hot Brown Morning Potion"
        advance until id "input"
        keysym "K_UP" id "input"
        keysym "K_UP" id "input"
        keysym "K_UP" id "input"
        keysym "K_RETURN" id "input"
        
        # Open inventory 
        pause 0.5
        $ print("testcase open_inventory activated")
        click id "inventory_open_button"
        $ print("inventory_open_button pressed")

        # This system is so frustrating to work with... i can finish implementing this test suite later....

    # teardown:
    #     exit
