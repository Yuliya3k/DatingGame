label linfeedingscale:
    $ linfeedingactive = 1
    $ lin_fullness += 100
    call sceneimg

    $ linfeedingpressurexsize += renpy.random.randint(100,300)
    if linfeedingpressurexsize > 500:
        $ linistoofull = 1
        $ linfeedingpressurexsize = 500

    pause 0.1
    $ linfeedingchancexsize = int(lin_fullness/8)
    if linfeedingchancexsize > 500:
        $ linfeedingchancexsize = 500
    pause 1

    if lin_fullstage == 10 or linistoofull == 1:
        call linistoofull
        $ linistoofull = 0
    else:
        if lin_fullstage < 5:
            call lineatingcomments
            $ linfeedingactive = 0
        else:
            call linfedcomments
            $ linfeedingactive = 0
    


label pressuredrop:

    if linfeedingpressurexsize > 1:
        if lin_fullstage < 5:
            $ linfeedingpressurexsize -= 40
        else:
            $ linfeedingpressurexsize -= 10
        pause 0.3
    else:
        pause

    jump pressuredrop