import unittest  # noqa: N999


class TestInventorySystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # Extract the Python code and import the package
        from tests.utils.extractPython import extractPy
        extractPy('game/src/py/utils/Singleton.rpy', 'tests/src/')
        extractPy('game/src/py/Time.rpy', 'tests/src/')
        extractPy('game/src/py/inventory/InventoryItems.rpy', 'tests/src/')

        global PlayerInventory  # ty: ignore[unresolved-global]
        from tests.src.PlayerInventory import PlayerInventory

    def test_default_snails(self):
        inventory = PlayerInventory()
        self.assertEqual(inventory.snails, 150)

if __name__ == '__main__':
    unittest.main()