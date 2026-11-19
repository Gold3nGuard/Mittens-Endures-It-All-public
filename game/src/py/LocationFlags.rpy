# TODO: Use enums to set the location flag!

init -3 python: 
    from enum import Enum
    # TODO: Should Grom Tree be dance location or make out location?
    # Currently thinking Grom = makeout, Hexside gym = dance
    class Location(Enum):
        """Indicates date locations/venues
        Prefix `dark` indicates going to that location after it's closed (after dark)
        """

        PRE_DATE = 00

        ON_CALL_WITH_GF = 1
        BONESBOROUGH_MARKET = 2

        PICKUP_AMITYS_HOUSE = 10 # Formerly `pickup`
        PICKUP_LUZS_HOUSE = 20 # Formerly `pickup`
        
        BROOM = 30 # Formerly `driveout`

        COVENTION_HALL_PLAY = 40 # Formerly `themovie`
        WATCHING_COVENTION_PLAY = 41 # Formerly `domovie`
        DARK_COVENTION = 45

        NIGHTCLUB_DANCE_VENUE = 50 # Formerly `theclub`
        CURRENTLY_DANCING = 51 # Formerly `godance`
        DARK_CLUB = 55

        GRIMGRUBS_PUB = 60  # Formerly `thebar`
        DARK_BAR = 65
        DRINKING_GAME = 66

        GROM_TREE = 700
        MAKEOUT_LOCATION = 70 # Formerly `themakeout`. GROM_TREE? 
        ROMANTIC_WALK = 71 # Formerly `thewalk`
        THE_YARD = 72 # Formerly `theyard`
        THE_HOT_TUB = 73 # Formerly `thehottub`
        LAKE_LACUNA_BEACH = 74 # Formerly `thebeach`

        AMITYS_HOUSE_OUTDOORS_NIGHT = 110 # Formerly `thehome`
        AMITYS_LIVING_ROOM_NIGHT = 111
        AMITYS_BEDROOM_NIGHT = 112 # Formerly `thebedroom`
        AMITYS_NIGHT_SEX_1 = 113 # Formerly `fuckher`
        AMITYS_NIGHT_SEX_2 = 114
        AMITYS_NIGHT_SEX_3 = 115
        AMITYS_NIGHT_SEX_4 = 116
        AMITYS_NIGHT_SEX_5 = 117
        AMITYS_NIGHT_SEX_6 = 118

        LUZS_HOUSE_OUTDOORS_NIGHT = 120 # Formerly `thehome`
        LUZS_LIVING_ROOM_NIGHT = 121
        LUZS_BEDROOM_NIGHT = 122 # Formerly `thebedroom`
        LUZS_NIGHT_SEX_1 = 123 # Formerly `fuckher`
        LUZS_NIGHT_SEX_2 = 124
        LUZS_NIGHT_SEX_3 = 125
        LUZS_NIGHT_SEX_4 = 126
        LUZS_NIGHT_SEX_5 = 127
        LUZS_NIGHT_SEX_6 = 128

    class CoventionPlayChoice(Enum):
        """Indicates the different plays available
            to watch at the Covention Hall"""
        POST_EXAM_EMBARRASSING_DESPERATION = 0
        FELINE_OTTERLY_IN_LOVE = 1
        ROADTRIP_R = 2
        NO_PEE_DAY_IN_HELL = 3

label itsclosed(mainCharacter, girlfriend):

    $ loc_name = ""
    if currentLocation == Location.DARK_BAR:
        $ loc_name = "Grimgrub's Pub"
    elif currentLocation == Location.DARK_CLUB:
        $ loc_name = "the night club"
    elif currentLocation == Location.DARK_COVENTION:
        $ loc_name = "the Covention Theatre Hall"

    "You and [girlfriend.name] arrive at [loc_name]."
    "It seems a bit deserted."

    if (girlfriend.bladder > girlfriend.bladder_emergency):
        girlfriend "{i}It better not be closed.{/i}"
        call displayGottaGoVocalization() from _call_displayGottaGoVocalization_5

    "[loc_name] is definitely closed."
    call showNeed(character.mainCharacter, girlfriend) from _call_showNeed_6

    # Delegate the responsibility of using a key to open the door to the location labels

    return