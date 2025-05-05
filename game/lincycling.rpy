label lincycling:  

    
        
    # if linrideabikesat == 0:
    #     $ myrandom = renpy.random.randint(1,3)
    #     if myrandom == 1:
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg
    #         player "Lin, today's ride was fantastic. Thanks for leading the way and showing me those amazing trails."
    #         $ position = "linbikeparktalkclose"
    #         call sceneimg

    #         Lin "I'm so glad you enjoyed it! It was great having you along. We should definitely do this again soon."
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg

    #         player "Absolutely, I'd love that. Let's plan another ride in the near future. You've shown me a new side to cycling."
    #         $ position = "linbikeparktalkclose"
    #         call sceneimg

    #         Lin "It's a date! Take care and rest up after today's workout. You did really well out there."
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg

    #         player "Thanks, Lin. You too. Have a great rest of your day!"
    #     if myrandom == 2:
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg

    #         player "What an exhilarating ride, Lin! I had a blast. You really know how to pick a route."
    #         $ position = "linbikeparktalkclose"
    #         call sceneimg

    #         Lin "It's always more fun with good company. I'm happy you had a good time. Let's not wait too long for our next ride!"
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg

    #         player "Definitely, count me in. It's always a pleasure riding with you. Thanks for a great day."
    #         $ position = "linbikeparktalkclose"
    #         call sceneimg

    #         Lin "You're welcome! And thank you for joining me. See you soon, and take care!"
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg

    #         player "See you, Lin. Enjoy the rest of your day!"
    #     if myrandom == 3:
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg

    #         player "Lin, that was an amazing cycling experience. Thanks for inviting me along."
    #         $ position = "linbikeparktalkclose"
    #         call sceneimg

    #         Lin "Of course! It’s always more enjoyable with a friend. I hope we can do it again sometime."
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg

    #         player "I'd really like that. You’ve made cycling even more enjoyable for me. Let's plan another outing soon."
    #         $ position = "linbikeparktalkclose"
    #         call sceneimg

    #         Lin "Sounds like a plan! Have a great rest of your day and take it easy after all that pedaling."
    #         $ position = "linbikeparklisteningclose"
    #         call sceneimg

    #         player "Will do, Lin. You too, take care!"
    #     jump culinarychoices


    $ position = "linbikeparkmeeting"
    call sceneimg
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        

        player "Hey Lin, ready for our cycling adventure? It's a perfect day for it!"
        $ position = "linbikeparktalkclose"
        call sceneimg

        Lin "Absolutely! I've been looking forward to this. It's great to switch things up from hiking to cycling."
        $ position = "linbikeparklisteningclose"
        call sceneimg

        player "Same here. It's always exciting to explore new trails. Have you got your water and snacks?"
        $ position = "linbikeparktalkclose"
        call sceneimg

        Lin "All set. I brought some energy bars too. Let's hit the road and enjoy the ride!"
        $ position = "linbikeparklisteningclose"
        call sceneimg

        player "Fantastic, let's make the most of it. And who knows, we might find some new inspiration for our cooking and training."

    if myrandom == 2:
        

        player "Good morning, Lin! Ready to conquer some trails on our bikes today?"
        $ position = "linbikeparktalkclose"
        call sceneimg

        Lin "Morning! Yes, I can't wait. It's always refreshing to get out and pedal through nature."
        $ position = "linbikeparklisteningclose"
        call sceneimg

        player "Couldn't agree more. Cycling gives a whole new perspective on the outdoors. Did you bring everything you need?"
        $ position = "linbikeparktalkclose"
        call sceneimg

        Lin "I did, including plenty of water. I'm all about staying hydrated on these rides."
        $ position = "linbikeparklisteningclose"
        call sceneimg

        player "Excellent. Stay safe, and let's enjoy the journey. Maybe we'll find a nice spot for a break and a snack."
    if myrandom == 3:
        

        player "Hey Lin, great to see you! Ready for some cycling fun?"
        $ position = "linbikeparktalkclose"
        call sceneimg

        Lin "Definitely, it's a nice change from our regular hikes. I'm all geared up for today."
        $ position = "linbikeparklisteningclose"
        call sceneimg

        player "That's the spirit. Cycling is a great way to mix up our fitness routine. You got your helmet and gear?"
        $ position = "linbikeparktalkclose"
        call sceneimg

        Lin "Yes, safety first! And I packed some light snacks too. Can't wait to see what the trail has in store for us."
        $ position = "linbikeparklisteningclose"
        call sceneimg

        player "Perfect, let's keep it safe and enjoyable. Maybe we’ll discover some scenic spots for future outings."

    menu: 
        "So what route should we choose?":
            menu:
                "Hard":
                    if lin_attitude < 20:
                        $ position = "linbikeparkridingstanding"
                        call sceneimg

                        # Opening exchange (player already falling behind)
                        player "Huff… Lin—could you—*wheeze*—slow down?"
                        Lin "Hill’s only half done, champ! Stay on my wheel."

                        # Player gets three ways to respond:
                        menu:
                            "You try to say something between ragged breaths.":
                                menu:
                                    "Cramp! My calves are on fire!":
                                        player "Left calf just seized… I’m about to tip over."
                                        Lin "Stand and stretch it out—tiny circles, easy gears. You’ve got this!"
                                        
                                    "I can taste pennies… is that normal?":
                                        player "Metallic taste—lungs feel like they’re shredding."
                                        Lin "Classic lactic flood. Deep belly breaths—use the down‑stroke to exhale."
                                    "Go on without me—save yourself!":
                                        player "Tell my spatula… I loved it."
                                        Lin "Drama queen. Coast a second, then catch my draft; I’m not leaving you behind."
                                        $ reputationchange = -1
                                        $ nigirlimage = "nilin"
                                        call reputationchange
                                        pause 0.6

                        $ calorieschange = -200
                        $ nigirlimage = "nilin"
                        call calorieschange
                        pause 0.6
                        # Lin offers encouragement, but the player is still dragging.
                        Lin "Remember, pace over pride. Spin easy—momentum beats mashing."
                        player "Noted… also dying… noted."

                        jump afterridingloop
                    if lin_attitude < 60 and lin_attitude >= 20:
                        $ position = "linbikeparkridingstanding"
                        call sceneimg

                        # Opening struggle
                        player "Ngh… legs feel like molten lead!"
                        Lin "That means you’re working the right zone. Keep steady—almost cresting."

                        # Player picks a breathless reply
                        menu:
                            "Between gasps you manage to say…":
                                menu:
                                    "If I black out, donate my bike to science.":
                                        player "Tell the world this hill was vicious."
                                        Lin "You’ll live—and brag—by the time we’re down the other side."
                                    "Any secret breathing trick?":
                                        player "I’m hyperventilating here."
                                        Lin "Four‑count inhale, six‑count exhale. Let the pedals set the rhythm."
                                    "I’m regretting every pastry I ever baked.":
                                        player "Espresso‑crème danish, why have you forsaken me?"
                                        Lin "Burn it now, earn it later—pastries taste sweeter after a climb."

                        # Crest the hill – success scene
                        $ position = "linbikeparktalkclose"
                        call sceneimg

                        $ calorieschange = -200
                        $ nigirlimage = "nilin"
                        call calorieschange

                        "You roll onto the ridge, lungs burning but still upright."
                        Lin "See? You conquered it. Proud coach moment."
                        player "Proud puddle of sweat… but thanks."

                        # Stat boost
                        $ reputationchange = 1
                        $ nigirlimage = "nilin"
                        call reputationchange

                        jump afterridingloop
                    if lin_weightstage >=4:
                        $ position = "linbikeparkridingstanding"
                        call sceneimg

                        "You spin smoothly up the climb."
                        player "Nice breeze—legs feel good."
                        Lin "Hah… speak… for yourself…!"

                        menu:
                            "How do you respond while she’s panting?":
                                menu:
                                    "Encourage her gently":
                                        player "Deep breaths, small gears—you’ve got this."
                                        Lin "Trying… but these hills are rude!"
                                    "Offer to push her saddle": 
                                        player "Want a little push on the back wheel?"
                                        Lin "Appreciate the thought—pride says no, lungs say maybe."
                                    "Tease her (lightly)":
                                        player "Trainer’s getting schooled by the chef today?"
                                        Lin "*Wheeze*—rub it in why don’t you."

                        "Lin grits her teeth, jersey stretched over her mid‑section as she powers upward."

                        $ position = "linbikeparktalkclose"
                        call sceneimg

                        $ calorieschange = -50
                        $ nigirlimage = "nilin"
                        call calorieschange
                        
                        Lin "Ugh… that hill exposed my weak spot."
                        player "Hey, effort beats ease—respect."
                        Lin "Thanks, but I need to up my conditioning…"

                        # She’s a bit embarrassed → attitude down
                        $ reputationchange = -2
                        $ nigirlimage = "nilin"
                        call reputationchange                      
                    
                                    
                        jump afterridingloop

                "Easy":
                    $ position = "linbikeparkridingsitting"
                    call sceneimg

                    "You and Lin roll side‑by‑side, breaths easy, cadence relaxed."

                    Lin "Nice rhythm. Looks like you could talk the whole ride!"

                    menu:
                        "You chat while pedaling.":
                            menu:
                                "Point out the scenery":
                                    player "Check that sunbeam through the pines—feels like riding in a postcard."
                                    Lin "Moments like this sell people on cycling."
                                "Ask about ideal cadence":
                                    player "You aim for, what, 90 RPM on flats?"
                                    Lin "Exactly. Efficient power band. You’ve been doing your homework!"
                                "Share your favorite recovery snack":
                                    player "Post‑ride? Almond butter banana sandwich—chef’s secret."
                                    Lin "Protein plus potassium—your kitchen’s on point."

                    Lin "Love riders who appreciate the details. You’re good company."

                    $ reputationchange = 1
                    $ nigirlimage = "nilin"
                    call reputationchange     # Award the reputation point
                    jump afterridingloop
    
    # else:
    #     pass

    "Something went wrong"
    jump culinarychoices

