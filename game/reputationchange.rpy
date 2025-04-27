label reputationchange:
    # $ reputationchange = -1
    # $ nigirlimage = "nilin"
    # call reputationchange

    if nigirlimage == "nilin":
        $ lin_attitude += reputationchange
        if lin_attitude < -100:
            $ lin_attitude = -100
        if lin_attitude > 100:
            $ lin_attitude = 100
        
        if reputationchange > 0:
            $ niimage = "reputationup"    
            $ notify_success("+[reputationchange]")
        else:
            $ niimage = "reputationdown"
            $ notify_success("[reputationchange]")

    if nigirlimage == "nihayoon":
        $ hayoon_attitude += reputationchange
        
        if hayoon_attitude < -100:
            $ hayoon_attitude = -100
        if hayoon_attitude > 100:
            $ hayoon_attitude = 100
        if reputationchange > 0:
            $ niimage = "reputationup"    
            $ notify_success("+[reputationchange]")
        else:
            $ niimage = "reputationdown"
            $ notify_success("[reputationchange]")
       
    if nigirlimage == "niava":
        $ ava_attitude += reputationchange
        if ava_attitude < -100:
            $ ava_attitude = -100
        if ava_attitude > 100:
            $ ava_attitude = 100
        if reputationchange > 0:
            $ niimage = "reputationup"    
            $ notify_success("+[reputationchange]")
        else:
            $ niimage = "reputationdown"
            $ notify_success("[reputationchange]")

    if nigirlimage == "nisally":
        $ sally_attitude += reputationchange
        if sally_attitude < -100:
            $ sally_attitude = -100
        if sally_attitude > 100:
            $ sally_attitude = 100
        if reputationchange > 0:
            $ niimage = "reputationup"    
            $ notify_success("+[reputationchange]")
        else:
            $ niimage = "reputationdown"
            $ notify_success("[reputationchange]")

    if nigirlimage == "nikris":
        $ kris_attitude += reputationchange
        if kris_attitude < -100:
            $ kris_attitude = -100
        if kris_attitude > 100:
            $ kris_attitude = 100
        if reputationchange > 0:
            $ niimage = "reputationup"    
            $ notify_success("+[reputationchange]")
        else:
            $ niimage = "reputationdown"
            $ notify_success("-[reputationchange]")

    if nigirlimage == "nimargo":
        $ margo_attitude += reputationchange
        if margo_attitude < -100:
            $ margo_attitude = -100
        if margo_attitude > 100:
            $ margo_attitude = 100
        if reputationchange > 0:
            $ niimage = "reputationup"    
            $ notify_success("+[reputationchange]")
        else:
            $ niimage = "reputationdown"
            $ notify_success("[reputationchange]")

    return