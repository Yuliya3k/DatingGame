label bar:

    $ kira_fullness = renpy.random.randint(0,4000)
    if kirafirsttime == 0:
        
        jump bar1

    if kirafirsttime == 1:
        $ kirafirsttime = 2
        jump bar2

        

    if kirafirsttime == 2:
        jump bar3

    
"Something went wrong"
jump bar