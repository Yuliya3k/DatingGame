label joggingmotivationchange:


# $ joggingmotivationchange = -1
# $ nigirlimage = "nilin"
# call joggingmotivationchange

    # if nigirlimage == "nilin":
    #     $ lin_joggingmotivation += joggingmotivationchange
    #     if lin_joggingmotivation < -100:
    #         $ lin_joggingmotivation = -100
    #     if lin_joggingmotivation > 100:
    #         $ lin_joggingmotivation = 100
        
    #     if joggingmotivationchange > 0:
    #         $ niimage = "jogging"    
    #         $ notify_success("+[joggingmotivationchange]")
    #     else:
    #         $ niimage = "jogging"
    #         $ notify_success("[joggingmotivationchange]")

    # if nigirlimage == "nihayoon":
    #     $ hayoon_joggingmotivation += joggingmotivationchange
        
    #     if hayoon_joggingmotivation < -100:
    #         $ hayoon_joggingmotivation = -100
    #     if hayoon_joggingmotivation > 100:
    #         $ hayoon_joggingmotivation = 100
    #     if joggingmotivationchange > 0:
    #         $ niimage = "jogging"    
    #         $ notify_success("+[joggingmotivationchange]")
    #     else:
    #         $ niimage = "jogging"
    #         $ notify_success("[joggingmotivationchange]")
       
    # if nigirlimage == "niava":
    #     $ ava_joggingmotivation += joggingmotivationchange
    #     if ava_joggingmotivation < -100:
    #         $ ava_joggingmotivation = -100
    #     if ava_joggingmotivation > 100:
    #         $ ava_joggingmotivation = 100
    #     if joggingmotivationchange > 0:
    #         $ niimage = "jogging"    
    #         $ notify_success("+[joggingmotivationchange]")
    #     else:
    #         $ niimage = "jogging"
    #         $ notify_success("[joggingmotivationchange]")

    if nigirlimage == "nisally":
        $ sally_joggingmotivation += joggingmotivationchange
        if sally_joggingmotivation < 1:
            $ sally_joggingmotivation = 0
        if sally_joggingmotivation > 100:
            $ sally_joggingmotivation = 100
        if joggingmotivationchange > 0:
            $ niimage = "jogging"    
            $ notify_success("+[joggingmotivationchange]")
        else:
            $ niimage = "jogging"
            $ notify_success("[joggingmotivationchange]")

    # if nigirlimage == "nikris":
    #     $ kris_joggingmotivation += joggingmotivationchange
    #     if kris_joggingmotivation < -100:
    #         $ kris_joggingmotivation = -100
    #     if kris_joggingmotivation > 100:
    #         $ kris_joggingmotivation = 100
    #     if joggingmotivationchange > 0:
    #         $ niimage = "jogging"    
    #         $ notify_success("+[joggingmotivationchange]")
    #     else:
    #         $ niimage = "jogging"
    #         $ notify_success("-[joggingmotivationchange]")

    # if nigirlimage == "nimargo":
    #     $ margo_joggingmotivation += joggingmotivationchange
    #     if margo_joggingmotivation < -100:
    #         $ margo_joggingmotivation = -100
    #     if margo_joggingmotivation > 100:
    #         $ margo_joggingmotivation = 100
    #     if joggingmotivationchange > 0:
    #         $ niimage = "jogging"    
    #         $ notify_success("+[joggingmotivationchange]")
    #     else:
    #         $ niimage = "jogging"
    #         $ notify_success("[joggingmotivationchange]")

    return