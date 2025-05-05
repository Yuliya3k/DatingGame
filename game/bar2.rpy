label bar2:
    call closescreens
    $ calendar.AddMinutes(20)
    $ myrandom = renpy.random.randint(1,5)

    $ position = "barenterance"
    call sceneimg
    player "I decided to revisit Kiras bar, eager to feel that vibrant atmosphere again. The moment I stepped inside, lively chatter and clinking glasses welcomed me."

    $ position = "kiraenterance"
    call sceneimg
    player "Kira was behind the counter, confident and precise as she mixed drinks and served guests. I found an open stool at the bar."

    $ position = "kiraworking"
    call sceneimg

    if myrandom == 1:
        player "Hello Kira, it is great to be back. What special do you recommend today?"
        $ position = "kiraexplain"
        call sceneimg
        Kira "Welcome back Welcome is correct Today we feature a signature cocktail called City Lights A bright mix of citrus and a touch of spice. Care to try it?"
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "That sounds wonderful Kira I will take one please":
                call drinkthank
                jump barleaving
            "I am curious about the rest of the menu I will take a look":
                call bardrinks
                jump barleaving

    if myrandom == 2:
        player "Hi Kira Your bar has such a great vibe What do most people order here?"
        $ position = "kiraexplain"
        call sceneimg
        Kira "You cannot go wrong with Sapphire Sunset It has been a big hit and I think you will love its smooth, refreshing taste."
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "That sounds wonderful Kira I will take one please":
                call drinkthank
                jump barleaving
            "I am curious about the rest of the menu I will take a look":
                call bardrinks
                jump barleaving

    if myrandom == 3:
        player "Hi Kira Last time your cocktails amazed me Surprise me with something new today"
        $ position = "kiraexplaining"
        call sceneimg
        Kira "I like your adventurous spirit How about I make a Mystic Mirage for you It is a bit mysterious, just like this city."
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "That sounds wonderful Kira I will take one please":
                call drinkthank
                jump barleaving
            "I am curious about the rest of the menu I will take a look":
                call bardrinks
                jump barleaving

    if myrandom == 4:
        player "Hello again Kira I had a blast last time here What is the most popular drink?"
        $ position = "kiraexplaining"
        call sceneimg
        Kira "Moonlit Martini has been a favorite for years It is a classic, elegant choice Would you like one?"
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "That sounds wonderful Kira I will take one please":
                call drinkthank
                jump barleaving
            "I am curious about the rest of the menu I will take a look":
                call bardrinks
                jump barleaving

    if myrandom == 5:
        player "Kira it is great to be back Your drinks remain top notch What is the special today?"
        $ position = "kiraexplaining"
        call sceneimg
        Kira "Today we have a Starfall Sour A unique blend of sweet and tart with a hint of raspberry. Care to try?"
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "That sounds wonderful Kira I will take one please":
                call drinkthank
                jump barleaving
            "I am curious about the rest of the menu I will take a look":
                call bardrinks
                jump barleaving

    jump barleaving
return