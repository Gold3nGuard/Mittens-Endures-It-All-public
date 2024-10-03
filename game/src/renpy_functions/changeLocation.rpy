# only ever applies to broomRide, so moved there
# label changeLocation(mainCharacter, girlfriend, newLocation):
#     # Changes the location. Should only be *called* when you're with your girlfriend
#     # Calls showNeed() and then jumps to the new location
#     # Args:
#     #   mainCharacter (renpy.Character): Should input "character.mainCharacter"
#     #   girlfriend (Girlfriend): 
#     #   newLocation (str): A string that is exactly the same as the label you want to jump to
#     call showNeed(mainCharacter, girlfriend, changeVenue = True)
#     jump expression newLocation