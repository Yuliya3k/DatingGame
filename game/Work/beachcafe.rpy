label beachcafe:

    if beachcafeisset == False:
        $ beachcafeisset = True
        scene black with slowdissolve
        $ calendar.AddMinutes(50)
        $ calendar.AddMinutes(40)
        pause 1.0

        show text "You set the whole café up by yourself." at truecenter with slowdissolve
        pause 3.5
        hide text with dissolve

        $ position = "beachcafeassambled"
        call sceneimg
        pause


label beachcafeloop:
    $ calendar.AddMinutes(15)
        
    if margobeachbbqgreeting == False:
        $ margobeachbbqgreeting = True
        $ myrandom = renpy.random.randint(1,3)

        # # first three greeting CG beats
        # $ position = "margobeachbbqclosehi"
        # call sceneimg            
        # $ position = "margobeachbbqcloselistening"
        # call sceneimg            
        # $ position = "margobeachbbqclosetalking"
        # call sceneimg

        if myrandom == 1:
            # Margo compliments the set-up – 3-5 replicas
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Wow, look at this place! You turned a patch of sand into a five-star kiosk."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Glad it passes inspection."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "The banner catches the breeze perfectly, and the grill’s angled away from the wind—nice touch."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Figured the smoke should drift out to sea, not over customers."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Smart and stylish—chef-slash-architect in one."

        if myrandom == 2:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Everything’s lined up like a magazine spread! You nailed the vibe."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Took a few early-morning dry runs."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "The menu board, the fairy lights—chef’s kiss. Tourists will think we’ve been here all season."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Fake it till we make it, right?"
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "We’re already making it."

        if myrandom == 3:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "I can’t believe you hauled all this gear solo! You’re a one-person moving crew."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "My shoulders would like a day off now."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Earned yourself a foot massage coupon—redeemable after last call."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Deal."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Seriously, great work. This place looks incredible."

        # Margo offers serving help
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "I’ll handle the counter and drinks while you rock the grill. You’ll be knee-deep in orders."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Thanks—keeping the burgers flipping will be a full-time gig."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Just holler if the flames get rowdy."

        if myrandom == 2:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Want me on cash and smoothies? You’ll need free hands for the hot stuff."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Yes, please. Nothing worse than handling money with barbecue sauce fingers."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "I’ll keep the queue moving—watch me work."

        if myrandom == 3:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "You cook, I charm. I’ll deliver plates so customers don’t crowd your station."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Perfect division of labour."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Teamwork tastes delicious."

    if margo_fullstage > 7 and margo_fullnesscomplaint == False:
        $ margo_fullnesscomplaint = True
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Confession: I sampled one too many ribs. If my shorts look snug, pretend you don’t notice."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Your secret’s safe. The chef won’t judge."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Good, because the chef is to blame."

        if myrandom == 2:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "These burgers are dangerously good. I’m pretty sure I just ate tomorrow’s calories."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Consider it quality control."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Quality control is starting to show on my waistline."

        if myrandom == 3:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Note to self: stop taste-testing every batch of fries."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "But how else will we guarantee perfection?"
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Perfection now, gym later."

    if avabeacbbqgreeting == False:
        # Ava greeting CG beats
        # $ position = "avabeachbbqclosehi"
        # call sceneimg            
        # $ position = "avabeachbbqcloselistening"
        # call sceneimg            
        # $ position = "avabeachbbqclosetalking"
        # call sceneimg

        $ avabeacbbqgreeting = True
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            # Ava talks strict rules
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Ground rules: keep the rescue lane clear, no grease runoff into the sand, and trash straight to the blue bins."
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Copy that—safety first."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Break the rules and I blow the whistle—literally."

        if myrandom == 2:
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Remember, no glass near the shoreline and zero garbage in the dunes. I patrol those spots hourly."
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Everything’s compostable cups and paper trays—promise."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Music to my eco-ears."

        if myrandom == 3:
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "If a seagull steals a burger, it’s on you—not filing a bird complaint."
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Understood. I’ll guard the grill."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Good. Last thing I need is a food-frenzied flock."

        # Ava asks for food sometimes
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Mind if I snag a sandwich between rescues? Salt water burns calories fast."
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Kitchen’s open to lifeguards 24/7."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Sweet—I’ll pay in quick saves."

        if myrandom == 2:
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Those ribs smell incredible. Think I could trade a safety briefing for a plate?"
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Deal—knowledge for nourishment."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Best barter ever."

        if myrandom == 3:
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "I’ll be swinging by for protein bars—rescues don’t wait for meal breaks."
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Help yourself whenever."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "You’re a lifesaver in more ways than one."

    if ava_fullstage > 7 and ava_fullnesscomplaint == False:
        $ ava_fullnesscomplaint = True
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Note to self: sprint drills plus two burgers equals very tight shorts."
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Occupational hazard of good food."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Next rescue, I’ll swim it off."

        if myrandom == 2:
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "I promised myself one snack, ended up with four. If I waddle, ignore it."
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Call it energy storage."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Energy’s stored all right—right here."  

        if myrandom == 3:
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "Uniform’s snug after that plate of ribs, but totally worth it."
            $ position = "avabeachbbqcloselistening"
            call sceneimg
            player "Fashion sacrifices for flavour."
            $ position = "avabeachbbqclosetalking"
            call sceneimg
            Ava "I’ll run extra laps tomorrow."

    # cooking SFX & dish rotation

    play sound "audio/bbqsound.mp3"
    $ myrandom = renpy.random.randint(1,5)
    $ position = "bbqbg"
    call sceneimg
    pause 5
    if myrandom == 1:
        $ position = "bcroastedchicken"
        call sceneimg
        $ calorieschange = 1600
        $ fullnesschange = 1600
        pause 1
    if myrandom == 2:
        $ position = "bcsalmon"
        call sceneimg
        pause 1
    if myrandom == 3:
        $ position = "bcbbqdish"
        call sceneimg
        $ calorieschange = 300
        $ fullnesschange = 300
        pause 1
    if myrandom == 4:
        $ position = "bcribsdish"
        call sceneimg
        $ calorieschange = 500
        $ fullnesschange = 300
        pause 1
    if myrandom == 5:
        $ position = "bcburgerdish"
        call sceneimg
        $ calorieschange = 500
        $ fullnesschange = 500
        pause 1

    # ------------------------------------------------------------
    # RANDOM CUSTOMER CLOSE-UPS  — only girls who still have room
    # ------------------------------------------------------------
    python:
        # Build a list of IDs for girls who can still eat
        eligible = []

        if margo_fullness + fullnesschange  <= margo_fullmax:   eligible.append(1)
        if farida_fullness + fullnesschange <= farida_fullmax:  eligible.append(2)
        if kris_fullness + fullnesschange   <= kris_fullmax:    eligible.append(3)
        if ava_fullness + fullnesschange    <= ava_fullmax:     eligible.append(4)
        if alexa_fullness + fullnesschange  <= alexa_fullmax:   eligible.append(5)
        if aurora_fullness + fullnesschange <= aurora_fullmax:  eligible.append(6)

        # If everyone is stuffed, skip this serving round
        if eligible:
            renpy.store.myrandom = renpy.random.choice(eligible)
        else:
            myrandom = 0      # no service this tick

    # ------------------------------------------------------------
    # SHOW the chosen girl and apply her food / fullness changes
    # ------------------------------------------------------------
    if myrandom == 0:
        $ myrandom = renpy.random.randint(1,5)

        #—————————————————————————————————————————
        # 1 ▸ Everybody is stuffed – variant 1
        #—————————————————————————————————————————
        if myrandom == 1:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Chef, emergency! Every customer is rubbing their bellies and begging for mercy."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Ha! Music to my ears, but yeah—looks like we’ve hit capacity."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Me included. One more bite and I’ll literally explode confetti and barbecue sauce."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Alright then—wrap-up time."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Let’s quit while we’re all still able to walk."

        #—————————————————————————————————————————
        # 2 ▸ Everybody is stuffed – variant 2
        #—————————————————————————————————————————
        if myrandom == 2:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Status report: the crowd’s reached maximum stuffing. I just heard a collective groan of happiness."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "No room left for samples, huh?"
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Nope—I’m one forkful away from rolling down the beach like a burrito."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Then we pack up before gravity wins."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Same time next sunny day—minus the food coma."

        #—————————————————————————————————————————
        # 3 ▸ Everybody is stuffed – variant 3
        #—————————————————————————————————————————
        if myrandom == 3:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Look around—people are lolling in their chairs like happy whales."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "And you?"
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "I’m harbouring half a rack of ribs in my stomach. Call the naval engineers."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Declaration accepted: café closed for the day."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Perfect. Next time we’ll do it all over—after digestion."

        #—————————————————————————————————————————
        # 4 ▸ Everybody is stuffed – variant 4
        #—————————————————————————————————————————
        if myrandom == 4:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Chef, even the seagulls look full! We’ve officially over-fed the coastline."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "When birds stop scavenging, you know you’ve served enough."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Let’s shut the lids before someone bursts a button."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Roger that—operation clean-up begins."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Next event, we install stretchy pants on the menu board."

        #—————————————————————————————————————————
        # 5 ▸ Everybody is stuffed – variant 5
        #—————————————————————————————————————————
        if myrandom == 5:
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "I just polled the crowd: zero capacity left, unanimous satisfaction."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Good news for reviews, bad news for leftovers."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Honestly, if I inhale I can feel the grill marks from inside."
            $ position = "margobeachbbqcloselistening"
            call sceneimg
            player "Time to roll down the shutters, then."
            $ position = "margobeachbbqclosetalking"
            call sceneimg
            Margo "Deal. Let’s reconvene when bellies reset."

        #—————————————————————————————————————————
        #  Shut the café and exit to culinarychoices
        #—————————————————————————————————————————
        $ beachcafeisset = False
        scene black with slowdissolve
        $ calendar.AddMinutes(50)
        $ calendar.AddMinutes(40)
        pause 1.0

        show text "You've disassembled the café and stored it in the lifeguard's shack." at truecenter with slowdissolve
        pause 3.5
        hide text with dissolve

        jump culinarychoices

    
    if myrandom == 1:
        $ position = "margobeachbbq"
        call sceneimg
        $ nigirlimage = "nimargo"
        call fullnesschange
        pause 1
        call calorieschange
        pause 3

    if myrandom == 2:
        $ position = "faridabeachbbq"
        call sceneimg
        $ nigirlimage = "nifarida"
        call fullnesschange
        pause 1
        call calorieschange
        pause 3

    if myrandom == 3:
        $ position = "krisbeachbbq"
        call sceneimg
        $ nigirlimage = "nikris"
        call fullnesschange
        pause 1
        call calorieschange
        pause 3

    if myrandom == 4:
        $ position = "avabeachbbq"
        call sceneimg
        $ nigirlimage = "niava"
        call fullnesschange
        pause 1
        call calorieschange
        pause 3

    if myrandom == 5:
        $ position = "alexabeachbbq"
        call sceneimg
        $ nigirlimage = "nialexa"
        call fullnesschange
        pause 1
        call calorieschange
        pause 3

    if myrandom == 6:
        $ position = "aurorabeachbbq"
        call sceneimg
        $ nigirlimage = "niaurora"
        call fullnesschange
        pause 1
        call calorieschange
        pause 3
         
    if calendar.Hours > 18:
        "Time to go home!"
        $ beachcafeisset = False
        scene black with slowdissolve
        $ calendar.AddMinutes(50)
        $ calendar.AddMinutes(40)
        pause 1.0

        show text "You've disassembled the café and stored it in the lifeguard's shack." at truecenter with slowdissolve
        pause 3.5
        hide text with dissolve
        jump culinarychoices

    jump beachcafeloop
