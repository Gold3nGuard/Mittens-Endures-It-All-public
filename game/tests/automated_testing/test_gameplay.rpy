testsuite gameplay:
    setup:
        click "start"
        skip until screen "choice"

    testcase open_inventory:
        pause 0.5
        $ print("testcase open_inventory activated")
        click id "inventory_open_button"
        $ print("inventory_open_button pressed")

    testcase start_time_defined:
        $ print(gametime)
        $ print(Time(17,30))
        $ print(gametime == Time(17,30))
        assert eval(gametime == Time(17,30))

    teardown:
        run MainMenu(confirm=False)
