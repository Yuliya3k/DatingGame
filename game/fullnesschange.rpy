label fullnesschange:
    # $ fullnesschange = 0
    # $ calorieschange = 0
    # $ fullnesschange = 200
    # $ nigirlimage = "nilin"
    # call fullnesschange


    if nigirlimage == "nilin":
        if lin_fullness + fullnesschange > lin_fullmax:
            $ fullnesschange = lin_fullmax - lin_fullness
            $ lin_fullness = lin_fullmax
        if lin_fullness + fullnesschange < 0:
            $ fullnesschange = lin_fullness
            $ lin_fullness = 0
        if lin_fullness + fullnesschange <= lin_fullmax:
            $ lin_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")


    return
"Something went wrong Fullnesschange"