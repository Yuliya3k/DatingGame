label avasurfmeet:
    # Player has just swum and returns to shore, spots Ava on duty
    $ position = "avabeachsufringfar"
    call sceneimg
    player "Whew—nice swim. Oh, is that Ava over there?"

    menu:
        "Approach her":
            # Player walks over
            $ position = "avabeachsurfcloselistening"
            call sceneimg
            player "Hey Ava, I just got out of the water—everything look okay out there?"

            $ position = "avabeachsurfclosetalking"
            call sceneimg
            Ava "All clear! I noticed you swimming and wanted to make sure you weren’t drifting too far."

            # Three small‑talk choices
            menu:
                "What made you become a lifeguard?":
                    $ position = "avabeachsurfclosesmiling"
                    call sceneimg
                    player "What drew you to lifeguarding in the first place?"

                    $ position = "avabeachsurfclosetalking"
                    call sceneimg
                    Ava "I grew up swimming competitively—becoming a lifeguard was a natural step once I graduated."

                "Do you surf when you’re off duty?":
                    $ position = "avabeachsurfclosetalking"
                    call sceneimg
                    player "When you’re not working, do you ever catch waves?"

                    $ position = "avabeachsurfcloselistening"
                    call sceneimg
                    Ava "All the time. Today’s surf is calm—perfect for a lesson if you’re interested."

                "Have you ever had a scary rescue?":
                    $ position = "avabeachsurfclosetalking"
                    call sceneimg
                    player "Ever had to dive in for a dramatic rescue?"

                    $ position = "avabeachsurfcloselistening"
                    call sceneimg
                    Ava "A few times—strong rip currents can catch people off-guard."

            # Reveal player's inexperience
            $ position = "avabeachsurfclosetalking"
            call sceneimg
            player "I’ve never even tried surfing. I’m not sure I could stand up on a board."

            $ position = "avabeachsurfcloselistening"
            call sceneimg
            Ava "No problem—I have an extra board here. Today’s waves are gentle, so it’ll be fun."

            # Ready to train
            $ avareadytotrain = True

            $ position = "avabeachsurfclosesmiling"
            call sceneimg
            player "Thanks, Ava. I’m ready to learn—lead the way!"

            $ position = "avabeachsurfclosesmiling"
            call sceneimg
            Ava "Great! Let’s head down to the water’s edge and get you started."
            $ avasurfing = True
            jump surfingoptions

        "Ignore her":
            "You do nothing and she surfs away"
            $ avaignore = True
            jump weekendbeach

        "Head back home":
            $ avaignore = False
            "..."
            jump culinarychoices

    return
