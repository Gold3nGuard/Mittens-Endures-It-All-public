# Define randomness thresholds
default restroom_bar_locked = 80 # Likelihood of bar restroom locked. Originally `rrlockedthresh`
default restroom_covention_line = 80 # Likelihood of line for Covention Hall restroom. Originally `rrmovielinethresh`
default restroom_gas_threshold = 80 # Likelihood of gas station toilet being out of order. Originally `rrgasthresh`
default phone_hold_threshold = 80 # Likelihood of her holding it for you on the phone. 
default spurt_threshold = 50 # Likelihood of her spurting rather than wetting

init python:

    from random import random

    def randomChoice(probability: float) -> bool:
        """Has a probability% chance of outputting True. False otherwise."""
        if 0 <= probability <= 100:
            return (random() * 100) < probability
        else:
            raise ValueError(f"probability must be between 0 and 100 incl. Was given {probability=}")