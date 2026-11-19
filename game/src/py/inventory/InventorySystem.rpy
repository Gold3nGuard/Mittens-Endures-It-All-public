init -5 python:

    from abc import ABC, abstractmethod
    from typing import TypedDict
    from enum import Enum
    from dataclasses import dataclass, field
    from typing import ClassVar
    import warnings

    # Required for unit tests
    if __name__ != 'store':
        from tests.src.Time import Time

    # Place abstract and tracker inventories here
    class RemoveItemConfirmationState(Enum):
        """A set of enums that indicates why an item may not have been consumed.
        """
        NO_STATE_GIVEN_CHECK_CODE = 0
        ITEM_CONSUMED_SUCCESSFULLY = 1
        GIRLFRIEND_REFUSED_CONSUMPTION = 2
        ITEM_NOT_IN_INVENTORY = 3
        ITEM_CAN_BE_REUSED = 4
        NOT_ENOUGH_OF_ITEM_TO_REMOVE = 5
        ITEM_REMOVED_SUCCESSFULLY = 6

    class PurchaseFailedState(Enum):
        """A set of enums that indicate why an item wasn't purchased.
        """
        NOT_ENOUGH_SNAILS = -1

    @dataclass(frozen=True, kw_only=True)
    class InventoryItem(ABC):
        """Abstract base class for inventory items
        
        Args:
            _name (str): 
            _description (str): 
            _cost (int): 
            _remove_upon_use (bool): 
        """

        # _instances: ClassVar[dict] = {}

        # # Do not instantiate the following abstract classes
        # def __new__(cls, *args, **kwargs):
        #     if cls is InventoryItem or \
        #     cls is ConsumableLiquid or \
        #     cls is MoodAlteringItem or \
        #     cls is LiquidContainerItem or \
        #     cls is Keys:
        #         raise TypeError(f"{cls} is an abstract class. It cannot be instantiated!")
        #     else:
        #         print(cls)
        #         return object.__new__(cls, *args, **kwargs)

        # Attributes for all items
        name: str
        plural_name: str
        description: str
        cost: int
        remove_upon_use: bool 

        @abstractmethod
        def use_item(
            self, 
            girlfriend = None, 
            gametime: Time | None = None, 
            **kwargs
            ) -> bool:
            """Tells the game what happens after you use the item. 
            This is an abstract method intended to be implemented by concrete classes.
            """
            pass

    class AbstractInventory(ABC):
        """A class to manage the in-game inventory system
        TODO: I need to restructure this class! 
        Make an AbstractInventory class with children:
        - ItemsInventory for all items the main character obtains and interacts with (only one should be instantiated for the main character)
        - DrinksInventory for liquids that are consumed by both main character and gf (two of these should be created)
        and make ItemsInventory backwards compatible with everything I've written so far LOL.
        """

        def __init__(self):
            self.items: dict[InventoryItem, int] = {}

        def __contains__(self, item: InventoryItem) -> bool:
            """Checks if the item is in the inventory

            Args:
                item (InventoryItem): An in-game item

            Returns:
                bool: Returns true if the item was found in the inventory
            """
            return item in self.items and self.items[item] > 0

        def __repr__(self):
            return f"{type(self).__name__}(items={self.items})"

        def list_items(self, withNewlines: bool = False) -> str: 
            """Lists the items in the inventory in text form.
            """
            newlines = "\n" if withNewlines else ""
            if self.items == {}:
                output_string = "I'm not carrying anything" 
            else:
                output_string = ""
                for item in self.items:
                    output_string = output_string + item.name + f": {self.items[item]}, " + newlines
                output_string = output_string.strip(", \n")

            return output_string
        
        def __str__(self) -> str:
            return self.list_items()
    

        # ===== Inventory management methods ===== #

        def _add_item(
            self, 
            item: InventoryItem, 
            quantity: int = 1,
            ):
            """Adds the item to the inventory.

            Args:
                item (InventoryItem): The item to add to your inventory.
                quantity (int): The quantity of the item to add to your inventory.
            """

            if quantity < 0:
                warnings.warn(message="quantity must be non-negative")
                return
            elif quantity == 0:
                # Do nothing if nothing is added
                return

            if item in self:
                self.items[item] += quantity
            else:
                self.items[item] = quantity


        def _remove_item(
            self, 
            item: InventoryItem, 
            quantity: int = 1,
            ) -> RemoveItemConfirmationState:
            """
            Attempts to remove some quantity of item from the inventory

            Args:
                item (InventoryItem): The item to remove from inventory
                quantity (int): The amount of item to remove from inventory
            
            RemoveItemConfirmationState: Returns a state indicating a successful removal, 
            or reason why removal was not possible
            """

            # Check if item is in the inventory
            if item not in self:
                warnings.warn(message=f"{item.name} not found in inventory!")
                return RemoveItemConfirmationState.ITEM_NOT_IN_INVENTORY
                
            # Check if there's enough of item to remove
            if quantity > self.items[item]:
                warnings.warn(message=f"Not enough {item.name} in inventory to remove!")
                return RemoveItemConfirmationState.NOT_ENOUGH_OF_ITEM_TO_REMOVE

            # Decrease quantity if not reusable
            if item.remove_upon_use:
                self.items[item] -= quantity

            # Remove from inventory if none left
            if self.items[item] <= 0:
                self.items.pop(item)

            return RemoveItemConfirmationState.ITEM_REMOVED_SUCCESSFULLY

    class DrinksTracker(AbstractInventory): 

        def add_drink(self, drink: InventoryItem, quantity: int = 1):
            self._add_item(item=drink, quantity=quantity)

        def list_drinks(self):
            drinks_list = []
            for drink, amount in self.items.items():
                if amount == 1:
                    drinks_list.append(f"{amount} {drink.name}")
                elif amount > 1:
                    drinks_list.append(f"{amount} {drink.plural_name}")
            drinks_list_str = ", ".join(drinks_list)
            return drinks_list_str
            
        def reset(self): # girlfriend.pees() should call this method!!!
            self.items.clear()
