label krisbackyard:
    $ position = "krisbackyardhello"
    call sceneimg
    Kris "Hello! Would you mind if I join?"
    menu:
        "Invite Kris to sit down":
            $ position = "krisbackyardtalking"
            call sceneimg
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                
                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Hey Kris! I was hoping you'd drop by. Come on in and grab a seat by the fire. I've got it going, and it's quite cozy."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "Thanks, it's lovely. You know, I've always wanted a backyard like this, but our place didn't come with one."

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Well, consider this your backyard too. And I've got a knack for grilling up some tasty snacks here. Care for some s'mores?"
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "S'mores? You've got it all figured out, huh? I'm in!"

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Great! Grab a stick, and let's get to roasting those marshmallows. So, what's been going on in your world, Kris?"
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "Not much, really. Mark's been swamped with work, so I thought I'd take a break from the routine and enjoy a quiet evening."

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Well, I'm glad you decided to join me. It's always nice to have a neighbor to share stories and s'mores with."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "Agreed. I'm looking forward to more evenings like this, and maybe one day, we can invite others from the neighborhood."

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Sounds like a plan, Kris. Our little backyard gatherings might just become a neighborhood tradition."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "I'd love that."

            if myrandom == 2:
                player "Of course! Come on in. Grab a seat by the fire. I love spending evenings here, especially with a nice, warm fire."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "Thanks, it's lovely. You know, I've always wanted a backyard like this, but our place didn't come with one."

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Well, consider this your backyard too. And I've got a knack for grilling up some tasty snacks here. Care for some s'mores?"
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "S'mores? You've got it all figured out, huh? I'm in!"

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Great! Grab a stick and let's get to roasting those marshmallows. So, what's been going on in your world, Kris?"
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "Not much, really. Mark's been swamped with work, so I thought I'd take a break from the routine and enjoy a quiet evening."
                
                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Well, I'm glad you decided to join me. It's always nice to have a neighbor to share stories and s'mores with."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "Agreed. I'm looking forward to more evenings like this, and maybe one day, we can invite others from the neighborhood."

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Sounds like a plan, Kris. Our little backyard gatherings might just become a neighborhood tradition."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "I'd love that."

            if myrandom == 3:
                
                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Hey Kris! I'm glad you could make it. I always have the fireplace going in the evenings. Please, take a seat and make yourself comfortable."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "Thanks for the invite! Your backyard looks so cozy, and I thought it'd be a great place to unwind."

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "It sure is. I love spending my evenings here. Oh, and if you're up for it, I can whip up some s'mores. It's become a bit of a tradition."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "S'mores by the fire? Count me in!"

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Awesome! Grab a stick, and we'll get roasting. So, Kris, how's everything on your side of the neighborhood?"
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "Not much, really. Mark's been swamped with work, so I thought I'd enjoy a change of scenery and some company."

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "Well, I'm delighted you came over. These evenings by the fire are even better with good company."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "I'm looking forward to it. And who knows, maybe we can invite some other neighbors in the future."

                $ position = "krisbackyardsmilingslightly"
                call sceneimg
                player "That's a fantastic idea, Kris. Our backyard gatherings might just become a neighborhood tradition."
                $ position = "krisbackyardtalking"
                call sceneimg
                Kris "I'd love that."
        "Sorry, Kris, I have no time now":
            Kris "Ok, see you later"
            $ krisnottoday = 1
            jump culinarychoices

    show screen marshmallow
    label cookloop:
        pause 1
        jump cookloop
    
    label marshmallowcom:
        $ position = "krisbackyardtalking"
        call sceneimg
        if marshmallowstate == 1:
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "I prefer them with a bit of toasting, she admits, her eyes twinkling as she waits for the fire to work its magic."
            if myrandom == 2:
                "I think I'll pass on this one, I like them slightly toasted, you know, with that irresistible golden crust."
            if myrandom == 3:
                "I've always found the roasted ones more appealing"
            show screen marshmallow
            $ marshmallowstate = 1
            jump cookloop
        if marshmallowstate == 5:
            $ marshmallowstate = 1
            
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                Kris "Thanks for offering, but I think this marshmallow might be a tad overdone for my taste. I'll pass this time."
            if myrandom == 2:
                Kris  "Wow, you really gave it your all with this marshmallow! It's a little too toasty for me, though. I'll have to skip it."
            if myrandom == 3:
                Kris  "Oh, I appreciate the marshmallow, but it seems like it got a bit carried away in the flames. I'll have to decline this one."
            $ marshmallowstate = 1
            show screen marshmallow
            jump cookloop
        else:
            $ position = "krisbackyardeating"
            call sceneimg
            pause
            $ position = "krisbackyardtalking"
            call sceneimg
            if cookingskill > 60:
                if kris_fullstage == 1:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "Oh, my stomach's growling up a storm. Time to feed this hungry beast!"
                    if myrandom == 2:
                        "Oh, my stomach's rumbling! Looks like it's high time for a hearty meal."
                if kris_fullstage == 2:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "Hm, I can feel a bit of hunger creeping in. Maybe it's snack o'clock?"
                    if myrandom == 2:
                        "I can feel that hunger creeping in. It's telling me it's time to think about eating something soon."
                if kris_fullstage == 3:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "A subtle grumble from my belly, but it's not too demanding yet."
                    if myrandom == 2:
                        "A gentle grumble from my stomach, but nothing urgent. I'll keep an eye on it."
                if kris_fullstage == 4:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "I'm getting a little peckish. A snack might be a good idea."
                    if myrandom == 2:
                        "I'm starting to feel a bit peckish. Maybe a little snack would hit the spot."
                if kris_fullstage == 5:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "Ah, just right. I'm content and not hungry or full."
                    if myrandom == 2:
                        "Ah, just right. Not hungry, not full. I'm comfortably satisfied."
                if kris_fullstage == 6:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "Okay, I'm starting to feel a subtle fullness, but I could definitely have a little more."
                    if myrandom == 2:
                        "A subtle fullness is starting to set in. I could have a bit more, but I'm not in a hurry."
                if kris_fullstage == 7:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "I'm pleasantly full, not too stuffed but quite satisfied."
                    if myrandom == 2:
                        "I'm feeling moderately full now, content but not pushing it."
                if kris_fullstage == 8:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "I can tell I'm getting full. Maybe it's time to stop and save some room for later."
                    if myrandom == 2:
                        "Notably full, but not quite there yet. I should think about saving room for later."
                if kris_fullstage == 9:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "Feeling pretty full now. I might want to put down my fork and avoid overdoing it."
                    if myrandom == 2:
                        "I'm getting quite full. Maybe it's time to put the fork down and enjoy the rest later."
                if kris_fullstage == 10:
                    #video here
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        "Oh dear, I pushed it a bit too far. My stomach is protesting, definitely time to stop eating!"
                    if myrandom == 2:
                        "Whoa, I might have overdone it. My stomach's protesting now. Time to take it easy."
                
                $ kris_fullness += 200                    
                $ niimage = "fullness"
                $ nigirlimage = "nikris"
                $ notify_success("+200")
                pause 1
                $ kris_calories += 200
                $ niimage = "calories"
                $ nigirlimage = "nikris"
                $ notify_success("+200")
                $ position = "krisbackyardsmilingslightly"
                call sceneimg
            if cookingskill > 30 and cookingskill <= 60:
                if kris_fullstage > 7:
                    $ position = "krisbackyardtalking"
                    call sceneimg
                    $ myrandom = renpy.random.randint(1,3)
                    if myrandom == 1:
                        Kris "My belly is officially in a marshmallow-induced food coma. If I eat another one of these, I might just burst. Time to take a marshmallow break!"     
                    if myrandom == 2:
                        Kris "My stomach is protesting! These marshmallows were delightful, but I might have overindulged just a tad. Time to give my belly a break."
                    if myrandom == 3:
                        Kris "I didn't expect marshmallows to be so filling, she says with a satisfied sigh, her voice deeper and slower, revealing her fullness." 
                    jump culinarychoices  
                else:
                    if kris_fullstage == 1:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "Oh, my stomach's growling up a storm. Time to feed this hungry beast!"
                        if myrandom == 2:
                            "Oh, my stomach's rumbling! Looks like it's high time for a hearty meal."
                    if kris_fullstage == 2:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "Hm, I can feel a bit of hunger creeping in. Maybe it's snack o'clock?"
                        if myrandom == 2:
                            "I can feel that hunger creeping in. It's telling me it's time to think about eating something soon."
                    if kris_fullstage == 3:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "A subtle grumble from my belly, but it's not too demanding yet."
                        if myrandom == 2:
                            "A gentle grumble from my stomach, but nothing urgent. I'll keep an eye on it."
                    if kris_fullstage == 4:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "I'm getting a little peckish. A snack might be a good idea."
                        if myrandom == 2:
                            "I'm starting to feel a bit peckish. Maybe a little snack would hit the spot."
                    if kris_fullstage == 5:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "Ah, just right. I'm content and not hungry or full."
                        if myrandom == 2:
                            "Ah, just right. Not hungry, not full. I'm comfortably satisfied."
                    if kris_fullstage == 6:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "Okay, I'm starting to feel a subtle fullness, but I could definitely have a little more."
                        if myrandom == 2:
                            "A subtle fullness is starting to set in. I could have a bit more, but I'm not in a hurry."
                    if kris_fullstage == 7:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "I'm pleasantly full, not too stuffed but quite satisfied."
                        if myrandom == 2:
                            "I'm feeling moderately full now, content but not pushing it."
                    $ kris_fullness += 200
                    
                    $ niimage = "fullness"
                    $ nigirlimage = "nikris"
                    $ notify_success("+200")
                    pause 1
                    $ kris_calories += 200
                    $ niimage = "calories"
                    $ nigirlimage = "nikris"
                    $ notify_success("+200")
                    $ position = "krisbackyardsmilingslightly"
                    call sceneimg
            
            
            if cookingskill >= 0 and cookingskill <= 30:
                if kris_fullstage > 4:
                    $ position = "krisbackyardtalking"
                    call sceneimg
                    $ myrandom = renpy.random.randint(1,3)
                    if myrandom == 1:
                        Kris "Okay, now I'm starting to understand why they say 'too much of a good thing.' My belly's got that pleasantly stretched feeling, but any more marshmallows, and I might just roll away!"    
                    if myrandom == 2:
                        Kris "I feel like I'm going to explode! These marshmallows were too tempting to resist, but now, I'm paying the delicious price."
                    if myrandom == 3:
                        Kris "I think I might have reached my marshmallow limit"
                    jump culinarychoices   
                else:
                    if kris_fullstage == 1:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "Oh, my stomach's growling up a storm. Time to feed this hungry beast!"
                        if myrandom == 2:
                            "Oh, my stomach's rumbling! Looks like it's high time for a hearty meal."
                    if kris_fullstage == 2:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "Hm, I can feel a bit of hunger creeping in. Maybe it's snack o'clock?"
                        if myrandom == 2:
                            "I can feel that hunger creeping in. It's telling me it's time to think about eating something soon."
                    if kris_fullstage == 3:
                        $ myrandom = renpy.random.randint(1,2)
                        if myrandom == 1:
                            "A subtle grumble from my belly, but it's not too demanding yet."
                        if myrandom == 2:
                            "A gentle grumble from my stomach, but nothing urgent. I'll keep an eye on it."
                    
                    $ kris_fullness += 200
                    
                    $ niimage = "fullness"
                    $ nigirlimage = "nikris"
                    $ notify_success("+200")
                    pause 1
                    $ kris_calories += 200
                    $ niimage = "calories"
                    $ nigirlimage = "nikris"
                    $ notify_success("+200")
                    $ position = "krisbackyardsmiling"
                    call sceneimg

            


        $ marshmallowstate = 1
        show screen marshmallow
        jump cookloop



                  