label afterridingloop:
    $ myrandom = renpy.random.randint(1,2)
    if myrandom == 1:
        $ position = "linbikeparkridingsitting"
        call sceneimg
    if myrandom == 2:
        $ position = "linbikeparkridingstanding"
        call sceneimg

    menu: # after the training talk
        "About bikes":
            menu:
                "How to choose":
                    call choosebike
                "What are health benefits":
                    if not _seen_health:
                        $ _seen_health = True

                        # Lin explains
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "Cycling is sneaky medicine: it spikes your heart rate without shredding your joints, lights up every core muscle, and turbocharges leg power."

                        # Player adds a quip
                        $ position = "linbikeparklisteningclose"
                        call sceneimg
                        player "All that while I sit down? My couch is going to feel jealous."

                        # Lin wraps up
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "Plus—it floods your brain with endorphins and vitamin D, and the only fuel it burns is breakfast."

                    else:
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "Heart, core, mood boost—same miracle package."
                "How long does she rides":
                    if not _seen_history:
                        $ _seen_history = True

                        # Lin answers
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "First ride? I was fourteen, wobbling on a hand‑me‑down ten‑speed with brakes that screamed louder than I did."

                        # Player reacts
                        $ position = "linbikeparklisteningclose"
                        call sceneimg
                        player "From rusty shriek‑machine to park‑crushing coach—nice upgrade arc."

                        # Lin continues
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "Yeah. Twenty‑odd years, a dozen bikes, and more sunrise rides than I can count. Still feels like freedom every time."

                    else:
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "Fourteen years old, junkyard bike, never stopped pedaling—same story."
        "About body image modern trends":
            if not _seen_bodyintro:
                $ _seen_bodyintro = True
                $ myrandom = renpy.random.randint(1,3)

                if myrandom == 1:
                    # Trainer’s influence
                    $ position = "linbikeparklisteningclose"
                    call sceneimg
                    player "Lin, as a trainer you set the tone—your words shape how clients see their own bodies."

                    $ position = "linbikeparktalkclose"
                    call sceneimg
                    Lin "Exactly. If I preach perfection only, I risk breeding insecurity instead of strength."

                elif myrandom == 2:
                    # Chef’s influence
                    $ position = "linbikeparklisteningclose"
                    call sceneimg
                    player "And me, as a cook, every dish I plate sends a message—indulgence, restraint, joy."

                    $ position = "linbikeparktalkclose"
                    call sceneimg
                    Lin "Food culture is powerful. A thoughtful menu can boost confidence—or feed guilt."

                else:
                    # Joint responsibility
                    $ position = "linbikeparklisteningclose"
                    call sceneimg
                    player "Together we have double impact—my kitchen and your coaching shape body-image trends."

                    $ position = "linbikeparktalkclose"
                    call sceneimg
                    Lin "Co-authors of self-worth. Let’s make our chapters about balance and self-love."

            menu:
                "About fit people" if _fitpeople == False:
                    
                    # 3 options of the idea for each topic below is why we feel what we feel about fit people. about evolution, hunting, something like this
                    menu:
                        "Healthy" if _seen_fit_healthy == False:
                            
                            $ _seen_fit_healthy = True

                            # Player asks
                            $ position = "linbikeparklisteningclose"
                            call sceneimg
                            player "Fit bodies signal resilience—lower disease risk and longer lifespans."

                            # Lin answers
                            $ position = "linbikeparktalkclose"
                            call sceneimg
                            Lin "Exactly. Evolution wired us to value health—it’s the foundation of everything."                            
                            

                        "Good looking":
                            if not _seen_fit_goodlooking:
                                $ _seen_fit_goodlooking = True

                                # Player comments
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Lean muscle and symmetry read as beauty across cultures."

                                # Lin responds
                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Nature’s rule: symmetry signals genetic strength. It’s hard-wired attraction."

                            else:
                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Symmetry and tone—classic beauty markers."
                            

                        "High energy" if _seen_fit_highenergy == False:
                            
                            $ _seen_fit_highenergy = True

                            # Player notes
                            $ position = "linbikeparklisteningclose"
                            call sceneimg
                            player "Athletic bodies run longer, recover faster—they’re like human dynamos."

                            # Lin elaborates
                            $ position = "linbikeparktalkclose"
                            call sceneimg
                            Lin "Right. Endurance breeds vitality—energy on tap all day."

                            

                            $ _fitpeople = True

                
                "About fat people":
                    if not _seen_fat_intro:
                        $ _seen_fat_intro = True
                        $ myrandom = renpy.random.randint(1,3)

                        if myrandom == 1:
                            # Evolutionary angle
                            $ position = "linbikeparklisteningclose"
                            call sceneimg
                            player "Back in the day, fat was survival fuel—our bodies stored reserves for lean times."
                            
                            $ position = "linbikeparktalkclose"
                            call sceneimg
                            Lin "Exactly. In hunter-gatherer eras, extra padding meant you’d outlast the droughts."

                        elif myrandom == 2:
                            # Wealth & status angle
                            $ position = "linbikeparklisteningclose"
                            call sceneimg
                            player "Throughout history, fuller figures signaled wealth and access to plentiful food."
                            
                            $ position = "linbikeparktalkclose"
                            call sceneimg
                            Lin "Yes—only the affluent could afford to carry those extra curves."

                        else:
                            # Pleasure & relaxation angle
                            $ position = "linbikeparklisteningclose"
                            call sceneimg
                            player "Today, many see a rounder shape as the freedom to enjoy life’s pleasures without guilt."
                            
                            $ position = "linbikeparktalkclose"
                            call sceneimg
                            Lin "True—balance isn’t just about workouts, it’s about savoring every moment."
                    menu:
                        "May be unhealthy, but only in 80 percent of cases":
                            $ myrandom = renpy.random.randint(1, 3)

                            if myrandom == 1:
                                # Genetics can protect
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Did you know about 20 % of heavier folks have healthy blood pressure and cholesterol thanks to genetics?"
                                
                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Exactly. Those ‘metabolically healthy obese’ prove genes and fat distribution matter big-time."

                            elif myrandom == 2:
                                # Activity mitigates risk
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Studies show regular exercise offsets many weight-related risks, even when BMI runs high."
                                
                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Right—movement and muscle mass trump a number on the scale every time."

                            else:
                                # Holistic health view
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "True wellness includes sleep, stress, and diet. Weight alone doesn’t tell the full story."
                                
                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Well said. I coach habits more than body shapes—health is a 360° game."
                        "They know how to relax":
                            
                            $ myrandom = renpy.random.randint(1, 3)

                            if myrandom == 1:
                                # Downtime wisdom + reality check
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "I admire how heavier folks prioritize downtime—knowing rest fuels better performance later."
                                
                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Rest days beat overtraining, but only if you’ve actually worked those muscles hard. Otherwise, you’re just… lounging. And believe it or not, many with higher BMI struggle with anxiety—this ‘always calm’ myth? Far from the truth."

                            elif myrandom == 2:
                                # Savoring life + nuance
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "They seem to savor life’s small joys—slow mornings, long meals—without guilt."
                                
                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Absolutely—mental rest is key. But muscle recovery only counts when you’ve stressed the fibers first. And that laid-back vibe? A lot of folks hide real worries behind it, especially if they’ve carried extra weight for years."

                            else:
                                # Self-care strength + myth-busting
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Their body language tells me they’ve mastered self-care—relaxation is their secret strength."
                                
                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Self-care is crucial, yes—but only after you push your limits. Otherwise it’s just sitting around. And while some project calm, statistics show higher-weight individuals often wrestle with anxiety—true peace isn't guaranteed by size."

                        "Good looking?":
                            $ myrandom = renpy.random.randint(1, 3)

                            if myrandom == 1:
                                # Self-care & styling angle
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Beauty often starts with self-care—good grooming, style choices, even cosmetic tweaks."

                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "True, but most people don’t invest in themselves that way—so it rarely translates to the street."

                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Celebrities pull it off because they work with pros. If someone’s active and intentional, any body can look stunning."

                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Fair point—and you, with your chef’s discipline and my training, would both turn heads at any size."

                            elif myrandom == 2:
                                # Celebrity contrast
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Every time a star gains weight, some cry foul—but others swoon. They still look amazing."

                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Celebs have stylists, trainers, sometimes surgery—that’s not the norm."

                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Exactly. In everyday life, activity and confidence matter more than a number."

                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "And I suppose that means you—and I—could rock it, no matter what the scale says."

                            else:
                                # Confidence & activity
                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "Confidence transforms perception. A person who owns their presence can look striking at any weight."

                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Confidence helps, but without movement and strength, it can ring hollow."

                                $ position = "linbikeparklisteningclose"
                                call sceneimg
                                player "That’s why active folks—like you—shine: muscle tone plus self-assurance is the real combo."

                                $ position = "linbikeparktalkclose"
                                call sceneimg
                                Lin "Flattery and truth—nice one. I’d like to think I’d look great either way."
                "About big bellies":
                    if not _seen_belly_intro:
                        $ _seen_belly_intro = True

                        # Lin opens on the undeniable beauty of pregnant bellies
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "There’s nothing more powerful than a belly carrying new life—those curves glow with strength and purpose."

                        # Player echoes
                        $ position = "linbikeparklisteningclose"
                        call sceneimg
                        player "Pregnancy radiance is real—soft, full, and absolutely stunning."

                        # Lin elaborates
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "Exactly. That fullness isn’t just shape, it’s story: growth, nurture, and hope personified."

                    # this is a more polarized opinions here, people tend to say what they are intended to say, not what they feel, so in this section first we should start with pregnant bellies, noone can argue that they are beautiful and we should Lin and player to discuss why it is so. And after they will discuss about pregnancy all the topics, Foodbabies should reveal and Lin should be persuaded and agree only if her lin_attritude is > 50, that it is beautiful, so other options will be a fail to persuade and a loss in lin-attitude
                    menu:
                        "Pregnant bellies":
                            menu:
                                "Beautiful":
                                    $ myrandom = renpy.random.randint(1, 3)

                                    if myrandom == 1:
                                        # Transcendent creation
                                        $ position = "linbikeparktalkclose"
                                        call sceneimg
                                        Lin "There’s something transcendent in the curve of a pregnant belly—like seeing the universe’s promise take shape."

                                        $ position = "linbikeparklisteningclose"
                                        call sceneimg
                                        player "It truly fills me with awe—nature’s greatest artwork."

                                    elif myrandom == 2:
                                        # Softness meets strength
                                        $ position = "linbikeparktalkclose"
                                        call sceneimg
                                        Lin "That soft, rounded form holds unbelievable strength—a fortress of life and love."

                                        $ position = "linbikeparklisteningclose"
                                        call sceneimg
                                        player "It’s both delicate and formidable; I can’t take my eyes off it."

                                    else:
                                        # Canvas of new life
                                        $ position = "linbikeparktalkclose"
                                        call sceneimg
                                        Lin "A belly that carries life is nature’s own canvas—every curve tells a story of hope."

                                        $ position = "linbikeparklisteningclose"
                                        call sceneimg
                                        player "Absolutely breathtaking. It’s the purest symbol of creation."
                                "Glowing":
                                    # Three random takes on “Glowing” without contractions
                                    $ myrandom = renpy.random.randint(1, 3)

                                    if myrandom == 1:
                                        # Quiet joy
                                        $ position = "linbikeparktalkclose"
                                        call sceneimg
                                        Lin "There is a gentle radiance around every expectant mother her face seems to light up with a steady calm joy."

                                        $ position = "linbikeparklisteningclose"
                                        call sceneimg
                                        player "I can feel the warmth she carries as vividly as the morning sun."

                                    elif myrandom == 2:
                                        # Hope shining
                                        $ position = "linbikeparktalkclose"
                                        call sceneimg
                                        Lin "The glow comes from deep within it is a blend of excitement and hope shining softly in her eyes."

                                        $ position = "linbikeparklisteningclose"
                                        call sceneimg
                                        player "Her presence feels both peaceful and powerful like a beacon guiding everyone around."

                                    else:
                                        # Natural luminescence
                                        $ position = "linbikeparktalkclose"
                                        call sceneimg
                                        Lin "Life growing inside brings a natural luminescence to her features making them soft yet alive."

                                        $ position = "linbikeparklisteningclose"
                                        call sceneimg
                                        player "That soft light makes her beauty feel profound and timeless."
                                "Full of life":
                                    # Lin sets the scene
                                    $ position = "linbikeparktalkclose"
                                    call sceneimg
                                    Lin "A belly so full of life hums with energy and promise—every curve speaks of a future unfolding."

                                    # Player comments on fullness
                                    $ position = "linbikeparklisteningclose"
                                    call sceneimg
                                    player "That sense of fullness is incredible—so tangible and profound, like holding tomorrow in the palm of your hands."

                                    # Lin probes the nuance
                                    $ position = "linbikeparktalkclose"
                                    call sceneimg
                                    Lin "Are you referring to the physical sensation itself, or to how a man connects to the new life growing within her?"
                                    Lin "How can a man relate to her fullness?"
                                    menu:
                                        

                                        "We sense her nurturing energy, even if we cannot carry life":
                                            # Best response → strong praise + attitude boost
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "Men cannot bear children, yet we feel her gentle swell—each tiny heartbeat a reminder of her strength and grace."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "Beautifully said. Honoring that inner journey binds us closer to her experience and her courage."
                                            $ reputationchange = 2
                                            $ nigirlimage = "nilin"
                                            call reputationchange
                                            $ _preg_right_answer = True

                                        "A pregnant belly shows she is nourished and deeply cared for":
                                            # Good response → moderate praise + small boost
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "To me, that roundness is the purest sign she is safely nourished and cherished—the quintessence of care I strive to provide."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "Indeed. Providing that nourishment is an act of love—her glow comes from being truly supported."
                                            $ reputationchange = 1
                                            $ nigirlimage = "nilin"
                                            call reputationchange
                                            $ _preg_right_answer = True
                                        "She looks like she ate a feast":
                                            # Fetish-style response → Lin frowns + attitude penalty
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "When she looks that full, it feels right to feed her every desire—as if a never-ending banquet shows my devotion."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "I understand the sentiment, but reducing her to an object of feast risks missing her humanity. True care honors her dignity."
                                            $ reputationchange = -2
                                            $ nigirlimage = "nilin"
                                            call reputationchange
                                            $ _preg_right_answer = False
                        "Food babies" if _preg_right_answer == True:
                            menu:
                                "Unhealthy food babies":
                                    # Lin’s take on junk-food-induced bloat
                                    $ position = "linbikeparktalkclose"
                                    call sceneimg
                                    Lin "Food babies from junk food are the worst kind—bloated, uneasy, and a silent signal that someone ate far beyond what their body needed."

                                    # Player supports but cautions moderation
                                    $ position = "linbikeparklisteningclose"
                                    call sceneimg
                                    player "Junk food tastes good in the moment, but it tricks us into overeating. Everyone indulges once in a while, yet making it routine only leads to that uncomfortable bloat."

                                    # Lin wraps up with the health angle
                                    $ position = "linbikeparktalkclose"
                                    call sceneimg
                                    Lin "Right. It is a reminder that mindful eating—real ingredients, proper portions—is the only way to avoid those food babies."

                                "Healthy food babies":
                                    menu:
                                        # Best response (cookingskill > 50) → +2 attitude
                                        "When every bite is pure nourishment..." if cookingskill > 50:
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "When every bite is pure nourishment, a hearty appetite becomes a blessing, and I have the recipes to prove it."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "That is exactly the kind of cuisine I admire. I would be honored to taste your creations."
                                            $ reputationchange = 2
                                            $ nigirlimage = "nilin"
                                            call reputationchange

                                        # Good response → +1 attitude
                                        "A little rounded belly...":
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "A little rounded belly from wholesome meals is harmless in my view. It shows care and good health rather than excess."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "I agree. Quality ingredients and moderation form the best recipe for well being."
                                            $ reputationchange = 1
                                            $ nigirlimage = "nilin"
                                            call reputationchange

                                        # Fetish-style response → −2 attitude
                                        "I could cook and serve you so much kale and quinoa that you would struggle for air and still ask for more.":
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "I could cook and serve you so much kale and quinoa that you would struggle for air and still ask for more."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "That is too far. Nourishment must respect the body, not become a forced spectacle."
                                            $ reputationchange = -2
                                            $ nigirlimage = "nilin"
                                            call reputationchange

                                "Foodbabies are beautiful as pregnant":
                                    # Best response → +2 attitude
                                    menu:
                                        "Same strength":
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "A rounded belly—whether from new life or from a feast—carries the same quiet strength and story of care."
                                            
                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "That speaks to me. Beauty is in the narrative, not the cause of the curve."
                                            $ reputationchange = 2
                                            $ nigirlimage = "nilin"
                                            call reputationchange
                                            $ _fbarebaspreg = True

                                        # Good response → +1 attitude
                                        "Nurture glow":
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "Fullness born of rich, wholesome food still evokes that same glow of nurture and vitality."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "I can see that. Nourishing oneself with care does share a kinship with carrying life."
                                            $ reputationchange = 1
                                            $ nigirlimage = "nilin"
                                            call reputationchange
                                            $ _fbarebaspreg = True

                                        # Poor response → –2 attitude
                                        "Belly is belly":
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "Why separate them? A belly is a belly—pregnancy or paella, it all looks equally round and stunning."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "That feels dismissive. The stories behind those curves matter, and conflating them erases her journey."
                                            $ reputationchange = -2
                                            $ nigirlimage = "nilin"
                                            call reputationchange
                                "They are dynamic and this is the best thing" if _fbarebaspreg == True:
                                    menu:
                                        "Living art":
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "A big belly is like a living sculpture—it shifts with every breath, a testament to change and vitality."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "Beautifully put. That fluid motion captures life’s rhythm in a way still forms cannot."
                                            $ reputationchange = 2
                                            $ nigirlimage = "nilin"
                                            call reputationchange
                                            $ _dynamicbellies = True


                                        "Ever-changing":
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "Its shape evolves constantly—stretch and rest—reminding us that nothing in life is static."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "True. Adaptation is strength—if our bodies can flow, so can our minds."
                                            $ reputationchange = 1
                                            $ nigirlimage = "nilin"
                                            call reputationchange
                                            $ _dynamicbellies = True


                                        "Blame flat women":
                                            $ position = "linbikeparklisteningclose"
                                            call sceneimg
                                            player "You know, some of those eternally flat-chested women get jealous of curves—they mask it with animosity and fake compliments."

                                            $ position = "linbikeparktalkclose"
                                            call sceneimg
                                            Lin "That is unfair and unkind. Comparing women like that only spreads negativity—everyone’s body deserves respect."
                                            $ reputationchange = -2
                                            $ nigirlimage = "nilin"
                                            call reputationchange

        "Make her a compliment":
            $ calendar.AddMinutes(15)
            $ myrandom = renpy.random.randint(1,20)
            $ reputationchange = 1
            $ nigirlimage = "nilin"
            call reputationchange
            if myrandom == 1:
                
                
                player "You're really setting a great pace, Lin. Impressive!"
                Lin "Thanks! I've been practicing. It's nice to have a good cycling partner like you."
            if myrandom == 2:
                
                
                player "Your energy is contagious, Lin. It makes this ride even more enjoyable."
                Lin "I'm glad to hear that. Cycling with you is a lot of fun!"
            
            if myrandom == 3:
                
                
                

                player "You handle your bike so well. It's like you were born to cycle."
                Lin "That's kind of you to say. I just love being on a bike, especially on days like this."
            
            if myrandom == 4:
                
                


                player "Your enthusiasm for cycling is really motivating. It pushes me to do better."
                Lin "We motivate each other! That's what makes cycling together so rewarding."
            
            if myrandom == 5:
                
                


                player "You know, you have an incredible sense of direction on these trails."
                Lin "Thanks! I've spent a lot of time exploring these paths. It's great to share them with you."
            
            if myrandom == 6:
                
                


                player "I admire how effortlessly you tackle these hills. Truly inspiring."
                Lin "Cycling’s all about the challenge and the thrill. I’m happy to inspire you!"
                
            if myrandom == 7:
                
                

                player "Your choice of route is perfect. You really know the best spots."
                Lin "I’m glad you like it. There’s nothing like sharing my favorite trails with a friend."
            
            if myrandom == 8:
                
                


                player "You're in great shape, Lin. It's amazing how you keep up such a strong pace."
                Lin "Thanks! Regular cycling does wonders. And it's more fun with a companion like you."

            if myrandom == 9:
                
                


                player "Your stamina is something else! You’re like the Energizer Bunny on a bike."
                Lin "Haha, that's a fun comparison! I just love cycling, it energizes me."
            
            if myrandom == 10:
                
                


                player "I'm impressed by your cycling skills. You make it look so easy."
                Lin "Thank you! It's all about practice. And having a good cycling buddy helps too."
            
            if myrandom == 11:
                
                


                player "You've got a real knack for finding the most scenic routes."
                Lin "I always keep an eye out for the best views. Glad you're enjoying it."
            
            if myrandom == 11:
                
                


                player "Your enthusiasm really brightens up the ride. It’s infectious!"
                Lin "That's sweet of you to say. I always enjoy our cycling trips."
            
            if myrandom == 13:
                
                


                player "You’re like a professional cyclist. It’s amazing to watch you ride."
                Lin "You're making me blush! I just love cycling, that's all."

            if myrandom == 14:
                
                


                player "This route is fantastic. Your choice in trails is top-notch."
                Lin "I'm happy you think so. I always try to pick the best routes for us."

            if myrandom == 15:
                
                


                player "Your energy levels are incredible, Lin. I'm trying to keep up!"
                Lin "You're doing great! It’s all about enjoying the ride together."
            
            if myrandom == 16:
                
                


                player "You're an excellent guide, Lin. I feel like I'm on a professional tour."
                Lin "I’m flattered! I just want to make sure we have a great time cycling."
            
            if myrandom == 17:
                
                


                player "Your passion for cycling really shines through. It’s inspiring."
                Lin "Cycling's my way of connecting with nature. I'm glad it inspires you."

            if myrandom == 18:
                
                


                player "You've really planned out a great route. It's the perfect balance of challenge and beauty."
                Lin "Thank you! I thought you'd enjoy this mix. It's great to have you along."

            if myrandom == 19:
                
                


                player "You've got a real talent for this, Lin. Your cycling skills are top-level."
                Lin "Thanks! I’ve been cycling for a while now. It’s one of my favorite things to do."

            if myrandom == 20:
                
                


                player "You make cycling look so graceful. It’s like watching an athlete in action."
                Lin "What a compliment! I just try to be smooth and steady on the bike."
        "Wanna ice cream?":
            $ position = "icecreamlisten"
            call sceneimg
            menu:
                "Yes, let us indulge!" if _dynamicbellies == True and lin_fullness < lin_fullmax:
                    $ position = "icecreamthumbsup"
                    call sceneimg
                    player "We will take 5!"
                    
                    $ moneytoadd = -25
                    call moneynotification
                    if notenoughmoney == True:
                        jump afterridingloop
                    else:
                        # First scoop, clean
                        $ position = "linbikeparkeatinicecream1clean"
                        call sceneimg
                        Lin "Mmm… that first taste is always the best."
                        $ calorieschange = 500
                        $ nigirlimage = "nilin"
                        call calorieschange
                        pause 0.5
                        $ fullnesschange = 250
                        $ nigirlimage = "nilin"
                        call fullnesschange
                        
                        # Second scoop, messy
                        $ position = "linbikeparkeatinicecream1dirty"
                        call sceneimg
                        Lin "Oops… a little drip. Still worth it."
                        $ calorieschange = 500
                        $ nigirlimage = "nilin"
                        call calorieschange
                        pause 0.5
                        $ fullnesschange = 250
                        $ nigirlimage = "nilin"
                        call fullnesschange
                        # Third scoop, clean
                        $ position = "linbikeparkeatinicecream2clean"
                        call sceneimg
                        Lin "Another round? I cannot resist."
                        $ calorieschange = 500
                        $ nigirlimage = "nilin"
                        call calorieschange
                        pause 0.5
                        $ fullnesschange = 250
                        $ nigirlimage = "nilin"
                        call fullnesschange
                        # Fourth scoop, very messy
                        $ position = "linbikeparkeatinicecream2dirty"
                        call sceneimg
                        Lin "I am a mess, but… oh, so good."
                        $ calorieschange = 500
                        $ nigirlimage = "nilin"
                        call calorieschange
                        pause 0.5
                        $ fullnesschange = 250
                        $ nigirlimage = "nilin"
                        call fullnesschange
                        # After the feast
                        $ lin_attitude += 1
                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        Lin "Okay, I admit it… this was worth every calorie."
                        $ calorieschange = 500
                        $ nigirlimage = "nilin"
                        call calorieschange
                        pause 0.5
                        $ fullnesschange = 250
                        $ nigirlimage = "nilin"
                        call fullnesschange
                "Just one scoop, please" if lin_attitude >= 50:
                    $ position = "icecreamtalk"
                    call sceneimg
                    player "We will take 1"
                    $ moneytoadd = -5
                    call moneynotification
                    if notenoughmoney == True:
                        jump afterridingloop
                    else:
                        # Single scoop, clean then back to talk
                        $ position = "linbikeparkeatinicecream1clean"
                        call sceneimg
                        Lin "A single scoop—wise choice. Savor each bite."

                        $ position = "linbikeparktalkclose"
                        call sceneimg
                        player "I do not want to overreach."
                        $ position = "linbikeparkeatinicecream2clean"
                        call sceneimg
                        Lin "Balance is key. Enjoy it slowly."
                        $ calorieschange = 500
                        $ nigirlimage = "nilin"
                        call calorieschange
                        pause 0.5
                        $ fullnesschange = 250
                        $ nigirlimage = "nilin"
                        call fullnesschange
                "Not right now, thank you." if lin_attitude < 50:
                    $ position = "linbikeparktalkclose"
                    call sceneimg
                    Lin "Maybe later. But when the craving strikes, I will not say no."
        "Go home":
            jump culinarychoices


