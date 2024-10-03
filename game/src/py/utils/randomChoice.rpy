init python:

    from random import random

    def randomChoice(probability: float) -> bool:
        """Has a probability% chance of outputting True. False otherwise."""
        if 0 <= probability <= 100:
            return (random() * 100) < probability
        else:
            raise ValueError(f"probability must be between 0 and 100 incl. Was given {probability=}")