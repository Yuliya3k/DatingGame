label bar2:
    call closescreens
    $ calendar.AddMinutes(20)
    $ myrandom = renpy.random.randint(1,5)

    $ position = "barenterance"
    call sceneimg
    player "I decided to revisit Kira's bar, eager to experience the vibrant atmosphere once more. The moment I walked through the door, the lively chatter and clinking of glasses greeted me." 
    $ position = "kiraenterance"
    call sceneimg
    player "Kira was behind the bar, a beacon of confidence as she expertly mixed drinks and served customers. I made my way to an empty spot at the bar."
    $ position = "kiraworking"
    call sceneimg



    if myrandom == 1:        
        player "Hey there, Kira! It's good to be back. What's your special recommendation today?"
        $ position = "kiraexplain"
        call sceneimg
        Kira "Welcome back! You've got great timing. Today, we're featuring a signature cocktail called the 'City Lights.' It's a delightful blend of citrus and a hint of spice. Care to give it a try?"
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "Sounds amazing, Kira. I'll take one, please.":
                call drinkthank
                jump barleaving
            "You know what, Kira? I'm curious to explore the menu a bit. I'll take a look at what else you've got behind that bar.":
                call bardrinks
                jump barleaving

    if myrandom == 2:
        player "Hi, Kira! Your bar has such a fantastic vibe. What's the crowd's favorite drink here?"
        $ position = "kiraexplain"
        call sceneimg
        Kira "Thanks for the compliment! You can't go wrong with our 'Sapphire Sunset.' It's been a hit lately, and I think you'll love its smooth and refreshing taste."
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "Sounds amazing, Kira. I'll take one, please.":
                call drinkthank
                jump barleaving
            "You know what, Kira? I'm curious to explore the menu a bit. I'll take a look at what else you've got behind that bar.":
                call bardrinks
                jump barleaving
    if myrandom == 3:
        player "Hey, Kira! Last time I was here, your cocktails were amazing. Surprise me with something new today!"
        $ position = "kiraexplaining"
        call sceneimg
        Kira "I like your adventurous spirit! How about I whip up a 'Mystic Mirage' for you? It's a bit mysterious, just like the city."
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "Sounds amazing, Kira. I'll take one, please.":
                call drinkthank
                jump barleaving
            "You know what, Kira? I'm curious to explore the menu a bit. I'll take a look at what else you've got behind that bar.":
                call bardrinks
                jump barleaving
    if myrandom == 4:
        player "Hi again, Kira! I had a blast the last time I was here. What's the most popular drink on the menu?"
        $ position = "kiraexplaining"
        call sceneimg
        Kira "I'm glad you enjoyed it! Our 'Moonlit Martini' has been a long-time favorite. It's a classic, elegant choice. Want one?"
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "Sounds amazing, Kira. I'll take one, please.":
                call drinkthank
                jump barleaving
            "You know what, Kira? I'm curious to explore the menu a bit. I'll take a look at what else you've got behind that bar.":
                call bardrinks
                jump barleaving
    if myrandom == 5:
        player "Kira, it's great to be back. Your drinks are top-notch. What's today's special?"
        $ position = "kiraexplaining"
        call sceneimg
        Kira "Welcome back! Today's special is a 'Starfall Sour.' It's a unique blend of sweet and sour with a hint of raspberry. Care to give it a shot?"
        $ position = "kiraquestion"
        call sceneimg
        menu:
            "Sounds amazing, Kira. I'll take one, please.":
                call drinkthank
                jump barleaving
            "You know what, Kira? I'm curious to explore the menu a bit. I'll take a look at what else you've got behind that bar.":
                call bardrinks
                jump barleaving
    jump barleaving
return