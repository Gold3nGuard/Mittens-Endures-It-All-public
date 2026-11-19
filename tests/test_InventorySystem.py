import unittest  # noqa: N999

import tests.src.InventoryItems as ii


class ConcreteInventoryItems:
    # Initialize items that are used in the game
    item_water: ii.InventoryItem = ii.Water()
    item_diur: ii.InventoryItem = ii.WaterWithDiuretic()
    item_hbmp: ii.InventoryItem = ii.HotBrownMorningPotion()
    item_soda: ii.InventoryItem = ii.AppleBlood()
    item_rose: ii.InventoryItem = ii.BouquetOfRoses()
    item_diam: ii.InventoryItem = ii.AzuraDiamondEarring()
    item_vase: ii.InventoryItem = ii.FlowerVase()
    item_shot: ii.InventoryItem = ii.ShotGlass()
    item_roll: ii.InventoryItem = ii.PaperTowelRoll()
    item_panties: ii.InventoryItem = ii.SexyPanties()
    item_wine: ii.InventoryItem = ii.ArtisanGrapeBlood()

cii = ConcreteInventoryItems

class TestInventorySystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # Extract the Python code and import the package
        from tests.utils.extractPython import extractPy
        extractPy('game/src/py/utils/Singleton.rpy', 'tests/src/')
        extractPy('game/src/py/Time.rpy', 'tests/src/')
        # extractPy('game/src/py/Girlfriend.rpy', 'tests/src/')
        extractPy('game/src/py/inventory/InventoryItems.rpy', 'tests/src/')
        extractPy('game/src/py/inventory/InventorySystem.rpy', 'tests/src/')
        extractPy('game/src/py/inventory/PlayerInventory.rpy', 'tests/src/')
        global PlayerInventory
        from tests.src.PlayerInventory import PlayerInventory


    def test_default_snails(self): # This is a bad test, I will probably change this value in the future
        inventory = PlayerInventory()
        self.assertEqual(inventory.snails, 150)

    # TODO: test out adding, removing, and using items in the inventory. maybe i could use automated testing for this? will need to define concrete instantiations of each item for consistency
    def test_adding_removing_using_items(self):
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
        self.assertEqual(
            first=inventory.list_items(),
            second="Water: 5, Hot Brown Morning Potion: 2, Shot Glass: 1, Roses: 1",
        )

        # Removing items
        inventory._remove_item(cii.item_water)
        inventory._remove_item(cii.item_shot) # Reusable Item!
        inventory._remove_item(cii.item_rose)
        self.assertEqual(
            first=inventory.list_items(),
            second="Water: 4, Hot Brown Morning Potion: 2, Shot Glass: 1",
        )

        # Using items requires girlfriend to be defined... so nvm for now lol


if __name__ == '__main__':
    unittest.main()