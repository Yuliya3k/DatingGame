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
    if position == "backyard":
        scene bg
        
    
return