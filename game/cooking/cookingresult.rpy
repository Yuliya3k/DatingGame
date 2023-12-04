label cookingresult:
    $ calendar.AddMinutes(15)
    if x >= 696 and x <= 750:
        $ cookingstatus = "Success"
        
        with slowdissolve
        
        $ workreputation += 1
        $ dayworksuccessfulhours += float(0.25)
        $ cookingskill += float(0.1)
        $ daysalary = float(cooksalaryperhour*dayworksuccessfulhours)
        # $ salarystatus = (workreputation*cookingskill)/10000


    else:
        $ cookingstatus = "You have failed"
        with slowdissolve
        $ workreputation -= 1
        if workreputation > 100 and cookingskill > 100:
            $ margo_fullness += 100
            hide screen kitchenscale
            $ position = "margoeatingleftovers"
            call sceneimg
            
    $ myrandom = renpy.random.randint(1,5)
    if myrandom == 1:
        hide screen kitchenscale
        $ position = "margormstandingwhilecooking"
        call sceneimg
        $ myrandom = renpy.random.randint(1,20)
        if myrandom == 1 and rmclients == 1:
            $ rmclienttalk = "mrsanderson"
            call rmclienttalk
            

        pause
        
    jump cook