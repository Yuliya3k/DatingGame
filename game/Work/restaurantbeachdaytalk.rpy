label restaurantbeachdaytalk:

    
    if margobeachcafediscuss == False:
        $ margobeachcafediscuss = True
        $ position = "margormtalking"
        call sceneimg
        Margo "I’ve got a plan to reel more people into the restaurant."
        $ position = "margormlistening"
        call sceneimg
        Margo "Let’s run a pop-up beach café on weekdays—quick bites, iced drinks, toes in the sand."
        $ position = "margormgoodluck"
        call sceneimg
        Margo "The beach crowd never strays far from the waves. We’ll bring the waves to them! What do you think?"

        menu:
            "Ok":
                jump rbtok
            "Not ok":
                jump rbtnotok
    else:
        if rbtok > 0:
            jump rbtok
        if rbtnotok > 0:
            return

"Something gone wrong"

return


label rbtok:

    if rbtok == 0:
        $ rbtok = 1

        # ———————————————————
        #  1) Player says it’s a great idea  (randomised 3-options, 3 replicas each)
        # ———————————————————
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "That’s genius, Margo! Sun-kissed customers are always starving."
            $ position = "margormlistening"
            call sceneimg
            Margo "Exactly—nothing sells like salty hair and empty stomachs."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Let’s ride that tide."

        if myrandom == 2:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Love it! A weekday pop-up will show off our menu to a brand-new crowd."
            $ position = "margormlistening"
            call sceneimg
            Margo "Low effort, high visibility—my favourite combo."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Count me in."

        if myrandom == 3:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Great minds think alike—I’ve secretly wanted to serve tacos in flip-flops."
            $ position = "margormlistening"
            call sceneimg
            Margo "Then let’s bring the kitchen to the coast!"
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Surf and serve—done."

        # ———————————————————
        #  2) It’s the player’s job to talk to Ava (3 random options, 3 replicas each)
        # ———————————————————
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "margormlistening"
            call sceneimg
            Margo "Could you run it by Ava? She’s the lifeguard on duty and knows the beach rules inside-out."
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Sure thing—I’ll catch her at the tower after her shift."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "You’re a lifesaver!"

        if myrandom == 2:
            $ position = "margormlistening"
            call sceneimg
            Margo "We need Ava’s thumbs-up—she coordinates with the beach manager whenever events pop up."
            $ position = "margormtalking"
            call sceneimg
            "[name]" "I’ll swing by her lookout with the plan."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "Perfect. Thanks!"

        if myrandom == 3:
            $ position = "margormlistening"
            call sceneimg
            Margo "Ava spots everything from that lifeguard chair—get her blessing and we’re golden."
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Absolutely—leave the approvals to me."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "Great! Fingers crossed."

        # ———————————————————
        #  3) Player already spoke to Ava and she agreed
        # ———————————————————
    if rbtok == 1 and avarbtok == 1:
        $ rbtok = 2
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Good news—Ava loves the idea. Weekday mornings are calm, and she’ll flag it with beach admin."
            $ position = "margormlistening"
            call sceneimg
            Margo "Yes! I’ll draft a slim beach menu tonight."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Let’s make waves."

        if myrandom == 2:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "I pitched it to Ava—she said, ‘Go for it, just clean up before the evening patrol.’"
            $ position = "margormlistening"
            call sceneimg
            Margo "Deal. Eco-friendly gear, here we come."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Summer’s looking tasty."

        if myrandom == 3:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Ava’s on board—she’s even lending us spare umbrellas from the lifeguard shack."
            $ position = "margormlistening"
            call sceneimg
            Margo "Shade and lemonade—crowds will flock."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Awesome."

    # ———————————————————
    #  4) Player hasn’t spoken to Ava yet
    # ———————————————————
    if rbtok == 1 and avarbtok == 0:
        
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "I haven’t caught Ava—she’s patrolling the south stretch."
            $ position = "margormlistening"
            call sceneimg
            Margo "No worries, just find her before Friday."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "On it."

        if myrandom == 2:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Still waiting for a window—her break schedule keeps shifting."
            $ position = "margormlistening"
            call sceneimg
            Margo "The sooner we know, the sooner we order supplies."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "I’ll keep you posted."

        if myrandom == 3:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Ava left early after a rescue—I’ll track her down tomorrow."
            $ position = "margormlistening"
            call sceneimg
            Margo "Alright—I’ll hold off on flyers till then."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Makes sense."


    if rbtok == 2:
        $ rbtok = 3
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "margormtalking"
            call sceneimg
            Margo "Okay, we’re cleared to go. Could you haul the portable grill and cooler down to the boardwalk? Once they’re parked, we can pop the café open any sunny weekday."
            $ position = "margormlistening"
            call sceneimg
            player "No problem—I’ll grab a dolly and make a couple of trips."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "Perfect. One sunrise later and we’re in business!"

        if myrandom == 2:
            $ position = "margormtalking"
            call sceneimg
            Margo "Next step: gear relocation. Think you can ferry the pop-up tent, tables, and that battery blender to the lifeguard shed?"
            $ position = "margormlistening"
            call sceneimg
            player "Yeah, I’ll truck them over right after the lunch rush."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "Awesome! With the kit staged we can launch at a moment’s notice."

        if myrandom == 3:
            $ position = "margormtalking"
            call sceneimg
            Margo "Before we celebrate, we need our equipment beach-side. Can you stash the crates and signage near Ava’s tower?"
            $ position = "margormlistening"
            call sceneimg
            player "Consider it done—I'll rope in Sam to help with the heavy stuff."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "Great! Once that’s in place, we pick any weekday and just raise the shutters."
return     


label rbtnotok:

    if rbtnotok == 0:
        $ rbtnotok = 1
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "Honestly, a beach pop-up would stretch our staff too thin."
            $ position = "margormlistening"
            call sceneimg
            Margo "Hmm, I didn’t factor in scheduling."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Let’s focus on perfecting the main restaurant first."

        if myrandom == 2:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "The beach is risky—one storm and the whole setup’s gone."
            $ position = "margormlistening"
            call sceneimg
            Margo "True, weather is fickle."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Maybe revisit next season."

        if myrandom == 3:
            $ position = "margormtalking"
            call sceneimg
            "[name]" "I’m not convinced the revenue would match the effort."
            $ position = "margormlistening"
            call sceneimg
            Margo "Fair point—we could invest in targeted ads instead."
            $ position = "margormgoodluck"
            call sceneimg
            "[name]" "Exactly—more reach, less hassle."

return