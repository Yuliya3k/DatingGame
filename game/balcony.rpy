label balcony:
    
    $ myrandom = renpy.random.randint(2,3)
    if myrandom == 1:
        $ position = "gardeningbalconynoaurora"
        call sceneimg
        "You can see the view from your balcony"
    if myrandom == 2:
        $ position = "kriswalkingbalconynokris"
        call sceneimg
        "You can see the view from your balcony to the road"
    if myrandom == 3:
        $ position = "kriswalkingbalcony"
        call sceneimg
        
        if krisfirstmeet == 0:
            player "As I was settling into my new home, I couldn't help but notice my quirky neighbor, Kris. She lives just down the street, and her childlike character is evident from her playful antics. While I don't know her well yet, I've seen her around, always bringing smiles to people's faces. Kris and I haven't spoken much, but I'm curious to get to know her better and perhaps find out what makes her tick."
            $ krisfirstmeet = 1
        else:
            player "I can see Kris is going somewhere"
    if myrandom == 4:
        $ position = "auroragardeningbalcony"
        call sceneimg
        if aurorafirstmeet == 0:
            player "Living in my new neighborhood, I couldn't help but notice Aurora, one of my neighbors. Her house and garden are meticulously kept, and she's known for her eco-friendly lifestyle. Although we haven't met yet, I've heard about her commitment to sustainability and eco-conscious living. I'm eager to introduce myself and perhaps get some tips on sustainable cooking and gardening from her."
            $ aurorafirstmeet = 1
            $ auroraseen = 1
        else:
            player "I can see Aurora is gardening"
            $ auroraseen = 1
    
    
    jump culinarychoices