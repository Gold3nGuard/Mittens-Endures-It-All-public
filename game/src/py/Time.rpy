init -3 python:

    from datetime import datetime, timedelta

    class Time():

        def __init__(self, hour=17, minute=30):
            self._datetime_obj = datetime(
                year=2024,
                month=1,
                day=1,
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

        def advanceTime(self, deltaMinutes: int = 2):
            """Advances time by deltaMinutes.

            Args:
                deltaMinutes (int): Number of minutes to advance time by.

            Side Effects:
                Modifies self.
            """

            self += deltaMinutes
            

# Instantiate the time object          
default gametime = Time()

label updateTimeAndStats():
    # Updates the time and girlfriend's omo stats
    $ gametime.advanceTime()
    $ girlfriend.updateBladderFillRate()
    $ girlfriend.transfer_tummy_to_bladder(girlfriend.bladder_filling_rate)
    $ girlfriend.diuretic_level_decay()
    if girlfriend.turns_to_wait_before_asking > 0:
        $ girlfriend.turns_to_wait_before_asking -= 1

    return