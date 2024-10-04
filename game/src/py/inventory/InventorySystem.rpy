init -3 python:

    from typing import Dict
    from enum import Enum

    class RemoveItemConfirmationState(Enum):
        """A set of enums that indicates why an item may not have been consumed.
        """
        NO_STATE_GIVEN_CHECK_CODE = 0
        ITEM_CONSUMED_SUCCESSFULLY = 1
        GIRLFRIEND_REFUSED_CONSUMPTION = 2
        ITEM_NOT_IN_INVENTORY = 3
        ITEM_CAN_BE_REUSED = 4


    class ItemNotInInventoryError(ValueError):
        pass

    class Inventory():
        """A class to manage the in-game inventory system
        """

        def __init__(self):
            """
            _items (Dict[str, InventoryItem]): The items that are currently in the inventory. Initializes to {}
            _snails (int): The currency system used in the Boiling Isles.
            _snails_confirmation_msg (str): A message to describe how a purchase was successful, if it was. May be deprecated in future.
            _is_purchase_valid (bool): 
            """

            self._items: Dict[str, InventoryItem] = {}
            self._snails: int = 150
            # self._snails: int = 2000
            self._snails_confirmation_msg: str = ""
            self._is_purchase_valid: bool = False

        def list_items(self, withNewlines: bool = False) -> str: 
            """Lists the items in the inventory in text form.
            """
            newlines = "\n" if withNewlines else ""
            if self._items == {}:
                output_string = "I'm not carrying anything" 
            else:
                output_string = ""
                for item in self._items:
                    output_string = output_string + item + f": {self._items[item].quantity_in_inventory}, " + newlines
                output_string = output_string.strip(", \n")

            return output_string

        def list_drank(self, withNewlines: bool = False) -> str:
            """Lists the items your girlfriend has drank since she last peed.
            """
            newlines = "\n" if withNewlines else ""
            if self._items == {}:
                output_string = "I'm not carrying anything" 
            else:
                output_string = ""
                for item in self._items:
                    output_string = output_string + item + f": {self._items[item].amount_girlfriend_drank}, " + newlines
                output_string = output_string.strip(", \n")

            return output_string

        def __str__(self) -> str:
            return self.list_items()

        def __contains__(self, item: InventoryItem) -> bool:
            """Checks if the item is in the inventory

            Args:
                item (InventoryItem): An in-game item

            Returns:
                bool: Returns true if the item was found in the inventory
            """
            for i in self._items:
                if i == item.name:
                    return True 
            return False

        @property
        def hasUniversalConsumableLiquid(self) -> bool:
            """Check if inventory has any universal ConsumableLiquids

            Return:
                bool: Returns true if there is a universal consumable liquid in the inventory
            """
            for key in self._items:
                if isinstance(self._items[key], ConsumableLiquid):
                    if self._items[key].show_in_all_relevant_choice_menus:
                        return True 
            return False

        @property
        def hasMoodAlteringItem(self) -> bool:
            """Check if inventory has any universal ConsumableLiquids

            Return:
                bool: Returns true if there is a universal consumable liquid in the inventory
            """
            for key in self._items:
                if isinstance(self._items[key], MoodAlteringItem):
                    return True 
            return False

        @property
        def items(self) -> Dict:
            return self._items

        # @items.setter
        # def items(self, value) -> bool:
        #     """Item setter method for transaction validation.
        #     """
        #     self._items = value
        #     return True

        @property
        def snails(self) -> int:
            return self._snails

        @snails.setter
        def snails(self, value):

            self.reset_snails_conf_msg()
            self._is_purchase_valid = False

            if value < 0:
                msg = "Transaction unsuccessful, not enough snails!" 
                self._is_purchase_valid = False
            elif value > 999999:
                msg = "Not enough room in wallet to hold all these snails!"
                self._is_purchase_valid = False
            else:
                self._snails = value
                msg = "Transaction successful!"
                self._is_purchase_valid = True
            
            self._snails_confirmation_msg = msg

        @property
        def snails_confirmation_msg(self) -> str:
            return self._snails_confirmation_msg
        
        @snails_confirmation_msg.setter
        def snails_confirmation_msg(self, value):
            self._snails_confirmation_msg = value 

        def reset_snails_conf_msg(self):
            self._snails_confirmation_msg = ""

        @property
        def is_purchase_valid(self) -> bool:
            return self._is_purchase_valid

        @is_purchase_valid.setter
        def is_purchase_valid(self, value: bool):
            self._is_purchase_valid = value

        @property
        def consumableLiquidsUniversalMenuChoices(self) -> list:
            """Returns a list of consumable liquids in your inventory to use in relevant menus.
            """
            choices = []
            for key in self._items:
                print(key)
                item = self._items[key]
                if isinstance(item, ConsumableLiquid) and item.show_in_all_relevant_choice_menus:
                    choices.append(item.menu_option_text)
            return choices


        # ===== Inventory management methods ===== #

        def __add_item(self, item: InventoryItem, quantity: int):
            """Adds the item to the inventory.

            Args:
                item (InventoryItem): The item to add to your inventory.
                quantity (int): The quantity of the item to add to your inventory.
                girlfriendDrank (bool): Indicates whether item was added to girlfriend's drank inventory.
            """

            # If an identical item is not already in the inventory, then add the item as a new item to the inventory
            if item not in self:
                self._items[item.name] = item
                self._items[item.name].quantity_in_inventory = 0

            # Increment the quantity of that item in the inventory
            self._items[item.name].quantity_in_inventory += quantity

        def girlfriend_drank_item(self, item: InventoryItem):
            """Adds the item to girlfriend's drank inventory tracker. 
            Which tracks which liquids your gf has drank since her last pee,
            and how much.
            
            Args:
                item (InventoryItem): The item to add to your inventory.
            """
            # If an identical item is not already in the inventory, then add the item as a new item to the inventory
            if item not in self:
                self._items[item.name] = item
                self._items[item.name].amount_girlfriend_drank = 0

            # Increment the quantity of that item in the inventory
            self._items[item.name].amount_girlfriend_drank += 1


        def add_item_without_purchase(self, item: InventoryItem, quantity: int = 1):
            """Adds the item to the inventory without purchasing. Meant to be used in debug mode only!

            Actually, some items (like keys) can be added without purchasing. But those should have a cost of 0.
            """

            self.__add_item(item, quantity)


        def attemptPurchaseItem(self, item: InventoryItem) -> int:
            """Attempts to purchase the item and add it to the inventory

            Args:
                item (InventoryItem): The item you're attempting to purtchase.

            bool: Returns the quantity purchased. Returns -1 if purchase was unsuccessful.
            """

            # Ask for a quantity prompt
            quantity: int = int(renpy.input(prompt=f"How many {item.plural_name} do you want to purchase?", default="1", allow="0123456789", length=16))

            # This statement should properly update self.is_purchase_valid in the self.snails setter
            self.snails -= item.cost * quantity

            # If the purchase was valid, add the item to the inventory
            if self.is_purchase_valid:
                self.__add_item(item, quantity)
            else:
                quantity = -1 

            return quantity


        def __remove_item(self, item: InventoryItem) -> bool:
            """Removes one copy of the item from the inventory if it exists in the inventory.

            Args:
                item (InventoryItem): The item to remove from inventory
            
            bool: Returns a bool to indicate whether the item was removed
            """

            # Check if item is in inventory
            if item in self:

                # Then remove one copy of it
                item.quantity_in_inventory -= 1

                # If no more of the item remains, remove it from inventory
                if item.quantity_in_inventory <= 0:
                    self._items.pop(item.name)
                    
                # Indicate that the item was removed
                return True

            # Indicate that item was not found in the inventory, and thus not removed
            else: 
                return False


        def attemptUseItem(self, item: InventoryItem, girlfriend: Girlfriend = None) -> RemoveItemConfirmationState:
            """Attempts to use the item

            Args:
                item (InventoryItem): The item to use
                girlfriend (Girlfriend): girlfriend that item use might affect. Defaults to None
            
            RemoveItemConfirmationState: Returns an enum that tells the program what happened to the item and how to react.
            """

            # Define local variables
            confirmation_state: RemoveItemConfirmationState = RemoveItemConfirmationState.NO_STATE_GIVEN_CHECK_CODE
            item_used: bool = False

            # Check if item is in inventory
            if item in self:

                # Figure out type of item and use accordingly

                # For consumable liquids
                if isinstance(item, ConsumableLiquid):
                    if girlfriend is None:
                        raise ValueError("`girlfriend` needs to be specified when using Consumable Liquids.")
                    else:
                        # TODO: Implement the use of the consumable liquid here
                        item_used: bool = item.use_item(girlfriend)

                # For mood altering items
                elif isinstance(item, MoodAlteringItem):
                    if girlfriend is None:
                        raise ValueError("`girlfriend` needs to be specified when using Consumable Liquids.")
                    else:
                        # TODO: Implement the use of the consumable liquid here
                        item_used: bool = item.use_item(girlfriend)
                
                else:
                    # TODO: Implement the use of other items with elif!
                    item_used: bool = item.use_item(girlfriend)


                # Check if item was successfully used, remove it, then update the confirmation state
                if item_used:
                    if item.remove_upon_use:
                        # Update confirmation state
                        confirmation_state = RemoveItemConfirmationState.ITEM_CONSUMED_SUCCESSFULLY
                        successfully_removed = self.__remove_item(item)
                        if not successfully_removed:
                            raise ValueError(f"{item.name} was not removed from the inventory. Check the Inventory.__remove_item() method")
                    else:
                        # Don't remove item if it's reusable
                        # TODO: Test this when I implement LiquidContainerItem's better
                        confirmation_state = RemoveItemConfirmationState.ITEM_CAN_BE_REUSED
                else: 
                    confirmation_state = RemoveItemConfirmationState.GIRLFRIEND_REFUSED_CONSUMPTION

            # If item not in inventory, update confirmation state
            else:
                confirmation_state = RemoveItemConfirmationState.ITEM_NOT_IN_INVENTORY

            return confirmation_state

                  
