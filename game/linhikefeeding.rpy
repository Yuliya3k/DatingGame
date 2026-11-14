label linhikefeeding:

    # $ position = "linsittingcampfiremouthopened"
    # call sceneimg
    # pause
    # $ position = "linsittingcampfiremouthopenedfromabove"
    # call sceneimg
    # pause
    if lin_fullstage == 10:
        call linistoofull

    if linhikebreakeat == 1 or linhikingbreak == 1:
        # just add fullness
        $ lin_fullness += renpy.random.randint(100,400)
        if lin_fullness > 4000:
            $ lin_fullness = 4000
        $ lin_calories += renpy.random.randint(100,400)
        $ lin_attitude += 1
        $ linhikingbreak = 0
        return



    if linhikejustrest == 2:
        show screen linhikefeeding
        # feeding by player

        $ position = "linsittingcampfiremouthopened"
        call sceneimg
        label linfeedingloop1:
            $ position = "linsittingcampfiremouthopenedfromabove"
            call sceneimg
            pause 1
            jump linfeedingloop1
        

    if linhikeexplodingeat == 1:
        
        # feeding by player
        show screen linhikefeeding
        $ position = "linsittingcampfiremouthopened"
        call sceneimg
        label linfeedingloop2:

            $ position = "linsittingcampfiremouthopenedfromabove"
            call sceneimg
            pause 1
            jump linfeedingloop2



# label linfeedingreturn:
#     hide screen linhikefeeding

#     return
"Something gone wrong"