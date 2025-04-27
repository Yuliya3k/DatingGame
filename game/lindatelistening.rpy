label lindatelistening:

    if lindtaeeatq == 1:
        $ myrandom = renpy.random.randint(1,2)
        if myrandom == 1:
            $ position = "parkpromlincafesittingeating" 
            
            $ fullnesschange = 200

            $ nigirlimage = "nilin"
            call fullnesschange
            pause 2
            $ calorieschange = 200
            $ nigirlimage = "nilin"
            call calorieschange
            
        else:
            $ position = "parkpromlincafesittinglistening"
            call sceneimg
    else:
        $ position = "parkpromlincafesittinglistening"                   
        call sceneimg

    
    return