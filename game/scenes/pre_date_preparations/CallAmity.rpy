label CallAmity:

    "I send a crow towards Blight Manor and await a response."
    Amity "Hola Batata, how are you doing?"
    Luz "I'm doing great! I am so excited for tonight!"
    jump CallAmityChoices


label CallAmityChoices:

    menu:

        "Ask for a favour":
            call updateTimeAndStats() from _call_updateTimeAndStats_21
            jump PhoneFavours

        "Compliment Amity":
            call compliment(girlfriend) from _call_compliment_1
            call updateTimeAndStats() from _call_updateTimeAndStats_22
            Amity "Oh Luz, you're such a tease!"
            jump CallAmityAnythingElse

        "Say \"See you soon!\" and hang up":
            call updateTimeAndStats() from _call_updateTimeAndStats_23
            Luz "See you soon!"
            "I hang up before Amity has the chance to play the \"You hang up first\" game with me again."
            "I was late to our date that night and she still got upset with me! (It was the playful type of upset, but still...)"
            jump PrepareForDate

    # jump PrepareForDate


label PhoneFavours:

    Luz "Could I ask please for a favour before our date?"
    Amity "Oh alright, since you're asking so nicely Batata."

    menu:

        "Do you need to pee right now?":

            Amity "N- Nope! Not at all, w- why do you ask, Luz?"
            "I hear a hint of nervousness in her voice as she said that."
            call updateTimeAndStats() from _call_updateTimeAndStats_24

            menu:

                "You just sound distracted is all.":
                    Amity "Oh, really?"
                    call updateTimeAndStats() from _call_updateTimeAndStats_25

                "Could you hold it until I come pick you up?":
                    Amity "N- Nope. Sorry Luz, I- I just don't {i}want{/i} to be... bursting... during our date..."
                    "She sounded really flustered as she said that."
                    call updateTimeAndStats() from _call_updateTimeAndStats_26

        "Could you drink a glass of water?":
            if girlfriend.tummy <= girlfriend.tummy_capacity:
                $ girlfriend.tummy += 1000
                Amity "Yep, always good to stay hydrated!"
            else:
                Amity "I'm not thirsty right now."
            call updateTimeAndStats() from _call_updateTimeAndStats_27

        "Nevermind...":
            call updateTimeAndStats() from _call_updateTimeAndStats_28
            jump CallAmityAnythingElse

    jump CallAmityAnythingElse


label CallAmityAnythingElse:

    Amity "Anything else Batata?"
    jump CallAmityChoices