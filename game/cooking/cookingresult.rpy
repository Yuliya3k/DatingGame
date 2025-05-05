label cookingresult:
    $ calendar.AddMinutes(15)

    if scalecrop_right >= scalesweetspotmin and scalecrop_right <= scalesweetspotmax:
           
        $ cookingstatus = "Success"
        
        with slowdissolve
        
        $ workreputation += 1
        $ niimage = "cookreputation"
        $ nigirlimage = ""
        $ notify_success("+5")
        $ dayworksuccessfulhours += float(0.25)
        $ cookingskill += float(0.1)
        $ daysalary += float(cooksalaryperhour*0.25)
        pause 1
        $ niimage = "cookingskill"
        $ nigirlimage = ""
        $ notify_success("+5")
        
        pause 1
        $ niimage = "money"
        $ nigirlimage = ""
        $ notify_success("+[(cooksalaryperhour*0.25)]")
        # $ salarystatus = (workreputation*cookingskill)/10000
        pause 1.0
        $ cookingstatus = ""


    else:
        $ cookingstatus = "You have failed"
        with slowdissolve
        $ workreputation -= 1
        $ niimage = "cookreputation"
        $ nigirlimage = ""
        $ notify_success("-1")
        pause 1.0
        $ cookingstatus = ""
        if workreputation > 100 and cookingskill > 100:
            $ margo_fullness += 200
            $ niimage = "fullness"
            $ nigirlimage = "nimargo"
            $ notify_success("+200")
            pause 1
            $ margo_calories += 200
            $ niimage = "calories"
            $ nigirlimage = "nimargo"
            $ notify_success("+200")
            hide screen kitchenscale
            $ position = "margoeatingleftovers"
            call sceneimg
            pause
            
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