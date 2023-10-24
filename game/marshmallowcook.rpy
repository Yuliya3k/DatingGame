label marshmallowcook:
    $ position = "krisbackyardsmilingslightly"
    call sceneimg
    $ marshmallowstate = 1
    $ stop = 0
    $ cooking = 1
    if cookingskill > 0 and cookingskill <= 30:
        $ myrandom = marshmallowpos*renpy.random.randint(1,30)
    if cookingskill > 30 and cookingskill <= 60:
        $ myrandom = marshmallowpos*renpy.random.randint(10,30)
    if cookingskill > 60:
        $ myrandom = 10
    
        
        
    
    label marshmallowrawloop:
        if myrandom > 0 and stop == 0:
            $ myrandom -= 1
            $ marshmallowstate = 1
            pause 1
            jump marshmallowrawloop
        else:
            call skilltest
            if cookingskill > 0 and cookingskill <= 30:
                $ myrandom = marshmallowpos*renpy.random.randint(0,30)
            if cookingskill > 30 and cookingskill <= 60:
                $ myrandom = marshmallowpos*renpy.random.randint(10,30)
            if cookingskill > 60:
                $ myrandom = 10
            jump marshmallowlightloop
    label marshmallowlightloop:
        if myrandom > 0 and stop == 0:
            $ myrandom -= 1
            $ marshmallowstate = 2
            pause 1
            jump marshmallowlightloop
        else:
            call skilltest
            if cookingskill > 0 and cookingskill <= 30:
                $ myrandom = marshmallowpos*renpy.random.randint(0,30)
            if cookingskill > 30 and cookingskill <= 60:
                $ myrandom = marshmallowpos*renpy.random.randint(10,30)
            if cookingskill > 60:
                $ myrandom = 10
            jump marshmallowmediumloop
    label marshmallowmediumloop:
        if myrandom > 0 and stop == 0:
            $ myrandom -= 1
            $ marshmallowstate = 3
            pause 1
            jump marshmallowmediumloop
        else:
            call skilltest
            if cookingskill > 0 and cookingskill <= 30:
                $ myrandom = marshmallowpos*renpy.random.randint(0,30)
            if cookingskill > 30 and cookingskill <= 60:
                $ myrandom = marshmallowpos*renpy.random.randint(10,30)
            if cookingskill > 60:
                $ myrandom = 10
            jump marshmallowmuchloop
    label marshmallowmuchloop:
        if myrandom > 0 and stop == 0:
            $ myrandom -= 1
            $ marshmallowstate = 4
            pause 1
            jump marshmallowmuchloop
        else:
            call skilltest
            if cookingskill > 0 and cookingskill <= 30:
                $ myrandom = marshmallowpos*renpy.random.randint(0,30)
            if cookingskill > 30 and cookingskill <= 60:
                $ myrandom = marshmallowpos*renpy.random.randint(10,30)
            if cookingskill > 60:
                $ myrandom = 10
            jump marshmallowtoomuchloop

    label marshmallowtoomuchloop:
        $ marshmallowstate = 5
        "Oops, you have ruined the marshmallow"
        jump stop

    label skilltest:
        if stop == 1:
            jump stop
        return
    "something went wrong"
    return