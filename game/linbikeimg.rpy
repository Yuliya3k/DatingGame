label linbikeimg:
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        $ position = "linbikeparkridingstanding"
        call sceneimg
        
        
    if myrandom == 2:
        $ position = "linbikeparkridingsitting"
        call sceneimg
    if myrandom == 3:
        $ position = "linbikeparkridingsittingside"
        call sceneimg

    return