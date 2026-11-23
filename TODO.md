# TODO

## General
- Finish implementing the phone dialogue from favor() and gotta()
- Finish implementing holdIt(), display_hold_quip()
- Add 2 more pee desperation stories
- Implement begToilet()
- Finish implementing indePee()
- Consider using an animated bar to indicate bladder fullness!!!
- Not sure if I'm applying updateTimeAndStats() consistently. I think it should be applied everywhere that there was `c(locstack[0], "Continue ...")` in the html, which was usually in menus. But gotta double check this!

## Bugs to fix!
- Write tests for the new inventory system
- Consider updating RNG state only after a decision is made as opposed to after every single time rng is required for history consistency.
- From the original game, the main character can "see" features of their date (like what bra they're wearing, notice they're squirming) while they're on the phone. This is unrealistic and should be patched out. 
- Sometimes, there's conflicting dialogue between "You're lucky I love you more than I need to pee right now" and immediately after some dialogue expressing how much she needs to pee right now!
- May need to adjust the girlfriend.showed_need flag, it appears even after she's emptied her bladder. Maybe the original html had a soln to this tho?

## Notes
- NYI = Not Yet Implemented



## Testing

At the moment, there are 3 different ways to perform automatic tests for this project:

### Python Unit Tests ([tests/](tests/))
Best for testing class definitions that were defined using Python syntax

### Renpy Lint Hooks Integration ([game/tests/lint_hooks/](game/tests/lint_hooks/))
Used for verifying commits. Can also put some version of Python unit tests in here too

### Renpy Automated Testing ([game/tests/automated_testing/](game/tests/automated_testing/))
Best for testing gameplay paths/loops, UI
Ensure that some path is reachable
Ensure that a collection of choices reaches the same outcome
Verifying dialogue.