jump afterridingloop


                # "So you are the boss, what's the plan?" if lincyclingboss == 0:
                #     $ lincyclingboss = 1

                #     $ myrandom = renpy.random.randint(1,3)
                #     if myrandom == 1:
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg
                    

                #         player "Lin, do you have any suggestions on where we could go cycling today? Maybe somewhere with a nice view?"
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "Yes, I have the perfect place in mind. Let's head to the park. It has some fantastic views and excellent bike paths."
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "That sounds like a plan! Is it a challenging route, or more on the relaxed side?"
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "It's pretty relaxed but with enough variety to keep it interesting. The park is known for its scenic routes and lush landscapes."
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "Sounds like a photographer's dream. I'll make sure to bring my camera. Let's enjoy the day and the views!"
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "Great idea! It'll be a fun ride with lots of photo opportunities. Ready to roll out?"
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "Absolutely! Let's make the most of this beautiful day and explore the park."
                #     if myrandom == 2:
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "Lin, any thoughts on where we should cycle today? Something scenic would be lovely."
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "Definitely! Let's go to the park. It's got the best bike roads and the views are simply breathtaking."
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "Oh, that sounds wonderful. I haven't been there yet. Are the paths beginner-friendly?"
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "They are perfect for all levels. The park offers a mix of easy and slightly challenging paths, all surrounded by natural beauty."
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "That’s exactly what I was hoping for. A peaceful ride surrounded by nature. Shall we get going?"
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "Let's do it. You're going to love the views and the peaceful atmosphere. The park is a cyclist's delight."
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "Can't wait to experience it. Today's going to be a great day for a ride."
                #     if myrandom == 3:
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "Hey Lin, any good cycling spots you’d recommend for today? I’d love somewhere with great views."
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "I know just the place. How about we cycle to the park? It has some stunning views and the bike paths are top-notch."
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "Sounds like an adventure. I'm looking forward to it. Are the paths suitable for a leisurely ride?"
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "Absolutely. The park has a variety of paths, from easy to moderately challenging, all with gorgeous scenery."
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "That sounds ideal. A bit of exercise, fresh air, and nature. Let’s get going and enjoy the day."
                #         $ position = "linbikeparktalkclose"
                #         call sceneimg

                #         Lin "Yes, let's set off. The park is a beautiful spot for cycling, and I think you're going to really enjoy the ride."
                #         $ position = "linbikeparklisteningclose"
                #         call sceneimg

                #         player "Alright, let's make today an adventure. The park awaits!"


"something went wrong"
jump lincycling