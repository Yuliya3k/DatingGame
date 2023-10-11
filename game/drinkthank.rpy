label drinkthank:
    $ calendar.AddMinutes(20)
    $ myrandom = renpy.random.randint(1,5)
    if myrandom == 1:
        player "Kira, this is fantastic. Thanks for the recommendation."

        Kira "Glad you like it! You have good taste."

    if myrandom == 2:
        player "Cheers, Kira. You make the best drinks in town."

        Kira "To good company and even better drinks!"

    if myrandom == 3:
        player "You know, Kira, you really have a talent for this."

        Kira "Well, it's all about finding the perfect balance."

    if myrandom == 4:
        player "You're an artist, Kira. Thanks for this masterpiece."

        Kira "You're too kind. Enjoy!"

    if myrandom == 5:
        player "Kira, you're a magician. This is incredible."

        Kira " Just a little bartending magic. Enjoy every sip!"
    
return