label linhikefeeding:

    # $ position = "linhikingcampfiretalkmouthopen"
    # call sceneimg
    # pause
    # $ position = "linsittingcampfiremouthopenedfromabove"
    # call sceneimg
    # pause
    # linhikingcampfirebellyview
    # linhikingcampfiretalkeatingmmm

    if lin_fullstage == 10:
        call linistoofull

    if linhikebreakeat == 1 or linhikingbreak == 1:
        # just add fullness
        $ lin_fullness += renpy.random.randint(100,400)
        if lin_fullness > 4000:
            $ lin_fullness = 4000
        $ lin_calories += renpy.random.randint(100,400)
        
        $ reputationchange = 1
        $ nigirlimage = "nilin"
        call reputationchange
        $ linhikingbreak = 0
        return



    if linhikejustrest == 2:
        
        show screen linhikefeeding
        # feeding by player

        
        label linfeedingloop1:
            $ position = "linhikingcampfiretalkmouthopen"
            call sceneimg
            pause 1
            jump linfeedingloop1
        

    if linhikeexplodingeat == 1:
        # $ position = "linhikingcampfiretalkmouthopen"
        # call sceneimg
        # feeding by player
        show screen linhikefeeding
        
        label linfeedingloop2:

            $ position = "linhikingcampfiretalkmouthopen"
            call sceneimg
            pause 1
            jump linfeedingloop2



# label linfeedingreturn:
#     hide screen linhikefeeding

#     return
"Something gone wrong"