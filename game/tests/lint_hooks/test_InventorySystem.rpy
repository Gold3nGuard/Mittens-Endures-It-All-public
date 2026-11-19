init -98 python:

    @test_case
    def test_list_items1():

        # Initial inventory should be empty
        inventory = PlayerInventory()
        expected = "I'm not carrying anything"
        actual = inventory.list_items()
        assert expected == actual, f"Inventory should be initialized as empty!\n Expected = {expected} \n Actual   = {actual}"

        inventory.add_item_without_purchase(Water())
        expected = "Water: 1"
        actual = inventory.list_items()
        assert expected == actual, f"Water not added properly!\n Expected = {expected} \n Actual   = {actual}"

    @test_case
    def test_inventory_system():

        class ConcreteInventoryItems:
            # Initialize items that are used in the game
            item_water: InventoryItem = Water()
            item_diur: InventoryItem = WaterWithDiuretic()
            item_hbmp: InventoryItem = HotBrownMorningPotion()
            item_soda: InventoryItem = AppleBlood()
            item_rose: InventoryItem = BouquetOfRoses()
            item_diam: InventoryItem = AzuraDiamondEarring()
            item_vase: InventoryItem = FlowerVase()
            item_shot: InventoryItem = ShotGlass()
            item_roll: InventoryItem = PaperTowelRoll()
            item_panties: InventoryItem = SexyPanties()
            item_wine: InventoryItem = ArtisanGrapeBlood()

        cii = ConcreteInventoryItems
        
        inventory = PlayerInventory()

        # Adding items
        inventory.add_item_without_purchase(cii.item_water)
        inventory.add_item_without_purchase(cii.item_hbmp)
        inventory.add_item_without_purchase(cii.item_water)
        inventory.add_item_without_purchase(cii.item_water)
        inventory.add_item_without_purchase(cii.item_hbmp)
        inventory.add_item_without_purchase(cii.item_shot)
        inventory.add_item_without_purchase(cii.item_rose)
        inventory.add_item_without_purchase(cii.item_shot, 0)
        inventory.add_item_without_purchase(cii.item_panties, 0)
        inventory.add_item_without_purchase(cii.item_water, 2)
        my_assert(
            inventory.list_items(), 
            "Water: 5, Hot Brown Morning Potion: 2, Shot Glass: 1, Roses: 1",
            "Inventory does not have the expected items!",
        )

        # Removing items
        inventory._remove_item(cii.item_water)
        inventory._remove_item(cii.item_shot) # Reusable Item!
        inventory._remove_item(cii.item_rose)
        my_assert(
            inventory.list_items(), 
            "Water: 4, Hot Brown Morning Potion: 2, Shot Glass: 1",
            "Inventory does not have the expected items!",
        )
