label scale:
    play sound "audio/rmcooking.mp3" volume 0.5
    show screen kitchenscale

    
    
    $ rightpan = renpy.random.randint(1,9)
    $ leftpan = renpy.random.randint(1,9)
    label scaleloop:
        
        $ scaleactive = 1
        $ cookingstatus = "Cooking"
        pause 0.01
        if scaleactive == 1:
            if x >= 1190:
                $ poiterforward = 0
            if x <= 562:
                $ poiterforward = 1
            if x < 1190 and poiterforward == 1:
                $ x = x+10
                
            if x > 562 and poiterforward == 0:
                $ x = x-10
        else:
            jump stoppointer
        jump scaleloop

jump scale
