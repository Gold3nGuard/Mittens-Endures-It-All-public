init -4 python:
    # from abc import ABC, abstractmethod
    from abc import abstractmethod
    from dataclasses import dataclass
    class Girlfriend: pass # Forward declare the Girlfriend class for type hinting.

    # # Initialize logging
    # import logging
    # logger = logging.getLogger("InventoryItems.rpy")
    # import os
    # from pathlib import Path
    # import logging 
    # logger = logging.getLogger("InventoryItems.py")
    # logfile: str = f"{os.getcwd()}/logs/InventoryItems.log"
    # logdir: str = logfile.rsplit('/', 1)[0]
    # Path(logdir).mkdir(parents=True, exist_ok=True)
    # if not os.path.exists(logfile):
    #     with open(logfile, "w"):
    #         pass
    # logging.basicConfig(filename=logfile, level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(name)s %(message)s")

    # class Singleton(type, ABC):
    #     """Prevent multiple instantiations of each item type"""

    #     # Store single instances of each class
    #     _instances = {}

    #     def __call__(cls, *args, **kwargs):
    #         # If class hasn't been instantiated yet, we may instantiate it and then store it in Singleton.
    #         if cls not in cls._instances:
    #             cls._instances[cls] = super().__call__(*args, **kwargs)
    #         # Otherwise, send a warning that a singleton class attempted to instantiate more than once
    #         else:
    #             logger.warning(f"Attempted to instantiate another instance of {cls}. {cls} has already been instantiated!")
    #             print(f"Attempted to instantiate another instance of {cls}. {cls} has already been instantiated!")
    #         # Return the stored class
    #         return cls._instances[cls]


    class InventoryItem(metaclass = Singleton):
        """Abstract base class for inventory items
        
        Args:
            _name (str): 
            _description (str): 
            _cost (int): 
            _quantity_in_inventory (int): 
            _remove_upon_use (bool): 
        """

        _instances = {}

        # Do not instantiate the following abstract classes
        def __new__(cls, *args, **kwargs):
            if cls is InventoryItem or \
            cls is ConsumableLiquid or \
            cls is MoodAlteringItem or \
            cls is LiquidContainerItem or \
            cls is Keys:
                raise TypeError(f"{cls} is an abstract class. It cannot be instantiated!")
            else:
                return object.__new__(cls, *args, **kwargs)

        # Attributes for all items
        _name: str
        _plural_name: str
        _description: str
        _cost: int
        _quantity_in_inventory: int

        # Getters and setters
        @property
        def name(self):
            return self._name

        @property
        def plural_name(self):
            return self._plural_name

        @property
        def description(self):
            return self._description

        @property
        def cost(self):
            return self._cost

        @property
        def quantity_in_inventory(self) -> int:
            return self._quantity_in_inventory

        @property 
        def remove_upon_use(self) -> bool:
            return True         

        @quantity_in_inventory.setter
        def quantity_in_inventory(self, value: int):
            self._quantity_in_inventory = value

        @abstractmethod
        def use_item(self, girlfriend: Girlfriend, **kwargs) -> bool:
            """Tells the game what happens after you use the item. 
            This is an abstract method intended to be implemented by concrete classes.
            """
            pass


    class ConsumableLiquid(InventoryItem):
        """Abstract base class for consumable liquids
        
        Args:
            _volume (int): 
            _menu_option_text (str): The text to display as an option in menus
            _diuretic_level (int): Defaults as 0
            _show_in_all_relevant_choice_menus (bool): Indicates whether this item should be displayed in all 
                    relevant choice menus that offer use of consumable liquids. 
                    Defaults as True. # Only False for Artisan Grape Blood
            _consumption_confirmation_response (str): The response your girlfriend gives after consuming the item. 
                    Defaults as "Hmm, refreshing!"
            _amount_girlfriend_drank (int): Amount of the liquid that your girlfriend drank. Defaults to 0.
        """

        _volume: int
        _menu_option_text: str
        _diuretic_level: int = 0
        _show_in_all_relevant_choice_menus: bool = True # Only False for Artisan Grape Blood
        _consumption_confirmation_response: str = "Hmm, refreshing!"
        _amount_girlfriend_drank: int = 0

        @property
        def volume(self):
            return self._volume

        @property
        def diuretic_level(self):
            return self._diuretic_level

        @property 
        def menu_option_text(self):
            return self._menu_option_text

        @property 
        def consumption_confirmation_response(self) -> str:
            return self._consumption_confirmation_response

        @property 
        def show_in_all_relevant_choice_menus(self) -> bool:
            return self._show_in_all_relevant_choice_menus

        @property
        def amount_girlfriend_drank(self) -> int:
            return self._amount_girlfriend_drank

        @amount_girlfriend_drank.setter 
        def amount_girlfriend_drank(self, value: int):
            if value >= 0:
                self._amount_girlfriend_drank = value
            else:
                raise ValueError("Quantity drank cannot be zero!")

        def use_item(self, girlfriend: Girlfriend) -> bool:
            """Upon use of item, add the liquid to her tummy and increase diuretic level if appropriate.
            """
            if girlfriend.tummy <= girlfriend.tummy_capacity:
                girlfriend.tummy += self._volume
                girlfriend.diuretic_level += self._diuretic_level
                girlfriend.drank_inventory.girlfriend_drank_item(item = self)
                return True
            else:
                return False


    class MoodAlteringItem(InventoryItem):
        """Abstract base class for items that alter your girlfriend's mood or shyness
        
        Args:
            _consumption_confirmation_response (str): The response your girlfriend gives after consuming the item. 
            _consumption_emergency_response (str): gf's response to receiving the item when having a bladder emergency.
            _bribery_response (str): gf's response to using this item as a bribe to continue holding her pee. 
            _menu_option_text (str): The text to display as an option in menus
            _delta_mood (int): The change in mood when she doesn't have a bladder emergency
            _delta_shyness (int): The change in shyness when she doesn't have a bladder emergency
            _delta_mood_emergency (int): The change in mood when she has a bladder emergency
            _delta_shyness_emergency (int): The change in shyness when she has a bladder emergency
        """

        _consumption_confirmation_response: str
        _consumption_emergency_response: str
        _bribery_response: str
        _menu_option_text: str
        _delta_mood: int = 0
        _delta_shyness: int = 0
        _delta_mood_emergency: int = 0
        _delta_shyness_emergency: int = 0
        _turns_to_wait_after_use: int = 2

        @property 
        def menu_option_text(self):
            return self._menu_option_text

        @property 
        def consumption_confirmation_response(self) -> str:
            return self._consumption_confirmation_response

        @property 
        def consumption_emergency_response(self) -> str:
            return self._consumption_emergency_response

        @property 
        def bribery_response(self) -> str:
            return self._bribery_response

        def use_item(self, girlfriend: Girlfriend) -> bool:
            if (girlfriend.bladder < girlfriend.bladder_emergency):
                girlfriend.mood += self._delta_mood
                girlfriend.shyness += self._delta_shyness
            else:
                girlfriend.mood += self._delta_mood_emergency
                girlfriend.shyness += self._delta_shyness_emergency
                girlfriend.turns_to_wait_before_asking = self._turns_to_wait_after_use
            return True

    class LiquidContainerItem(InventoryItem):
        """Abstract base class for items that can contain liquids (i.e. urine)"""
        _capacity: int
        _gf_peed_in_previously: bool = False # Has gf previously peed in this container?

        @property
        def gf_peed_in_previously(self):
            return self._gf_peed_in_previously

        @gf_peed_in_previously.setter
        def gf_peed_in_previously(self, value: bool):
            self._gf_peed_in_previously = value

        @property 
        def remove_upon_use(self) -> bool:
            return False 

    class Keys(InventoryItem):
        """Abstract base class for keys, which can open locked doors"""
        _door_id: str 

        def open_door(self, door: str) -> bool:
            return self._door_id == door


    # ===== Concrete definition of in-game items ===== #

    # --- Bonesborough Marketplace Items --- #

    class Water(ConsumableLiquid):
        """Increases tummy
        """
        _name = "Water"
        _plural_name = "bottles of water"
        _volume = 500
        _description = f"A {_volume}mL bottle of water"
        _cost = 5
        _menu_option_text = "Give her a bottle of water."


    class WaterWithDiuretic(ConsumableLiquid):
        """Increases tummy and diuretic level
        """
        _name = "Water With Diuretic"
        _plural_name = "bottles of diuretic laced water"
        _volume = 500
        _description = f"A {_volume}mL bottle of water with some diuretic mixed in"
        _diuretic_level = 200
        _cost = 40
        _menu_option_text = "Give her a bottle of water with the diuretic."


    class HotBrownMorningPotion(ConsumableLiquid):
        """Increases tummy and diuretic level
        """
        _name = "Hot Brown Morning Potion"
        _plural_name = "Hot Brown Morning Potions"
        _volume = 600
        _description = f"A {_volume}mL thermos of Hot Brown Morning Potion. Imported fresh from Xadia this afternoon."
        _diuretic_level = 50
        _cost = 10
        _menu_option_text = "Give her some Hot Brown Morning Potion."
        _consumption_confirmation_response = "Whoa, this was imported from Xadia this afternoon?! No way! It's delicious!"


    class BouquetOfRoses(MoodAlteringItem):
        """Increases mood and decreases shyness
        """
        _name = "Roses"
        _plural_name = "bouquets of roses"
        _description = "A bouquet of pretty roses my beautiful girlfriend!"
        _cost = 20
        _menu_option_text = "Give her a bouquet of roses."
        _consumption_confirmation_response = "Thanks! They're beautiful."
        _consumption_emergency_response = "Thanks for the flowers, but I really need to pee."
        _bribery_response = "Ok, for roses..."
        _delta_mood = 10
        _delta_mood_emergency = 7

    class AzuraDiamondEarring(MoodAlteringItem):
        """Increases mood and decreases shyness
        """
        _name = "Azura Themed Diamond Earrings"
        _plural_name = "Azura Themed Diamond Earrings"
        _description = "Any fan of the Azura series would find this pair of earrings adorable!"
        _cost = 60
        _menu_option_text = "Give her a pair of Azura themed diamond earrings."
        _consumption_confirmation_response = "OMG! Azura themed earrings!? They're so beautiful, thank you so much!"
        _consumption_emergency_response = "Thanks for the earrings, but I really need to pee."
        _bribery_response = "OMG! Azura themed earrings!? I'd have done much more than hold my pee for these, you got a deal!"
        _delta_mood = 30
        _delta_mood_emergency = 25

    class FlowerVase(LiquidContainerItem):
        """Can be used to contain liquids in case of emergencies...
        """
        _name = "Flower Vase"
        _plural_name = "flower vases"
        _capacity = 2000
        _description = f"This flower vase has a capacity of {_capacity}mL"
        _cost = 30
        _menu_option_text = "Give her a vase."


    class ShotGlass(LiquidContainerItem):
        """Can be used to contain liquids in case of emergencies...
        """
        _name = "Shot Glass"
        _plural_name = "shot glasses"
        _capacity = 50
        _description = f"This shot glass has a capacity of {_capacity}mL"
        _cost = 10
        _menu_option_text = "Give her a shot glass."


    class PaperTowelRoll(LiquidContainerItem):
        """Can be used to contain liquids in case of emergencies...
        """
        _name = "Paper Towel Roll"
        _plural_name = "rolls of paper towels"
        _capacity = 3000
        _description = f"This roll of paper towels is extra absorbent! Rumour has it a whole roll can soak up to {_capacity}mL of liquid!"
        _cost = 30
        _menu_option_text = "Give her a roll of paper towels."


    class SexyPanties(InventoryItem):
        """A sexy piece of fabric that barely covers anything
        """
        _name = "Sexy Panties"
        _plural_name = "pairs of sexy panties"
        _description = f"A sexy piece of fabric that barely covers anything."
        _cost = 30
        _menu_option_text = "Give her a sexy pair of panties."


    class ArtisanGrapeBlood(ConsumableLiquid):
        """Increases tummy and diuretic level
        """
        _name = "Artisan Grape Blood"
        _plural_name = "bottles of Artisan Grape Blood"
        _volume = 50
        _description = f"The finest grape blood that was available at the Bonesborough Marketplace on a Tuesday afternoon."
        _diuretic_level = 30
        _cost = 50
        _menu_option_text = "Give her some artisan grape blood."
        _show_in_all_relevant_choice_menus = False

    # --- Keys --- #
