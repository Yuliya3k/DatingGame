label barleaving:
    $ myrandom = renpy.random.randint(1,5)
    if myrandom == 1:
        player "Thanks, Kira. See you next time."

        Kira "Take care! Come back soon."

    if myrandom == 2:

        player "Wow, time flies when you're here. Gotta run, Kira."

        Kira "No problem. Have a great night!"

    if myrandom == 3:
        player "Kira, you ever think about leaving this place?"

        Kira " Sometimes, but I love it here. It's like home."

        player "Well, I want to go home now. See you!"

        Kira "Bye bye!"

    if myrandom == 4:
        player "Well, another fantastic night at your bar, Kira. Thanks for the great drinks."

        Kira "Anytime, my friend. Sleep well."

    if myrandom == 5:
        player "Kira, you're the best bartender. Seriously."

        Kira "Flattery will get you another drink... next time!"

        player "See you next time!"
    jump culinarychoices