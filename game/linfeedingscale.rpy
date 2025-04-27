label linfeedingscale:
    $ position = "linhikingcampfiretalkeating"
    call sceneimg
    $ linfeedingactive = 1
    $ fullnesschange = 100
    $ nigirlimage = "nilin"
    call fullnesschange
    pause 2
    $ calorieschange = 100
    $ nigirlimage = "nilin"
    call calorieschange

    call sceneimg

    $ linfeedingpressurexsize += renpy.random.randint(100,300)
    if linfeedingpressurexsize > 500:
        $ linistoofull = 1
        $ linfeedingpressurexsize = 500
        $ position = "linhikingcampfiretalkabouttovomit"
        call sceneimg
        call linvomitcomments
        #  sound "audio/vomit.mp3" volume 0.5
        $ position = "linhikingcampfirevomiting"
        call sceneimg
        $ fullnesschange = - lin_fullness
        $ calorieschange = - lin_fullness
        $ nigirlimage = "nilin"
        call fullnesschange
        pause 2        
        $ nigirlimage = "nilin"
        call calorieschange
        pause 2.0
        $ reputationchange = -5
        $ nigirlimage = "nilin"
        call reputationchange
        $ linfeedingpressurexsize = 0
        jump linhiking
        # call unsuccessful ending

    pause 0.1
    $ linfeedingchancexsize = int(lin_fullness/8)
    if linfeedingchancexsize > 500:
        $ linfeedingchancexsize = 500
    pause 1

    if lin_fullstage == 10 or linistoofull == 1:
        $ position = "linhikingcampfireendoffeeding"
        call sceneimg
        call linistoofull
        $ linistoofull = 0
        $ reputationchange = 5
        $ nigirlimage = "nilin"
        call reputationchange
        pause 5
        $ lin_hikingsuccessfeeding = 1
        jump linhiking
    else:
        if lin_fullstage < 5:
            $ position = "linhikingcampfirebellyview"
            call sceneimg
            call lineatingcomments
            $ linfeedingactive = 0
            $ position = "linhikingcampfiretalkmouthopen"
            call sceneimg
        else:
            $ position = "linhikingcampfirebellyview"
            call sceneimg
            call linfedcomments
            $ linfeedingactive = 0
            $ position = "linhikingcampfiretalkmouthopen"
            call sceneimg
    


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