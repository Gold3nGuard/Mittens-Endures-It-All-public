init -10 python:

    from datetime import datetime, timedelta
    from functools import total_ordering


    @total_ordering
    class Time:

        """
        Custom time object for the game
        If indicating a time after midnight, set day = 2
        """

        def __init__(self, hour=17, minute=30, day=1):
            self._datetime_obj = datetime(
                year=2024,
                month=1,
                day=day,
                hour=hour,
                minute=minute
            )

        def __repr__(self) -> str:
            return f"Time({self.__str__()})"

        def __str__(self) -> str:
            return f"{self._datetime_obj.hour:02}:{self._datetime_obj.minute:02}"

        def display(self) -> str:
            return self.__str__()

        def __add__(self, minute: int) -> "Time":
            self._datetime_obj += timedelta(minutes=minute)
            return self

        def __sub__(self, minute: int) -> "Time":
            self += -minute
            return self

        def __sub__(self, other: "Time") -> timedelta:
            return self._datetime_obj - other._datetime_obj

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Time):
                return False
            return self._datetime_obj == other._datetime_obj

        def __ge__(self, other: "Time") -> bool:

            return self._datetime_obj >= other._datetime_obj


        def advanceTime(self, deltaMinutes: int = 2):
            """Advances time by deltaMinutes.

            Args:
                deltaMinutes (int): Number of minutes to advance time by.

            Side Effects:
                Modifies self.
            """

            self += deltaMinutes

        def copy(self) -> "Time":
            return Time(hour=self._datetime_obj.hour, minute=self._datetime_obj.minute)

# Instantiate the time object          
default gametime = Time()

label updateTimeAndStats():
    # Mostly replicates the go() function
    # This is a renpy function, must use `call` instead of `jump`!

    # Reset flags
    $ girlfriend.showed_need = False 
    $ girlfriend.now_peeing = False  
    $ girlfriend.now_wetting = False  
    $ girlfriend.now_just_made_it = False  
    $ girlfriend.now_peeing_outdoors = False  

    # Updates the time and girlfriend's omo stats
    $ girlfriend.updateBladderFillRate()
    $ girlfriend.transfer_tummy_to_bladder(girlfriend.bladder_filling_rate)
    $ girlfriend.diuretic_level_decay()

    # turns_to_wait_before_asking used to be waitcounter
    if girlfriend.turns_to_wait_before_asking > 0:
        $ girlfriend.turns_to_wait_before_asking -= 1

    $ gametime.advanceTime()

    # TODO: Implement hard limits on stats such as mood, shyness, tummy
    
    if girlfriend.peeUrgencyLevel == PeeUrgencyLevel.DOESNT_NEED_TO_GO_AT_ALL:
        image amity norm = Image("images/amity norm@3.5.png", oversample=3)
        if renpy.showing("amity"):
            show amity norm
    elif girlfriend.peeUrgencyLevel == PeeUrgencyLevel.FIRST_URGE:
        image amity urge = Image("images/amity urge@3.5.png", oversample=3)
        if renpy.showing("amity"):
            show amity urge
    elif girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_NEED:
        image amity need = Image("images/amity need@3.5.png", oversample=3)
        if renpy.showing("amity"):
            show amity need
    elif girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_EMERGENCY:
        image amity emer = Image("images/amity emer@3.5.png", oversample=3)
        if renpy.showing("amity"):
            show amity emer
    elif girlfriend.peeUrgencyLevel == PeeUrgencyLevel.BLADDER_LOSE:
        image amity lose = Image("images/amity leak@3.5.png", oversample=3)
        if renpy.showing("amity"):
            show amity lose

    return

# Define location closing times
# TODO: Ensure that times after midnight are properly accounted for
define club_closing_time = Time(hour=2, minute=0, day = 2) # Formerly `clubclosingtime`
define theater_closing_time = Time(hour=22, minute=0) # Formerly `clubclosingtime`
define bar_closing_time = Time(hour=1, minute=0, day = 2) # Formerly `clubclosingtime`
