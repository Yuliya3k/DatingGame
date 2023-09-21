label sceneimg:
    call girl
    scene blankbg
    # hide kira
    # hide kris
    # hide alexa
    if position == "home":
        scene bg
    if position == "kiraworking" or position == "kiraworking2" or position == "kiraquestion" or position == "kiraflirting" or position == "kiraexplain":
        scene bg
        show kira
    if position == "alexaexplaining" or position == "alexaworking" or position == "alexahappy" or position == "alexasurprised":
        scene bg
        show alexa

    if position == "krisexplaining" or position == "krishi" or position == "krisshy" or position == "kriswalking" or position == "kriswalkingbalcony":
        scene bg
        show kris

    if position == "auroragardening" or position == "aurorahello" or position == "aurorahey" or position == "auroraiwish" or position == "auroragardeningbalcony":
        scene bg
        show aurora

    if position == "backyard" or position == "gardeningbalconynoaurora" or position == "kriswalkingbalconynokris":
        scene bg
        
    
return