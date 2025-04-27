label trainingbye:
    if lin_attitude > 0:

        $ reputationchange = -1
        $ nigirlimage = "nilin"
        call reputationchange
        
    
    if myrandom == 1:

        player "Take care, Lin. See you around."
        $ position = "linhi"
        call sceneimg
        Lin "You too, [name]. Have a great day!"
        jump culinarychoices

    if myrandom == 2:

        player "Goodbye for now, Lin. Thanks again."

        Lin "No problem, [name]. See you next time!"
        jump culinarychoices

    if myrandom == 3:

        player "Until next time, Lin. Thanks for everything."
        $ position = "linhi"
        call sceneimg
        Lin "You're welcome, [name]. Stay motivated!"
        jump culinarychoices

    if myrandom == 4:

        player "Alright, Lin. I'll catch you later."
        $ position = "linhi"
        call sceneimg
        Lin "Sure thing, [name]. Take care!"
        jump culinarychoices

    if myrandom == 5:

        player "Thanks, Lin. See you soon."
        $ position = "linhi"
        call sceneimg
        Lin "Absolutely, [name]. Have a wonderful day!"
        jump culinarychoices

    if myrandom == 6:

        player "Goodbye, Lin. I appreciate your support."
        $ position = "linhi"
        call sceneimg
        Lin "Anytime, [name]. Keep up the hard work!"
        jump culinarychoices

"somethingwent wrong"
jump culinarychoices