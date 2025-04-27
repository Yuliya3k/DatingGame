##############################################################################
#  Ava – teasing (warm, cook-flavoured, human tone, belly unlocks)
##############################################################################

label ava_tease:

    menu:
        #------------------------------------------------------------------#
        "Light foodie tease":
            $ myrandom = renpy.random.randint(1,3)

            #––– Player speaks ––––––––––––––––––––––––––––––––––––––––––#
            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "Careful— I still need you to judge tonight’s tiramisu."

            #––– Ava replies –––––––––––––––––––––––––––––––––––––––––––#
            $ position = "avaaftersurfingtalkingclose"
            call sceneimg
            if myrandom == 1:
                Ava "Deal.  I take payment in espresso and compliments."
            elif myrandom == 2:
                Ava "Sweet stuff after beer?  You trying to roll me home?"
            else:
                Ava "Bring it on.  Dessert is my second language."

            #––– Reputation +1 ––––––––––––––––––––––––––––––––––––––––––#
            $ reputationchange = 1
            $ nigirlimage = "niava"
            call reputationchange
            return

        #------------------------------------------------------------------#
        "Easy rescue joke":
            $ myrandom = renpy.random.randint(1,3)

            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "If you slip under I’ll have to dive in wearing my apron."

            $ position = "avaaftersurfingtalkingclose"
            call sceneimg
            if myrandom == 1:
                Ava "Make sure the pockets are full of snacks."
            elif myrandom == 2:
                Ava "Apron’ll drag you down faster than me."
            else:
                Ava "That image alone keeps me from falling in."

            $ reputationchange = 1
            $ nigirlimage = "niava"
            call reputationchange
            return

        #------------------------------------------------------------------#
        "Gentle toughness poke":
            $ myrandom = renpy.random.randint(1,3)

            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "Figured a lifeguard could manage one more bottle."

            $ position = "avaaftersurfingsurprisedclose"
            call sceneimg       # attitude will drop after this
            if myrandom == 1:
                Ava "Strength isn’t measured in empties, chef."
            elif myrandom == 2:
                Ava "Push me and I’ll make you swim for refills."
            else:
                Ava "Nice try.  I know my limits."

            $ reputationchange = -2
            $ nigirlimage = "niava"
            call reputationchange
            return

        #------------------------------------------------------------------#
        "Self-jab about cooking":
            $ myrandom = renpy.random.randint(1,3)

            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "Keep pouring and my burgers will taste like dishwater."

            $ position = "avaaftersurfingtalkingclose"
            call sceneimg
            if myrandom == 1:
                Ava "Adds minerals, right?"
            elif myrandom == 2:
                Ava "I’ll save us with extra ketchup."
            else:
                Ava "Okay, for everyone’s sake I’ll slow down."

            $ reputationchange = 1
            $ nigirlimage = "niava"
            call reputationchange
            return

        #------------------------------------------------------------------#
        #  Belly teases (only appear if she’s properly stuffed)
        #------------------------------------------------------------------#
        "Playful belly compliment" if ava_fullstage >= 5:
            $ myrandom = renpy.random.randint(1,3)

            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "That little keg you’ve got going is kind of cute."

            $ position = "avaaftersurfingtalkingclose"
            call sceneimg
            if myrandom == 1:
                $ position = "avastandsbellylook"
                call sceneimg
                Ava "*smiles, pats belly*  Limited-edition model."
            elif myrandom == 2:
                Ava "Built-in floatation— very practical."
            else:
                Ava "Hey, I work hard on my six-pack… of beer."

            $ reputationchange = 2
            $ nigirlimage = "niava"
            call reputationchange
            return

        "Risky belly poke" if ava_fullstage >= 5:
            $ myrandom = renpy.random.randint(1,3)

            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "Careful— that belly’s rising like pizza dough."

            $ position = "avaaftersurfingsurprisedclose"
            call sceneimg
            if myrandom == 1:
                Ava "Keep going and I’ll toss you like pizza dough."
            elif myrandom == 2:
                Ava "Watch it, chef.  This dough can still run you down."
            else:
                Ava "*raises brow*  Brave words from land-kitchen boy."

            $ reputationchange = -2
            $ nigirlimage = "niava"
            call reputationchange
            return
