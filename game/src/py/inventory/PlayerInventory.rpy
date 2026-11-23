init -3 python:

    # Required for unit testing
    if __name__ != 'store':
        from tests.src.InventorySystem import *
        from tests.src.InventoryItems import *

    class PlayerInventory(AbstractInventory): 
        def __init__(
            self, 
            snails: int = 150, 
            items: dict[InventoryItem, int] | None = None
            ):
            super().__init__()
            self._snails: int = snails
            self._snails_confirmation_msg: str = ""
            self._is_purchase_valid: bool = False
            self.items = items if items is not None else {}

        def __repr__(self):
            return f"ItemInventory(snails={self._snails}, items={self.items})"

        @property
        def hasUniversalConsumableLiquid(self) -> bool:
            """Check if inventory has any universal ConsumableLiquids

            Return:
                bool: Returns true if there is a universal consumable liquid in the inventory
            """
            for item in self.items:
                if isinstance(item, ConsumableLiquid) and item.show_in_all_relevant_choice_menus:
                    return True 
            return False

        @property
        def hasMoodAlteringItem(self) -> bool:
            """Check if inventory has any MoodAlteringItem

            Return:
                bool: Returns true if there is a MoodAlteringItem in the inventory
            """
            for item in self.items:
                if isinstance(item, MoodAlteringItem):
                    return True 
            return False

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
            for item in self.items:
                if isinstance(item, ConsumableLiquid) and item.show_in_all_relevant_choice_menus:
                    choices.append(item.menu_option_text)
            return choices

        def attemptPurchaseItem(self, item: InventoryItem) -> int:
            """Attempts to purchase the item and add it to the inventory

            Args:
                item (InventoryItem): The item you're attempting to purtchase.

            bool: Returns the quantity purchased. Returns -1 if purchase was unsuccessful.
            """

            # Ask for a quantity prompt
            quantity_prompt: str = renpy.input(
                    prompt=f"How many {item.plural_name} do you want to purchase?${item.cost}", 
                    default="1", 
                    allow="0123456789", 
                    length=16,
                    screen="purchase_item_input_screen"
                    )
            quantity: int = int(quantity_prompt) if quantity_prompt else 0

            total_cost = item.cost * quantity
            # If the purchase costs too much, deny the transaction
            if total_cost > self.snails:
                quantity = PurchaseFailedState.NOT_ENOUGH_SNAILS.value
            else:
                self.snails -= item.cost * quantity
                self._add_item(item, quantity)

            return quantity

        def add_item_without_purchase(self, item: InventoryItem, quantity: int = 1):
            """Adds the item to the inventory without purchasing. Meant to be used in debug mode only!

            Actually, some items (like keys) can be added without purchasing. But those should have a cost of 0.
            """

            self._add_item(item, quantity)

        def attemptUseItem(
            self, 
            item: InventoryItem, 
            girlfriend: Girlfriend | None = None, 
            gametime: Time | None = None,
            ) -> RemoveItemConfirmationState:
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

                # For ConsumableLiquid
                if isinstance(item, ConsumableLiquid):
                    if girlfriend is None:
                        raise ValueError("`girlfriend` needs to be specified when using ConsumableLiquid.")
                    else:
                        # TODO: Implement the use of the consumable liquid here
                        item_used: bool = item.use_item(girlfriend=girlfriend)

                # For MoodAlteringItem
                elif isinstance(item, MoodAlteringItem):
                    if girlfriend is None:
                        raise ValueError("`girlfriend` needs to be specified when using MoodAlteringItem.")
                    else:
                        # TODO: Implement the use of the consumable liquid here
                        item_used: bool = item.use_item(girlfriend)

                # For LiquidContainerItem
                elif isinstance(item, LiquidContainerItem):
                    if isinstance(item, PaperTowelRoll) and girlfriend is None:
                        # There are two ways to use paper towels, to wipe, and as a container.
                        # This is the to wipe case
                        item_used: bool = item.use_item(girlfriend, gametime = None)
                    elif girlfriend is None:
                        raise ValueError("`girlfriend` needs to be specified when using LiquidContainerItem.")
                    elif gametime is None:
                        raise ValueError("`gametime` needs to be specified when using LiquidContainerItem")
                    else:
                        # TODO: Implement the use of the consumable liquid here
                        item_used: bool = item.use_item(girlfriend, gametime)

                else:
                    # TODO: Implement the use of other items with elif!
                    item_used: bool = item.use_item(girlfriend)


                # Check if item was successfully used, remove it, then update the confirmation state
                if item_used:
                    if item.remove_upon_use:
                        # Update confirmation state
                        confirmation_state = RemoveItemConfirmationState.ITEM_CONSUMED_SUCCESSFULLY
                        successfully_removed = self._remove_item(item)
                        if successfully_removed != RemoveItemConfirmationState.ITEM_REMOVED_SUCCESSFULLY:
                            raise ValueError(f"{item.name} was not removed from the inventory. Check the Inventory._remove_item() method")
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
