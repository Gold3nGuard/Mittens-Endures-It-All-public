# TODO: Use enums to set the location flag!

init -3 python: 
    from enum import Enum
    class Location(Enum):
        """Indicates date locations/venues"""

        PRE_DATE = 00

        PICKUP_AMITYS_HOUSE = 10
        PICKUP_LUZS_HOUSE = 20
        
        BROOM = 30

        COVENTION_HALL_PLAY = 40
        WATCHED_COVENTION_PLAY = 41

        GROM_TREE = 50

        GRIMGRUBS_PUB = 60

        MAKEOUT_LOCATION = 70
        THE_HOT_TUB = 72
        LAKE_LACUNA_BEACH = 73

        AMITYS_HOUSE_NIGHT = 110
        LUZS_HOUSE_NIGHT = 120

    class CoventionPlayChoice(Enum):
        """Indicates the different plays available
            to watch at the Covention Hall"""
        POST_EXAM_EMBARRASSING_DESPERATION = 0
        FELINE_OTTERLY_IN_LOVE = 1
        ROADTRIP_R = 2
        NO_PEE_DAY_IN_HELL = 3