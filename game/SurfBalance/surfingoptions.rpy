label surfingoptions:

    if balancesuccess == False:
        $ position = "playerinthewater"
        call sceneimg

    if balancesuccess == True and balacesuccessfirsttime == False:
        $ balacesuccessfirsttime = True
        $ position = "avabeachsurflearningsmilingfullbody"
        call sceneimg
        Ava "Fantastic work keeping your balance!"
        Ava "You're ready to take on the waves now."        

    if balancesoso == True:
        $ position = "avabeachsurflearningsoso"
        call sceneimg
        Ava "You held on, but there’s room to improve."
        Ava "Let’s go again—focus on your center of gravity."
        Ava "Once you hit 10 seconds solid, we’ll move forward."
        

    if balancefail == True:
        $ position = "avabeachsurflearningsmilingfromabove"
        call sceneimg
        Ava "Oops—you wiped out!"
        Ava "No worries, everyone falls at first."
        Ava "Catch your breath, then we’ll give it another shot."
        

    if wavefail == True:
        
        $ position = "playerisfalling"
        call sceneimg
        #water splash sound
        # play sound "surfingfall.mp4"
        pause 1.0
        $ position = "playerinthewater"
        call sceneimg
        pause 1
        $ position = "avabeachsurflearningsmilingfromabove"
        call sceneimg
        Ava "Oh no, you missed that wave."
        Ava "It's tougher than it looks, but you'll get it."
        menu:
            "Try catching the wave again":
                jump wavecatching
            "Take a break on the shore":
                $ wavefail = False
                $ balancefail = False
                $ position = "avabeachsurflearningsmilingfromabove"
                call sceneimg
                player "I think I’ll relax on the shore for now."
                if ava_attitude > 20:
                    $ position = "avabeachsurflearningsmilingfullbody"
                    call sceneimg
                    Ava "Sure thing—I could use a break too."
                    jump avaaftersurfchoices
                    # You can add a scene of Ava drinking water here
                else:
                    $ position = "avabeachsurflearningsmilingfromabove"
                    call sceneimg
                    Ava "Alright, I’ll keep surfing a bit longer. Thanks for hanging out!"
                jump weekendbeach

    if wavesuccess == True:
        $ wavesuccess = False
        $ position = "avabeachsurflearningthmbup"
        call sceneimg
        Ava "Amazing! You caught that wave flawlessly!"
        Ava "Ready to ride out the next challenge?"
        menu:
            "Bring on the open‑ocean ride":
                call surfbalancetraining_target(7.0)
            "Rest here for a bit":
                $ wavefail = False
                $ balancefail = False
                $ position = "avabeachsurflearningsmilingfromabove"
                call sceneimg
                player "I think I’ll relax on the shore for now."
                if ava_attitude > 20:
                    $ position = "avabeachsurflearningsmilingfullbody"
                    call sceneimg
                    Ava "Sure thing—I could use a break too."
                    jump avaaftersurfchoices
                    # You can add a scene of Ava drinking water here
                else:
                    $ position = "avabeachsurflearningsmilingfromabove"
                    call sceneimg
                    Ava "Alright, I’ll keep surfing a bit longer. Thanks for hanging out!"
                jump weekendbeach
                

    if wavesoso == True:
        $ wavesoso = False
        $ position = "avabeachsurflearningsoso"
        call sceneimg
        Ava "You caught the wave, but it was a bit shaky."
        Ava "Let’s work on your balance before we try again."
        menu:
            "Try catching the wave again":
                jump wavecatching
            "Take a break on the shore":
                jump weekendbeach

    menu:
        "Try again" if balancefail == True or balancesoso == True:
                       
            $ balancesoso = False
            $ position = "avabeachsurflearningtalking"
            call sceneimg
            Ava "Alright, let’s do this once more. You’ve got it!"
            jump balancetraining
            
        "Go wavesurfing" if balancesuccess == True:
            $ position = "avabeachsurflearningthmbup"
            call sceneimg
            Ava "Sweet! Let’s catch some real waves."
            Ava "Watch me, then jump on when you’re ready."
            jump wavecatching

        "Learn surfing" if balancefail == False and balancesoso == False and balancesuccess == False:
            # Ava invites you to go over fundamentals again
            $ position = "avabeachsurflearninglistening"
            call sceneimg
            Ava "Sure—let's go over the fundamentals one more time."

            # Stance explanation
            $ position = "avabeachsurflearningtalking"
            call sceneimg
            Ava "First, plant your feet shoulder-width apart, perpendicular to the board."

            $ position = "avabeachsurflearningsmilingfullbody"
            call sceneimg
            Ava "Bend your knees slightly, like you’re ready to spring up if needed."

            # Weight distribution
            $ position = "avabeachsurflearninglistening"
            call sceneimg
            player "Okay, feet planted and knees bent."

            $ position = "avabeachsurflearningtalking"
            call sceneimg
            Ava "Good. Now lean your weight evenly—don’t tip forward or back."

            $ position = "avabeachsurflearningsmilingfromabove"
            call sceneimg
            Ava "Keep your eyes looking toward the horizon, not down at your feet."

            # Breathing and focus
            $ position = "avabeachsurflearningtalking"
            call sceneimg
            Ava "Take a deep breath, relax your shoulders, and trust the board to support you."

            $ position = "avabeachsurflearninglistening"
            call sceneimg
            player "Got it—feet, knees, eyes forward, breathe."

            $ position = "avabeachsurflearningsmilingfullbody"
            call sceneimg
            Ava "Perfect. Let’s jump back on the board and put that into practice. I’ll count us in—ready?"

            jump balancetraining
            
            

        "Head back to the beach":
            $ wavefail = False
            $ balancefail = False
            $ position = "avabeachsurflearningsmilingfromabove"
            call sceneimg
            player "I think I’ll relax on the shore for now."
            if ava_attitude > 20:
                $ position = "avabeachsurflearningsmilingfullbody"
                call sceneimg
                Ava "Sure thing—I could use a break too."
                jump avaaftersurfchoices
                
            else:
                $ position = "avabeachsurflearningsmilingfromabove"
                call sceneimg
                Ava "Alright, I’ll keep surfing a bit longer. Thanks for hanging out!"
            jump weekendbeach