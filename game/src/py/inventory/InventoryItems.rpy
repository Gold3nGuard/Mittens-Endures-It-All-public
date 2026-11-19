init -4 python:

    from abc import ABC
    from dataclasses import dataclass
    import warnings
    from enum import Enum, auto

    # Required for unit testing
    if __name__ != 'store':
        from tests.src.Time import Time
        from tests.src.InventorySystem import InventoryItem

    class Girlfriend: pass

    @dataclass(frozen=True,kw_only=True)
    class ConsumableLiquid(InventoryItem, ABC):
        """Abstract base class for consumable liquids
        
        Args:
            volume (int): The volume of the liquid in mL.
            _menu_option_text (str): The text to display as an option in menus.
            _diuretic_level (int): Defaults as 0.
            _show_in_all_relevant_choice_menus (bool): Indicates whether this item should be displayed in all 
                    relevant choice menus that offer use of consumable liquids. 
                    Defaults as True. # Only False for Artisan Grape Blood
            _consumption_confirmation_response (str): The response your girlfriend gives after consuming the item. 
                    Defaults as "Hmm, refreshing!"
        """

        volume: int
        _menu_option_text: str = ""
        _diuretic_level: int = 0
        _show_in_all_relevant_choice_menus: bool = True # Only False for Artisan Grape Blood
        _consumption_confirmation_response: str = "Hmm, refreshing!"

        @property
        def volume(self):
            return self.volume

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

        def use_item(self, girlfriend: Girlfriend | None = None, gametime: Time | None = None, **kwargs) -> bool:
            """Upon use of item, add the liquid to her tummy and increase diuretic level if appropriate.
            """
            if girlfriend is None: warnings.warn("`girlfriend` must be defined in ConsumableLiquid.use_item()")
            if girlfriend.tummy <= girlfriend.tummy_capacity:
                girlfriend.tummy += self.volume
                girlfriend.diuretic_level += self._diuretic_level
                girlfriend.drank_inventory.add_drink(drink=self, quantity=1)
                return True
            else:
                return False

    @dataclass(frozen=True,kw_only=True)
    class MoodAlteringItem(InventoryItem, ABC):
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

        def use_item(self, girlfriend: Girlfriend | None = None, gametime: Time | None = None, **kwargs) -> bool:
            if girlfriend is None: warnings.warn("`girlfriend` must be defined in MoodAlteringItem.use_item()")
            if (girlfriend.bladder < girlfriend.bladder_emergency):
                girlfriend.mood += self._delta_mood
                girlfriend.shyness += self._delta_shyness
            else:
                girlfriend.mood += self._delta_mood_emergency
                girlfriend.shyness += self._delta_shyness_emergency
                girlfriend.turns_to_wait_before_asking = self._turns_to_wait_after_use
            return True

    @dataclass(frozen=True,kw_only=True)
    class LiquidContainerItem(InventoryItem, ABC):
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

        def use_item(self, girlfriend: Girlfriend | None = None, gametime: Time | None = None, **kwargs) -> bool:
            """Upon use of item, girlfriend pees a little bit into the container (decreases bladder)
            """
            if girlfriend is None or gametime is None: warnings.warn("Both `girlfriend` and `gametime` must be defined in LiquidContainerItem.use_item()")
            if gametime is not None:
                # NOTICE: To have gf pee in container, you MUST provide the current `gametime`
                # Assume that gametime = None means we are using paper towels to wipe. 
                # Otherwise, we must include the `gametime`
                if (self._capacity >= girlfriend.bladder):
                    girlfriend.flush_drank_inventory(gametime)
                else:
                    girlfriend.bladder -= self._capacity

            return True


    class Door(Enum):
        COVENTION_HALL_PLAY = auto()
        GRIMGRUBS_PUB = auto()
        NIGHTCLUB_DANCE_VENUE = auto()

    @dataclass(frozen=True,kw_only=True)
    class Keys(InventoryItem, ABC):
        """Abstract base class for keys, which can open locked doors"""
        door_id: Door 
        cost: int = 0
        remove_upon_use: bool = False

        def open_door(self, door: Door) -> bool:
            """
            Returns true if this key is able to open the door.
            """
            return self.door_id == door

        
    # ===== Concrete definition of in-game items ===== #

    # --- Bonesborough Marketplace Items --- #

    @dataclass(frozen=True)
    class Water(ConsumableLiquid):
        """Increases tummy
        """
        name: str = "Water"
        plural_name: str = "bottles of water"
        volume: int = 500
        description: str = f"A {volume}mL bottle of water"
        cost: int = 5
        _menu_option_text: str = "Give her a bottle of water."
        remove_upon_use: bool = True


    @dataclass(frozen=True)
    class WaterWithDiuretic(ConsumableLiquid):
        """Increases tummy and diuretic level
        """
        name: str = "Water With Diuretic"
        plural_name: str = "bottles of diuretic laced water"
        volume: int = 500
        description: str = f"A {volume}mL bottle of water with some diuretic mixed in"
        _diuretic_level: int = 200
        cost: int = 40
        remove_upon_use: bool = True
        _menu_option_text: str = "Give her a bottle of water with the diuretic."


    @dataclass(frozen=True)
    class HotBrownMorningPotion(ConsumableLiquid):
        """Increases tummy and diuretic level
        """
        name: str = "Hot Brown Morning Potion"
        plural_name: str = "Hot Brown Morning Potions"
        volume: int = 600
        description: str = f"A {volume}mL thermos of Hot Brown Morning Potion. Imported fresh from Xadia this afternoon."
        _diuretic_level: int = 50
        cost: int = 10
        remove_upon_use: bool = True
        _menu_option_text: str = "Give her some Hot Brown Morning Potion."
        _consumption_confirmation_response: str = "Whoa, this was imported from Xadia this afternoon?! No way! It's delicious!"


    @dataclass(frozen=True)
    class AppleBlood(ConsumableLiquid):
        """Increases tummy and diuretic level (Formerly soda)
        """
        name: str = "Apple Blood"
        plural_name: str = "bottles of Apple Blood"
        volume: int = 500
        description: str = f"A {volume}mL bottle of non-alcholic Apple Blood. Contains diuretic"
        remove_upon_use: bool = True
        _diuretic_level: int = 30
        cost: int = 7
        _menu_option_text: str = "Give her a bottle of Apple Blood."
        _consumption_confirmation_response: str = "That was refreshing!"


    @dataclass(frozen=True)
    class BouquetOfRoses(MoodAlteringItem):
        """Increases mood and decreases shyness
        """
        name: str  = "Roses"
        plural_name: str  = "bouquets of roses"
        description: str  = "A bouquet of pretty roses my beautiful girlfriend!"
        cost: int = 20
        remove_upon_use: bool = True
        _consumption_confirmation_response: str  = "Thanks! They're beautiful."
        _consumption_emergency_response: str  = "Thanks for the flowers, but I really need to pee."
        _bribery_response: str  = "Ok, for roses..."
        _menu_option_text: str  = "Give her a bouquet of roses."
        _delta_mood: int = 10
        _delta_mood_emergency: int = 7

    @dataclass(frozen=True)
    class AzuraDiamondEarring(MoodAlteringItem):
        """Increases mood and decreases shyness
        """
        name: str  = "Azura Themed Diamond Earrings"
        plural_name: str  = "Azura Themed Diamond Earrings"
        description: str  = "Any fan of the Azura series would find this pair of earrings adorable!"
        cost: int = 60
        remove_upon_use: bool = True
        _menu_option_text: str  = "Give her a pair of Azura themed diamond earrings."
        _consumption_confirmation_response: str  = "OMG! Azura themed earrings!? They're so beautiful, thank you so much!"
        _consumption_emergency_response: str  = "Thanks for the earrings, but I really need to pee."
        _bribery_response: str  = "OMG! Azura themed earrings!? I'd have done much more than hold my pee for these, you got a deal!"
        _delta_mood: int = 30
        _delta_mood_emergency: int = 25

    @dataclass(frozen=True)
    class FlowerVase(LiquidContainerItem):
        """Can be used to contain liquids in case of emergencies...
        """
        name: str  = "Flower Vase"
        plural_name: str  = "flower vases"
        _capacity: int = 2000
        description: str = f"This flower vase has a capacity of {_capacity}mL"
        cost: int = 30
        remove_upon_use: bool = False
        _menu_option_text: str  = "Give her a vase."


    @dataclass(frozen=True)
    class ShotGlass(LiquidContainerItem):
        """Can be used to contain liquids in case of emergencies...
        """
        name: str  = "Shot Glass"
        plural_name: str  = "shot glasses"
        _capacity: int = 100
        description: str = f"This shot glass has a capacity of {_capacity}mL"
        cost: int = 10
        remove_upon_use: bool = False
        _menu_option_text: str  = "Give her a shot glass."


    @dataclass(frozen=True)
    class PaperTowelRoll(LiquidContainerItem):
        """Can be used to contain liquids in case of emergencies...
        """
        name: str  = "Paper Towel Roll"
        plural_name: str  = "rolls of paper towels"
        _capacity: int = 3000
        description: str = f"This roll of paper towels is extra absorbent! Rumour has it a whole roll can soak up to {_capacity}mL of liquid!"
        cost: int = 10
        remove_upon_use: bool = True
        _menu_option_text: str  = "Give her a roll of paper towels."


    @dataclass(frozen=True)
    class SexyPanties(InventoryItem):
        """A sexy piece of fabric that barely covers anything
        """
        name: str  = "Sexy Panties"
        plural_name: str  = "pairs of sexy panties"
        description: str = f"A sexy piece of fabric that barely covers anything."
        cost: int = 30
        remove_upon_use: bool = True
        _menu_option_text: str  = "Give her a sexy pair of panties."

        def use_item(
            self, 
            girlfriend = None, 
            gametime: Time | None = None, 
            **kwargs
            ) -> bool:
            return False

    @dataclass(frozen=True)
    class ArtisanGrapeBlood(ConsumableLiquid):
        """Increases tummy and diuretic level
        """
        name: str  = "Artisan Grape Blood"
        plural_name: str  = "bottles of Artisan Grape Blood"
        volume: int = 50
        description: str = f"The finest grape blood that was available at the Bonesborough Marketplace on a Tuesday afternoon."
        _diuretic_level: int = 30
        cost: int = 50
        remove_upon_use: bool = False
        _menu_option_text: str  = "Give her some artisan grape blood."
        _show_in_all_relevant_choice_menus: bool = False

    # --- Keys --- #

    @dataclass(frozen=True)
    class CoventionTheatreKey(Keys):
        name: str = "Covention Theatre Key"
        plural_name: str = "Covention Theatre Keys"
        description: str = "Perhaps we can use this to enter the Covention Theatre after it's closed?"
        door_id: Door = Door.COVENTION_HALL_PLAY

        def use_item(self):
            pass

    @dataclass(frozen=True)
    class GrimgrubsPubKey(Keys):
        name: str = "Grimgrubs Pub Key"
        plural_name: str = "Grimgrubs Pub Keys"
        description: str = "Perhaps we can use this to enter Grimgrub's Pub after it's closed?"
        door_id: Door = Door.GRIMGRUBS_PUB

        def use_item(self):
            pass

    @dataclass(frozen=True)
    class NightclubKey(Keys):
        name: str = "Nightclub Key"
        plural_name: str = "Nightclub Keys"
        description: str = "Perhaps we can use this to enter the Nightclub after it's closed?"
        door_id: Door = Door.NIGHTCLUB_DANCE_VENUE
        
        def use_item(self):
            pass
