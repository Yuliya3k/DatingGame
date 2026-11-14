label lindatelistening:

    if lindtaeeatq == 1:
        $ myrandom = renpy.random.randint(1,2)
        if myrandom == 1:
            $ position = "parkpromlincafesittingeating"
            if lin_fullness < 4000:
                $ lin_fullness += 1000
            else:
                $ lin_fullness = 400
        else:
            $ position = "parkpromlincafesittinglistening"
        call sceneimg
    else:
        $ position = "parkpromlincafesittinglistening"                   
        call sceneimg

return