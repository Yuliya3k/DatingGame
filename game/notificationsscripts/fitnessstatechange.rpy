label fitnessstatechange:


    # if notenoughmoney == True:
    # $ nigirlimage = ""
    # $ fitnessstatechange = -5
    # call fitnessstatechange
    
    if nigirlimage == "":
        
        $ fitnessstate += fitnessstatechange
        if fitnessstate < 1:
            $ fitnessstate = 0
        if fitnessstate > 100:
            $ fitnessstate = 100
        if fitnessstatechange > 0:
            $ niimage = "fitness"    
            $ notify_success("+[fitnessstatechange] (Total [fitnessstate])")
        else:
            $ niimage = "fitness"
            $ notify_success("[fitnessstatechange] (Total [fitnessstate])")
    
        return

   


    # if nigirlimage == "nimargo":
    #     if margo_fitnessstate + fitnessstatechange < 0:
    #         $ fitnessstatechange = margo_fitnessstate
    #         $ fitnessstate = 0
    #     else:
    #         $ margo_fitnessstate += fitnessstatechange

    #     if fitnessstatechange > 0:
    #         $ niimage = "fitnessstate"    
    #         $ notify_success("+[fitnessstatechange]")
    #     else:
    #         $ niimage = "fitnessstate"
    #         $ notify_success("[fitnessstatechange]")  


    if nigirlimage == "nisally":
        if sally_fitnessstate + fitnessstatechange < 0:
            $ fitnessstatechange = sally_fitnessstate
            $ sally_fitnessstate = 0
        else:
            $ sally_fitnessstate += fitnessstatechange

        if fitnessstatechange > 0:
            $ niimage = "fitness"    
            $ notify_success("+[fitnessstatechange] (Total [sally_fitnessstate])")
        else:
            $ niimage = "fitness"
            $ notify_success("[fitnessstatechange] (Total [sally_fitnessstate])")


    # if nigirlimage == "nihayoon":
    #     if hayoon_fitnessstate + fitnessstatechange < 0:
    #         $ fitnessstatechange = hayoon_fitnessstate
    #         $ fitnessstate = 0
    #     else:
    #         $ hayoon_fitnessstate += fitnessstatechange

    #     if fitnessstatechange > 0:
    #         $ niimage = "fitnessstate"    
    #         $ notify_success("+[fitnessstatechange]")
    #     else:
    #         $ niimage = "fitnessstate"
    #         $ notify_success("[fitnessstatechange]")  



    # if nigirlimage == "niava":
    #     if ava_fitnessstate + fitnessstatechange < 0:
    #         $ fitnessstatechange = ava_fitnessstate
    #         $ fitnessstate = 0
    #     else:
    #         $ ava_fitnessstate += fitnessstatechange

    #     if fitnessstatechange > 0:
    #         $ niimage = "fitnessstate"    
    #         $ notify_success("+[fitnessstatechange]")
    #     else:
    #         $ niimage = "fitnessstate"
    #         $ notify_success("[fitnessstatechange]")  

    # if nigirlimage == "nikira":
    #     if kira_fitnessstate + fitnessstatechange < 0:
    #         $ fitnessstatechange = kira_fitnessstate
    #         $ fitnessstate = 0
    #     else:
    #         $ kira_fitnessstate += fitnessstatechange

    #     if fitnessstatechange > 0:
    #         $ niimage = "fitnessstate"    
    #         $ notify_success("+[fitnessstatechange]")
    #     else:
    #         $ niimage = "fitnessstate"
    #         $ notify_success("[fitnessstatechange]")  

    return