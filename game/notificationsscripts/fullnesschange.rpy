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

    if nigirlimage == "niava":
        if ava_fullness + fullnesschange > ava_fullmax:
            $ fullnesschange = ava_fullmax - ava_fullness
            $ ava_fullness = ava_fullmax
        if ava_fullness + fullnesschange < 0:
            $ fullnesschange = ava_fullness
            $ ava_fullness = 0
        if ava_fullness + fullnesschange <= ava_fullmax:
            $ ava_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")

    if nigirlimage == "nihayoon":
        if hayoon_fullness + fullnesschange > hayoon_fullmax:
            $ fullnesschange = hayoon_fullmax - hayoon_fullness
            $ hayoon_fullness = hayoon_fullmax
        if hayoon_fullness + fullnesschange < 0:
            $ fullnesschange = hayoon_fullness
            $ hayoon_fullness = 0
        if hayoon_fullness + fullnesschange <= hayoon_fullmax:
            $ hayoon_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")

    if nigirlimage == "nisally":
        if sally_fullness + fullnesschange > sally_fullmax:
            $ fullnesschange = sally_fullmax - sally_fullness
            $ sally_fullness = sally_fullmax
        if sally_fullness + fullnesschange < 0:
            $ fullnesschange = sally_fullness
            $ sally_fullness = 0
        if sally_fullness + fullnesschange <= sally_fullmax:
            $ sally_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")


    if nigirlimage == "nimargo":
        if margo_fullness + fullnesschange > margo_fullmax:
            $ fullnesschange = margo_fullmax - margo_fullness
            $ margo_fullness = margo_fullmax
        if margo_fullness + fullnesschange < 0:
            $ fullnesschange = margo_fullness
            $ margo_fullness = 0
        if margo_fullness + fullnesschange <= margo_fullmax:
            $ margo_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")


    if nigirlimage == "nikira":
        if kira_fullness + fullnesschange > kira_fullmax:
            $ fullnesschange = kira_fullmax - kira_fullness
            $ kira_fullness = kira_fullmax
        if kira_fullness + fullnesschange < 0:
            $ fullnesschange = kira_fullness
            $ kira_fullness = 0
        if kira_fullness + fullnesschange <= kira_fullmax:
            $ kira_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")

    if nigirlimage == "nialexa":
        if alexa_fullness + fullnesschange > alexa_fullmax:
            $ fullnesschange = alexa_fullmax - alexa_fullness
            $ alexa_fullness = alexa_fullmax
        if alexa_fullness + fullnesschange < 0:
            $ fullnesschange = alexa_fullness
            $ alexa_fullness = 0
        if alexa_fullness + fullnesschange <= alexa_fullmax:
            $ alexa_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")

    if nigirlimage == "nikris":
        if kris_fullness + fullnesschange > kris_fullmax:
            $ fullnesschange = kris_fullmax - kris_fullness
            $ kris_fullness = kris_fullmax
        if kris_fullness + fullnesschange < 0:
            $ fullnesschange = kris_fullness
            $ kris_fullness = 0
        if kris_fullness + fullnesschange <= kris_fullmax:
            $ kris_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")


    if nigirlimage == "niaurora":
        if aurora_fullness + fullnesschange > aurora_fullmax:
            $ fullnesschange = aurora_fullmax - aurora_fullness
            $ aurora_fullness = aurora_fullmax
        if aurora_fullness + fullnesschange < 0:
            $ fullnesschange = aurora_fullness
            $ aurora_fullness = 0
        if aurora_fullness + fullnesschange <= aurora_fullmax:
            $ aurora_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")

    if nigirlimage == "nifarida":
        if farida_fullness + fullnesschange > farida_fullmax:
            $ fullnesschange = farida_fullmax - farida_fullness
            $ farida_fullness = farida_fullmax
        if farida_fullness + fullnesschange < 0:
            $ fullnesschange = farida_fullness
            $ farida_fullness = 0
        if farida_fullness + fullnesschange <= farida_fullmax:
            $ farida_fullness += fullnesschange
        
        if fullnesschange > 0:
            $ niimage = "fullness"    
            $ notify_success("+[fullnesschange]")
        else:
            $ niimage = "fullness"
            $ notify_success("[fullnesschange]")

    return
"Something went wrong Fullnesschange"