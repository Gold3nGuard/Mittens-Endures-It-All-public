init -2 python:

    from dataclasses import dataclass, field
    from enum import Enum
    from math import ceil
    from typing import List

    class PeeUrgencyLevel(Enum):
        """A collection of enums to indicate how badly girlfriend needs to pee
        """
        DOESNT_NEED_TO_GO_AT_ALL = 0
        FIRST_URGE = 10 # Level where she first feels the urge to pee (actual multiplier is 1)
        BLADDER_NEED = 20 # Level where she continuously needs to go (actual multiplier is 2)
        BLADDER_EMERGENCY = 30 # Level where it becomes an emergency (actual multiplier is 3)
        BLADDER_LOSE = 35 # Level where she loses control (actual multiplier is 3.5)
        BLADDER_CUM_LOSE = 40 # Level where she spurts as she cums (actual multiplier is 4)
        BLADDER_SEX_LOSE = 50 # Level where she can't control it during sex (actual multiplier is 5)
    
    @dataclass
    class Girlfriend(metaclass=Singleton):
        """A class defining the stats of the girlfriend and how the game can interact with her.

        Args:
            # Displayable stats
            _name (str): 
            _fullname (str): 
            _mood (int): How willing your girlfriend is to positively react to your advancements.
            _shyness (int): How willing your girlfriend is to tell you that she needs to pee.
            _tummy (int): The amount of liquid currently in gf's tummy 
                which will eventually trickle it's way to her bladder
            _bladder (int):
            _diuretic_level (int): Indirectly indicates how quickly liquids go from tummy to bladder.
            _bladder_filling_rate (int): Indicates directly how quickly liquids go from tummy to bladder.
            
            # Hidden stats
            _bladder_first_urge (int): The volume in which your girlfriend first feels the urge to pee. 
            _arousal (int): Indicates how likely your girlfriend is to let you penetrate her.
            
            # Flags and counters
            _flirted_counter (int): How many times have you flirted with gf in the current venue?
                                Originally `flirtedflag`. Defaults to 0.
            _MAX_FLIRTS (int): The maximum flirtation attempts you're allowed per venue.
            _restroom_locked (bool): Was the restroom she just tried using locked?
                                Originally `rrlockedflag`.
            _asked_swim (bool): Did she ask to swim?
            _wet_the_car (bool): Did she soak the car seat?
            _spurted (bool): Is she currently spurting? Originally `shespurted`
            _broke_ice (bool): Has she ever previously mentioned that she needs to pee on this date?
            _saw_her_pee (bool): Have you ever seen her pee?
            _late (bool): Were you late picking up your date?
            _external_flirt (bool): Have you flirted with someone else in this venue? Defaults to False. 

=True
            _owed_favour (bool): Does she owe you a favour? Defaults to False. 
            _panty_colour_hex (str):
            _panty_colour_name (str):
            _wet_legs (bool): Are her legs are wet? Defaults to False.
            _wet_her_panties (bool): Has she ever wet herself on this date? Defaults to False.
            _pre_hold (bool): Did she agree to hold it until you picked her up? Defaults to False.
            _pre_peed (bool): Did she pee before you picked her up? Defaults to False.
            _champagne_counter (int): Number of glasses of champagne served. Defaults to 0.
            
            _gotta_go_flag (bool): Has she just asked to use the restroom? Defaults to False. # Indicates whether she's just asked to use the washroom.
            
            _ask_hold_it_counter (int): Number of times you asked her to hold it since her last pee. Defaults to 0.
            _turns_to_wait_before_asking (int): Indicates how many turns to wait before asking to pee.
                Originally `waitcounter`. Defaults to 0.
            
            _now_peeing (bool): Is she currently casually peeing? Defaults to False.
            _now_just_made_it (bool): Is she currently desperately peeing? Defaults to False.
            _now_wetting (bool): Is she currently wetting? Defaults to False.
            _now_peeing_outdoors (bool): Is she currently peeing outdoors? Defaults to False.
            _just_checked_her_out (bool): Did you just check her out? Defaults to False.

            _peed_outside (bool): Has she peed outside?

            # How long ago has it been since she peed and how much has she drank?
            _last_time_peed (Time): 
            _drank_inventory (Inventory): 

            # Constants (mostly)
            _MOOD_MIN (int): Defaults as 0
            _MOOD_MAX (int): Defaults as 130
            _SHY_MIN (int): Defaults as 0
            _SHY_MAX (int): Defaults as 100

            _TUMMY_MIN (int): Defaults as 0
            _tummy_capacity (int): Soft limit, the volume at which your girlfriend no longer feels thirsty. Defaults as 1500

            _BLADDER_MIN (int): Defaults as 0
        
            _MAX_KISS (int): Max number of kisses that have an effect. Defaults as 7
            _MAX_FEEL (int): Max number of feel-ups that have an effect. Defaults as 7
        
            _FLIRT_LOW_THRESHOLD (int): Likelihood of passing easy flirt check. Defaults as 100
            _FLIRT_MED_THRESHOLD (int): Likelihood of passing moderate flirt check. Defaults as 80
            _FLIRT_HIGH_THRESHOLD (int): Likelihood of passing difficult flirt check. Defaults as 60
        """

        # Displayable stats
        _name: str
        _fullname: str
        _mood: int
        _shyness: int
        _tummy: int
        _bladder: int
        _diuretic_level: int
        _bladder_filling_rate: int

        # Hidden stats
        _bladder_first_urge: int
        _arousal: int = 0 # To be implemented later!


        # Flags and counters
        _flirted_counter: int = 0 # TODO: getter + setter + docstring # Originally `flirtedflag`. indicates how many times you've flirted with her at the current venue.
        _MAX_FLIRTS: int = 2 # TODO: getter + setter + docstring

        _restroom_locked: bool = False # TODO: getter + setter + docstring # originally `rrlockedflag`
        _asked_swim: bool = False # TODO: getter + setter + docstring 
        _wet_the_car: bool = False # TODO: getter + setter + docstring 
        _spurted: bool = False # TODO: getter + setter + docstring # Originally `shespurted`

        _broke_ice: bool = False # TODO: getter + setter + docstring # She's previously mentioned that she needs to pee.
        _saw_her_pee: bool = False  # TODO: getter + setter + docstring 
        _late: bool = False # TODO: getter + setter + docstring 
        _external_flirt: bool = False # TODO: getter + setter + docstring 

        # Flags and counters
        _owed_favour: bool = False 
        _panty_colour_hex: str = "#FF00FF" # TODO: getter + setter + docstring
        _panty_colour_name: str = "magenta" # TODO: getter + setter + docstring
        _wet_legs: bool = False 
        _wet_her_panties: bool = False 
        _pre_hold: bool = False 
        _pre_peed: bool = False 
        _champagne_counter: int = 0

        _gotta_go_flag: bool = False # Indicates whether she's just asked to use the washroom.

        _ask_hold_it_counter: int = 0
        _turns_to_wait_before_asking: int = 0 # originally `waitcounter`

        
        _now_peeing: bool = False # TODO: getter + setter + docstring 
        _now_just_made_it: bool = False # TODO: getter + setter + docstring 
        _now_wetting: bool = False # TODO: getter + setter + docstring 
        _now_peeing_outdoors: bool = False  # TODO: getter + setter + docstring 
        _just_checked_her_out: bool = False # TODO: getter + setter + docstring 

        _peed_outside: bool = False  # TODO: getter + setter + docstring 

        # Variables used for complaining how long ago she's peed 
        # and how much she's drunk
        # TODO: Implement setters and getters and docstrings for all of these attributes!!!
        _last_time_peed: Time = Time(hour=16,minute=30) # originally `lastpeetime`
        _drank_inventory: Inventory = Inventory()
        
        # Location parameters
        _suggested_location: Location = Location.COVENTION_HALL_PLAY
        _visited_locations: List[Location] = field(default_factory=list) # Creates an empty list for dataclass
        _favourite_play: CoventionPlayChoice = CoventionPlayChoice.POST_EXAM_EMBARRASSING_DESPERATION

        # Constants (mostly)
        _MOOD_MIN: int = 0
        _MOOD_MAX: int = 130
        _SHY_MIN: int = 0
        _SHY_MAX: int = 100

        _TUMMY_MIN: int = 0
        _tummy_capacity: int = 1500

        _BLADDER_MIN: int = 0

        _MAX_KISS: int = 7
        _MAX_FEEL: int = 7

        _FLIRT_LOW_THRESHOLD: int = 100
        _FLIRT_MED_THRESHOLD: int = 80
        _FLIRT_HIGH_THRESHOLD: int = 60
        
        # --- Displayable stats --- #
        @property
        def name(self) -> str:
            return self._name

        @property
        def fullname(self) -> str:
            return self._fullname

        @property
        def mood(self) -> int:
            return self._mood

        @mood.setter
        def mood(self, value):
            if (value < self._MOOD_MIN):
                self._mood = self._MOOD_MIN 
            elif (value > self._MOOD_MAX):
                self._mood = self._MOOD_MAX
            else: 
                self._mood = value

        @property
        def shyness(self) -> int:
            return self._shyness

        @shyness.setter
        def shyness(self, value):
            if (value < self._SHY_MIN):
                self._shyness = self._SHY_MIN 
            elif (value > self._SHY_MAX):
                self._shyness = self._SHY_MAX
            else: 
                self._shyness = value

        @property
        def tummy(self) -> int:
            return self._tummy

        @tummy.setter
        def tummy(self, value) -> int:
            if value >= self._TUMMY_MIN:
                self._tummy = value
            else:
                self._tummy = self._TUMMY_MIN

        @property
        def bladder(self) -> int:
            return self._bladder

        @bladder.setter
        def bladder(self, value) -> int:
            if value >= self._BLADDER_MIN:
                self._bladder = value
            else:
                self._bladder = self._BLADDER_MIN

        @property
        def diuretic_level(self) -> int:
            return self._diuretic_level

        @diuretic_level.setter
        def diuretic_level(self, value) -> int:
            if value >= 0:
                self._diuretic_level = value
            else:
                self._diuretic_level = 0

        @property
        def bladder_filling_rate(self) -> int:
            return self._bladder_filling_rate

        @bladder_filling_rate.setter
        def bladder_filling_rate(self, value) -> int:
            """TODO: Perform validation checks on bladder_filling_rate!"""
            self._bladder_filling_rate = value

        @property
        def tummy_capacity(self) -> int:
            return self._tummy_capacity


        # --- Flags and counters --- #
        #
        @property
        def MAX_FLIRTS(self) -> int:
            return self._MAX_FLIRTS
        @property
        def flirted_counter(self) -> int:
            return self._flirted_counter
        @flirted_counter.setter
        def flirted_counter(self, value: int):
            if 0 <= value <= self._MAX_FLIRTS:
                self._flirted_counter = value
            else:
                raise ValueError(f"flirted_counter has to be between 0 and {self._MAX_FLIRTS} incl. Attempted value set was {self.flirted_counter=}")

        #
        @property
        def restroom_locked(self) -> bool:
            return self._restroom_locked
        @restroom_locked.setter
        def restroom_locked(self, value: bool):
            self._restroom_locked = value

        #
        @property
        def asked_swim(self) -> bool:
            return self._asked_swim
        @asked_swim.setter
        def asked_swim(self, value: bool):
            self._asked_swim = value

        #
        @property
        def wet_the_car(self) -> bool:
            return self._wet_the_car
        @wet_the_car.setter
        def wet_the_car(self, value: bool):
            self._wet_the_car = value

        #
        @property
        def spurted(self) -> bool:
            return self._spurted
        @spurted.setter
        def spurted(self, value: bool):
            self._spurted = value

        #
        @property
        def broke_ice(self) -> bool:
            return self._broke_ice
        @broke_ice.setter
        def broke_ice(self, value: bool):
            self._broke_ice = value

        #
        @property
        def saw_her_pee(self) -> bool:
            return self._saw_her_pee
        @saw_her_pee.setter
        def saw_her_pee(self, value: bool):
            self._saw_her_pee = value

        #
        @property
        def late(self) -> bool:
            return self._late
        @late.setter
        def late(self, value: bool):
            self._late = value

        #
        @property
        def external_flirt(self) -> bool:
            return self._external_flirt
        @external_flirt.setter
        def external_flirt(self, value: bool):
            self._external_flirt = value
           
        # 
        @property
        def owed_favour(self) -> bool:
            return self._owed_favour
        @owed_favour.setter
        def owed_favour(self, value: bool):
            self._owed_favour = value
           
        # 
        @property
        def panty_colour_hex(self) -> str:
            return self._panty_colour_hex
        @panty_colour_hex.setter
        def panty_colour_hex(self, value: str):
            self._panty_colour_hex = value
           
        # 
        @property
        def panty_colour_name(self) -> str:
            return self._panty_colour_name
        @panty_colour_name.setter
        def panty_colour_name(self, value: str):
            self._panty_colour_name = value
            
        #
        @property
        def wet_legs(self) -> bool:
            return self._wet_legs
        @wet_legs.setter
        def wet_legs(self, value: bool):
            self._wet_legs = value
            
        #
        @property
        def wet_her_panties(self) -> bool:
            return self._wet_her_panties
        @wet_her_panties.setter
        def wet_her_panties(self, value: bool):
            self._wet_her_panties = value

        #
        @property
        def pre_hold(self) -> bool:
            return self._pre_hold
        @pre_hold.setter
        def pre_hold(self, value: bool):
            self._pre_hold = value
            
        #
        @property
        def pre_peed(self) -> bool:
            return self._pre_peed
        @pre_peed.setter
        def pre_peed(self, value: bool):
            self._pre_peed = value
            
        #
        @property
        def champagne_counter(self) -> int:
            return self._champagne_counter
        @champagne_counter.setter
        def champagne_counter(self, value: int):
            self._champagne_counter = value

        #
        @property
        def gotta_go_flag(self) -> bool:
            return self._gotta_go_flag
        @gotta_go_flag.setter
        def gotta_go_flag(self, value: bool):
            self._gotta_go_flag = value

        #
        @property
        def turns_to_wait_before_asking(self) -> int:
            return self._turns_to_wait_before_asking
        @turns_to_wait_before_asking.setter
        def turns_to_wait_before_asking(self, value: int):
            self._turns_to_wait_before_asking = value

        #
        @property
        def ask_hold_it_counter(self) -> int:
            return self._ask_hold_it_counter
        @ask_hold_it_counter.setter
        def ask_hold_it_counter(self, value: int):
            self._ask_hold_it_counter = value
            
        #
        @property
        def now_peeing(self) -> bool:
            return self._now_peeing
        @now_peeing.setter
        def now_peeing(self, value: bool):
            self._now_peeing = value
          
        #  
        @property
        def now_just_made_it(self) -> bool:
            return self._now_just_made_it
        @now_just_made_it.setter
        def now_just_made_it(self, value: bool):
            self._now_just_made_it = value
            
        #
        @property
        def now_wetting(self) -> bool:
            return self._now_wetting
        @now_wetting.setter
        def now_wetting(self, value: bool):
            self._now_wetting = value
            
        #
        @property
        def now_peeing_outdoors(self) -> bool:
            return self._now_peeing_outdoors
        @now_peeing_outdoors.setter
        def now_peeing_outdoors(self, value: bool):
            self._now_peeing_outdoors = value
            
        #
        @property
        def just_checked_her_out(self) -> bool:
            return self._just_checked_her_out
        @just_checked_her_out.setter
        def just_checked_her_out(self, value: bool):
            self._just_checked_her_out = value
            
        #
        @property
        def peed_outside(self) -> bool:
            return self._peed_outside
        @peed_outside.setter
        def peed_outside(self, value: bool):
            self._peed_outside = value
            
        # @property
        # def ax(self) -> bool:
        #     return self._x

        # @ax.setter
        # def ax(self, value: bool):
        #     self._x = value


        # --- Variables used for complaining how long ago she's peed 
        # --- and how much she's drunk
        @property
        def last_time_peed(self) -> Time:
            return self._last_time_peed
        @last_time_peed.setter
        def last_time_peed(self, value: Time):
            self._last_time_peed = value

        @property
        def drank_inventory(self) -> Inventory:
            return self._drank_inventory
        def flush_drank_inventory(self): 
            # Check for amount_girlfriend_drank == 0 when generating dialogue!
            for key in self._drank_inventory.items:
                self._drank_inventory.items[key].amount_girlfriend_drank = 0


        # --- Bladder urgency levels getters --- #
        @property
        def bladder_urge(self) -> int:
            return self._bladder_first_urge
        @property
        def bladder_need(self) -> int:
            return self._bladder_first_urge * 2
        @property
        def bladder_emergency(self) -> int:
            return self._bladder_first_urge * 3
        @property
        def bladder_lose(self) -> int:
            return ceil(self._bladder_first_urge * 3.5)
        @property
        def bladder_cum_lose(self) -> int:
            return self._bladder_first_urge * 4
        @property
        def bladder_sex_lose(self) -> int:
            return self._bladder_first_urge * 5
        
        # Bladder urgency levels setters
        @bladder_urge.setter
        def bladder_urge(self, value):
            """TODO: Perform a validation check for setting the bladder_urge!"""
            self._bladder_first_urge = value

        @property
        def peeUrgencyLevel(self) -> PeeUrgencyLevel:
            """Indicates how badly your girlfriend needs to pee.
            """
            
            if self.bladder < self.bladder_urge:
                return PeeUrgencyLevel.DOESNT_NEED_TO_GO_AT_ALL
            elif self.bladder_urge <= self.bladder < self.bladder_need:
                return PeeUrgencyLevel.FIRST_URGE
            elif self.bladder_need <= self.bladder < self.bladder_emergency:
                return PeeUrgencyLevel.BLADDER_NEED
            elif self.bladder_emergency <= self.bladder < self.bladder_lose:
                return PeeUrgencyLevel.BLADDER_EMERGENCY
            elif self.bladder_lose <= self.bladder < self.bladder_cum_lose:
                return PeeUrgencyLevel.BLADDER_LOSE
            elif self.bladder_cum_lose <= self.bladder < self.bladder_sex_lose:
                return PeeUrgencyLevel.BLADDER_CUM_LOSE
            elif self.bladder_sex_lose <= self.bladder:
                return PeeUrgencyLevel.BLADDER_SEX_LOSE
            else:
                ValueError(f"How the heck did you get a negative bladder value? {self.bladder =} mL")

        def stats_summary(self) -> str:
            """Outputs your girlfriend's relevant stats for the game. 
            """
            output_string: str = f"Girlfriend: {self.name}\n"
            output_string += f"Mood: {self.mood}\n"
            output_string += f"Shyness: {self.shyness}\n"
            output_string += f"Tummy: {self.tummy}\n"
            output_string += f"Bladder: {self.bladder}\n"
            output_string += f"Diuretic Level: {self.diuretic_level}\n"
            output_string += f"Bladder Filling Rate: {self.bladder_filling_rate}"
            return output_string

        def transfer_tummy_to_bladder(self, amount):
            """Transfers liquid from girlfriend's tummy to her bladder.

            Args:
                amount (int): The amount of liquid to transfer.
            """
            if self._tummy >= amount:
                self._tummy -= amount
                self._bladder += amount
            else:
                self._bladder += amount

        def updateBladderFillRate(self):
            """Updates your girlfriend's bladder_filling_rate stat.
            """

            if (self.tummy <= 10):
                self.bladder_filling_rate = 5

            elif (self.diuretic_level > 200 and self.tummy != 0):
                self.bladder_filling_rate = 30

            elif (self.diuretic_level > 90 and self.tummy !=0):
                self.bladder_filling_rate = 25

            elif (self.diuretic_level > 50 and self.tummy !=0):
                self.bladder_filling_rate = 20

            elif (self.diuretic_level > 0 and self.tummy !=0):
                self.bladder_filling_rate = 15

            elif (self.diuretic_level == 0 and self.tummy !=0):
                self.bladder_filling_rate = 10

            else:
                raise ValueError("Either diuretic_level or tummy are at unexpected levels")


        def diuretic_level_decay(self):
            """Decays your girlfriend's diuretic levels
            """

            if (self.diuretic_level > 150):
                self.diuretic_level -= 3
            elif (self.diuretic_level > 100):
                self.diuretic_level -= 2
            elif (self.diuretic_level > 0):
                self.diuretic_level -= 1

        def pees(self, amount: int = -1):
            """Girlfriend empties her bladder.

            Args:
                amount (int): Amount to empty girlfriend's bladder by. 
                    Defaults to -1, which allows girlfriend to fully void her bladder.
            """

            if amount == -1:
                self._bladder = 0 
            elif amount < 0:
                raise ValueError(f"amount cannot be negative. {amount=}")
            else:
                self._bladder -= amount

        def timeHeld(self, currentTime: Time) -> timedelta:
            """Returns how long ago girlfriend had her last pee."""
            return currentTime - self._last_time_peed