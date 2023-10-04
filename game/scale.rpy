label scale:
    $ scaleactive = 1
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

jump scale
