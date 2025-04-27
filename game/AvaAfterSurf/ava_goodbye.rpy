##############################################################################
#  Ava – saying goodbye (human tone, rules applied)
##############################################################################

label ava_goodbye:

    # ––– Random opener from the player –––
    $ opener = renpy.random.randint(1,3)
    $ position = "avaaftersurfinglisteningclose"
    call sceneimg
    if opener == 1:
        player "Thanks for the beach time, Ava."
    elif opener == 2:
        player "That was a blast— appreciate the company."
    else:
        player "Alright, lifeguard, I’d better let you recover."

    # ––– Sign-off choices –––
    menu:

        #--------------------------------------------------#
        "Offer to walk her home":
            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "Want a walking buddy up the promenade?"

            if ava_attitude > 60:
                $ myrandom = renpy.random.randint(1,3)
                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                if myrandom == 1:
                    Ava "Sure— company sounds nice."
                elif myrandom == 2:
                    Ava "Only if you carry the cooler."
                else:
                    Ava "I’d like that— my legs feel like jelly."

                $ reputationchange = 2
                $ nigirlimage = "niava"
                call reputationchange
                # walking home line
                "Sorry, not ready yet :("

            else:
                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                Ava "That’s sweet, but I’m good.  Short stroll, then straight to bed."
                # no attitude change
            
            $ position = "avabeachaftersurfingfrontstand"
            call sceneimg
            
            jump culinarychoices

        #--------------------------------------------------#
        "Set up a sunrise surf":
            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "Dawn patrol tomorrow?  I’ll bring breakfast tacos."

            if calendar.WeekDay == "Sat":                 # surfing allowed
                $ myrandom = renpy.random.randint(1,3)
                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                if myrandom == 1:
                    Ava "Boards at first light— and extra salsa."
                elif myrandom == 2:
                    Ava "You had me at tacos.  See you before the gulls wake."
                else:
                    Ava "Perfect.  Sunrise and surf— best alarm clock."

                $ reputationchange = 2
                $ nigirlimage = "niava"
                call reputationchange
            else:
                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                Ava "Tempting, but the tide’s wrong tomorrow.  Saturday’s our window— let’s plan for then."
                # small friendly bump
                $ reputationchange = 1
                $ nigirlimage = "niava"
                call reputationchange
            $ position = "avabeachaftersurfingfrontstand"
            call sceneimg
            pause
            jump culinarychoices

        #--------------------------------------------------#
        "Keep it casual":
            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "Catch you around, then."

            $ myrandom = renpy.random.randint(1,3)
            $ position = "avaaftersurfingtalkingclose"
            call sceneimg
            if myrandom == 1:
                Ava "Definitely.  Thanks for today."
            elif myrandom == 2:
                Ava "Anytime, chef.  Stay salty."
            else:
                Ava "Later— and bring those tacos next time."

            $ reputationchange = 1
            $ nigirlimage = "niava"
            call reputationchange
            $ position = "avabeachaftersurfingfrontstand"
            call sceneimg
            pause
            jump culinarychoices

        #--------------------------------------------------#
        "Tease her about the next beer":
            $ position = "avaaftersurfinglisteningclose"
            call sceneimg
            player "Rest up— next round I’m matching you bottle for bottle."

            $ myrandom = renpy.random.randint(1,3)
            $ position = "avaaftersurfingsurprisedclose"
            call sceneimg
            if myrandom == 1:
                Ava "Ambitious… or reckless.  We’ll see."
            elif myrandom == 2:
                Ava "Bring electrolytes, hero."
            else:
                Ava "Challenge noted— ego check pending."

            $ reputationchange = -1
            $ nigirlimage = "niava"
            call reputationchange


            # $ position = "avabeachaftersurfingfrontstand"
            # call sceneimg
            # pause
            jump culinarychoices
