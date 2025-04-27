##############################################################################
#  Ava – geeking-out about the sea (wind, waves, safety etc.)
##############################################################################

label ava_talk_sea:

    $ myrandom = renpy.random.randint(1,3)

    #------------------------------------------------------------------#
    #  1) Wind → Fetch → Swell period
    #------------------------------------------------------------------#
    if myrandom == 1:

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Ever wonder why today’s waves felt so glassy?"

        $ position = "avaaftersurfinglisteningclose"
        call sceneimg
        player "Your secret weather sense?"

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Partly.  Offshore wind plus a long fetch over open ocean makes clean, long-period groundswell."

        $ position = "avaaftersurfinglisteningclose"
        call sceneimg
        player "Translate: ‘fetch’ equals…?"

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Distance the wind keeps blowing in one direction.  Longer fetch, more energy.  Twelve-second period?  Chef’s-kiss surf.  Four-second wind-chop?  Board-rattling soup."

        menu:
            "Ask how she predicts it":
                $ position = "avaaftersurfinglisteningclose"
                call sceneimg
                player "How do you know when that juicy groundswell is inbound?"

                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                Ava "Buoy 46042, wind maps, and too many dawn patrols.  Storm sits off New Zealand on Tuesday— I’m waxing my board by Friday."

            "Ask when it gets dangerous":
                $ position = "avaaftersurfinglisteningclose"
                call sceneimg
                player "When does the same wind turn the ocean sketchy?"

                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                Ava "Onshore gusts blow the faces flat, hide rips, and shove beginners past the break.  That’s whistle time."

    #------------------------------------------------------------------#
    #  2) Tide, sandbar & break personality
    #------------------------------------------------------------------#
    elif myrandom == 2:

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "See that sandbar forty metres out?  It’s why this break only works on a mid-incoming tide."

        $ position = "avaaftersurfinglisteningclose"
        call sceneimg
        player "Because the tide changes the depth?"

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Yep.  Waves ‘feel bottom’ when depth is about 1.3× their height.  Too deep, they mush.  Too shallow, they close-out.  Sweet spot is neck-deep over that bar."

        $ position = "avaaftersurfinglisteningclose"
        call sceneimg
        player "You sound like a coastal engineer."

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Occupational hazard.  I map the sand after every winter storm— one new groyne upriver and your favourite peak can vanish."

        menu:
            "Ask about night surfing":
                $ position = "avaaftersurfinglisteningclose"
                call sceneimg
                player "High tide under a full moon… worth it?"

                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                Ava "If the swell’s small, sure.  But the rebound off that wall makes double-ups appear like ghost trains."

            "Ask about teaching beginners":
                $ position = "avaaftersurfinglisteningclose"
                call sceneimg
                player "When do you throw beginners in?"

                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                Ava "Hip-high, mid-tide, gentle offshore.  Anything else and they spend the session in the washing machine."

    #------------------------------------------------------------------#
    #  3) Rip currents & reading the water
    #------------------------------------------------------------------#
    else:

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Most folks judge the sea by wave size; I start with colour and smell."

        $ position = "avaaftersurfinglisteningclose"
        call sceneimg
        player "Smell?"

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Metallic ‘storm-coming’ tang means pressure’s dropping— squalls and cross-rips inside the hour."

        $ position = "avaaftersurfinglisteningclose"
        call sceneimg
        player "And the colour?"

        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        Ava "Tea-green stripe cutting seaward?  Rip channel.  Looks calm, deadliest water on the beach."

        menu:
            "Ask how to escape a rip":
                $ position = "avaaftersurfinglisteningclose"
                call sceneimg
                player "Say I get caught— what’s the move?"

                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                Ava "Stay flat, paddle sideways till it stops pulling, ride whitewater in.  Fight it head-on and you’re toast."

            "Show off you knew that":
                $ position = "avaaftersurfinglisteningclose"
                call sceneimg
                player "Side-paddle, then angle in with the reform.  Did my homework."

                $ position = "avaaftersurfingtalkingclose"
                call sceneimg
                Ava "Gold star, surfer-student.  Saves me sprinting with the rescue can."

    #------------------------------------------------------------------#
    #  Wrap-up – attitude +2 via helper
    #------------------------------------------------------------------#
    $ reputationchange = 2
    $ nigirlimage = "niava"
    call reputationchange
    return
