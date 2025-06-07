label avabeach:
    



    $ myrandom = renpy.random.randint(1,2)
    if avafirstmeet > 0 and myrandom == 2 and calendar.Hours > 8 and calendar.Hours < 19:
        $ position = "beachava"
        call sceneimg
        if avafirstmeet == 1:
            $ avafirstmeet = 2
        
            "I glanced around and spotted Ava, the lifeguard, standing near the water's edge. She leaned on the weathered wooden fencing, her gaze fixed on the vast expanse of the sea. Her silhouette against the backdrop of the setting sun gave her an air of tranquility and grace."

            "I couldn't help but admire her dedication to her role as a lifeguard. The beach was her domain, and she watched over it with a vigilant eye, ready to spring into action at a moment's notice. I had seen her in her lifeguard attire before, but here, in casual clothes, she seemed even more at ease, as if the sea itself were her confidant."

            "As I drew closer, I couldn't help but wonder what thoughts occupied her mind as she stared out at the horizon. The sea had a way of inspiring reflection, and I wondered if she found solace in its boundless beauty."

            "Ava's presence was a reminder that life here had a natural rhythm, dictated by the ebb and flow of the tides. It was a stark contrast to the bustling city I had left behind, and I was beginning to appreciate the simplicity and serenity of this coastal town."

            "With a newfound sense of peace, I continued my stroll along the beach, the sound of the waves serving as a backdrop to my thoughts. Ava, the guardian of this shore, had left an impression on me, one that made me feel even more connected to this place I was beginning to call home."
        menu:
            "Come to Ava and talk":
                
                $ position = "beachavaclose"
                call sceneimg
                label avabeachloop:
                    menu:
                        "Say hello" if avasayhellotoday == 0:
                            $ avasayhellotoday = 1
                            $ myrandom = renpy.random.randint(1,3)
                            if avahello == 1:
                                if myrandom == 1:
                                    $ position = "beachavaclose"
                                    call sceneimg
                                    player "Hey, Ava, how's it going today?"
                                    $ position = "beachavaclosehey"
                                    call sceneimg
                                    Ava "Hey there! Not much action at the moment, but the day's been good so far. How about you?"
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Just enjoying the beach and the beautiful weather. It's nice to see a familiar face around here."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Absolutely! It's always good to have friendly company. If you ever need tips on the best spots to swim or relax, you know where to find me."

                                if myrandom == 2:
                                    $ position = "beachavaclose"
                                    call sceneimg
                                    player "Hi Ava! Seems like you're the guardian of this beach."
                                    $ position = "beachavaclosehey"
                                    call sceneimg
                                    Ava "You could say that. It's my turf. How's your day going?"
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Not too shabby. I'm starting to feel like a regular here. By the way, I didn't expect to see you in something other than a lifeguard uniform."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Yeah, I like to blend in with the crowd when I'm off duty. Keeps things relaxed."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "I can imagine. So, what's new in the world of lifeguarding?"

                                if myrandom == 3:
                                    $ position = "beachavaclose"
                                    call sceneimg
                                    player "Hey, Ava, long time no see! Still keeping watch over the beach?"
                                    $ position = "beachavaclosehey"
                                    call sceneimg
                                    Ava "Hey! Yep, same old routine. You've been enjoying the beach lately, I see."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Definitely. It's become one of my favorite spots in town. You know, it's funny, I first saw you at the Crave Bites, not in a lifeguard tower."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Oh, that was probably me. I like to unwind there sometimes. It's a small town; we all wear multiple hats."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "True, true. Well, it's nice to run into you again. Maybe I'll catch you at Crave Bites sometime soon."
                                
                            if avahello == 0:
                                if myrandom == 1:
                                    $ position = "beachavaclose"
                                    call sceneimg
                                    player "Hey there, enjoying the sun and waves?"
                                    $ position = "beachavaclosehey"
                                    call sceneimg
                                    Ava "Absolutely! It's a beautiful day at the beach. And speaking of enjoyment, I think we've bumped into each other before, haven't we?"
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Hmm, you seem familiar, but I can't quite put my finger on it. Have we met somewhere?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "I thought so! I was in a different outfit back then, but you saw me at Crave Bites, right?"
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Oh, right! You're the lifeguard from Crave Bites. It's a small world, isn't it?"

                                if myrandom == 2:
                                    $ position = "beachavaclose"
                                    call sceneimg
                                    player "Hey, you're the lifeguard from Crave Bites, right?"
                                    $ position = "beachavaclosehey"
                                    call sceneimg
                                    Ava "That's me! You remembered. Small world, huh?"
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Definitely! I didn't expect to see you here at the beach. It's a pleasant surprise."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "I like to spend my free time by the water, whether I'm on duty or not. What brings you to the beach today?"
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Just exploring the town and taking in the sights. The beach seemed like a great place to start."

                                if myrandom == 3:
                                    $ position = "beachavaclose"
                                    call sceneimg
                                    player "Hey, I remember you from Crave Bites! You're the lifeguard, right?"
                                    $ position = "beachavaclosehey"
                                    call sceneimg
                                    Ava "You've got a good memory. That's me! It's nice to see you again."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Likewise. I didn't expect to run into you here at the beach. Do you come here often?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Yeah, I like to spend my off-hours here, enjoying the sun and the water. It's so peaceful."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Sounds like a great way to unwind. I'm just exploring the town today. The beach seemed like a good place to start."
                                $ avahello = 1
                            
                        
                        "Do you like to work as a lifeguard?" if avalifeguard == 0:
                            $ myrandom = renpy.random.randint(1,3)
                            $ avalifeguard = 1
                            if myrandom == 1:
                                player "So, Ava, what's it like working as a lifeguard? Must be an interesting job."
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Oh, it definitely has its moments. It's important to stay vigilant and focused, especially on crowded days. You never know what might happen."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "I can imagine. Must be challenging but also rewarding."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "Absolutely. It's fulfilling knowing that you're here to help and ensure everyone stays safe in the water."

                            if myrandom == 2:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "I've always wondered, how's the experience of being a lifeguard? Is it as exciting as it looks?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Well, it can be exciting, that's for sure. There are times when we have to act quickly to keep everyone safe. But it's also about prevention and education, making sure people know how to swim safely."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "That sounds like a well-rounded role. You get to enjoy the beach and keep people safe at the same time."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "Yes, it's a unique job in that way. Plus, I get to spend a lot of time outdoors, which I love."

                            if myrandom == 3:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Lifeguarding seems like a cool job. What's a typical day like for you?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava " (reflecting) Well, it can vary quite a bit. Some days are calm and relaxing, while others can get pretty hectic, especially during peak season."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "I bet it keeps you on your toes. Any memorable experiences you'd like to share?"
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "Oh, plenty! From helping lost kids find their parents to rescuing people caught in strong currents, there's never a dull moment."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "It sounds like you're making a real difference here. Keep up the good work, Ava."

                        "Do you have any hobbies?" if avahobbies == 0:
                            $ myrandom = renpy.random.randint(1,3)
                            $ avahobbies = 1
                            if myrandom == 1:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "So, Ava, when you're not here keeping everyone safe, what do you like to do in your free time? Any hobbies?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Well, I'm quite the outdoorsy type. I enjoy hiking, camping, and anything that lets me connect with nature."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "That's awesome! I love spending time outdoors too. We should go hiking together sometime."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "I'd like that. It's always more fun with company."

                            if myrandom == 2:
                                player "Lifeguarding must keep you busy, but what do you do to unwind and relax when you're off duty?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "To relax, I like to read. I'm a bit of a bookworm, to be honest. I also dabble in painting from time to time."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Reading and painting, huh? You've got quite the artistic side. Any favorite books or themes?"
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "Oh, I enjoy a good mystery novel, and nature often inspires my paintings."

                            if myrandom == 3:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, I'm curious. What are your hobbies or interests outside of being a lifeguard?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Well, I'm a bit of a fitness enthusiast. I do yoga and hit the gym regularly. It helps me stay in shape for my job here."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "That's great. Staying fit is important. Do you have any favorite yoga poses or workout routines?"
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "I love doing sun salutations in the morning to start my day right. And as for workouts, I enjoy mixing things up, so I don't get bored."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "It sounds like you've got a healthy lifestyle going on. Maybe you could teach me some yoga moves sometime?"

                        "Tell Ava about yourself" if avayourself == 0:
                            $ myrandom = renpy.random.randint(1,3)
                            $ avayourself = 1
                            if myrandom == 1:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "By the way, Ava, I'm a cook, and I recently moved to this town. It's been quite an adventure settling in."
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "A cook? That's fascinating! Exploring new places through food must be exciting. Any favorite dishes you like to prepare?"
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Absolutely! I love experimenting with different cuisines, but I have a soft spot for classic comfort foods."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "Well, you might have to whip up something delicious for our new friends in town one day!"

                            if myrandom == 2:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Hey, Ava, just so you know, I'm a cook. I relocated here not too long ago, and I'm still getting to know the area."
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "A cook, huh? That's intriguing. Have you tried the local food scene yet? Any hidden gems you've discovered?"
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Oh, absolutely! I've been sampling different places, and there are some fantastic eateries around here."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "If you ever want some company for a food adventure, count me in!"

                            if myrandom == 3:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, I wanted to share that I'm a cook, and I moved to town recently. Figured you should know."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                Ava "Nice to meet you. I'm sure you're bringing some culinary magic to our town. What made you choose this place?"
                                
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Well, I heard this town had a unique charm, and I wanted a change of scenery to inspire my cooking."
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "That's wonderful. I hope you find plenty of inspiration here, and maybe you can even whip up something special for us one day."


                        "What will you do if you see a shark?" if avashark == 0:
                            $ myrandom = renpy.random.randint(1,3)
                            $ avashark = 1
                            if myrandom == 1:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, I was wondering, since you're a lifeguard, do you ever have to deal with sharks here?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Well, this beach isn't known for shark encounters, but we do have protocols in place for safety. If I ever spot a shark or any potential danger, I'll make sure to alert everyone and raise the appropriate flag."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "That's good to know. Thanks for keeping us safe!"

                            if myrandom == 2:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, I've heard stories about shark sightings at beaches. Do you have a plan in case that happens here?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Absolutely. While it's rare, we do have procedures for shark sightings. If I spot one, I'll immediately sound the alarm, and we'll clear the water. Safety is our top priority."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "I'm glad to hear you're prepared for any situation. It's reassuring to know."

                            if myrandom == 3:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, I hope this doesn't happen often, but what if you spot a shark here? Do you have a system in place?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Thankfully, shark sightings are rare here, but we have a well-practiced protocol. I'll sound the alarm, raise the appropriate flag, and ensure everyone's safety."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "It's good to hear that you're well-prepared. I'll feel safer knowing you're on the lookout."


                        "What's your story?" if avastory == 0:
                            $ myrandom = renpy.random.randint(1,3)
                            $ avastory = 1
                            if myrandom == 1:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, you seem like an interesting person. What's your life story? How did you end up as a lifeguard?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Well, it's not the typical path, but I've always loved the water. I used to be a competitive swimmer, and after college, I decided to combine my passion for swimming with a desire to help others. Lifeguarding just felt like the right fit."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "That's a great way to follow your passion and make a difference."

                            if myrandom == 2:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, I'm curious about your background. How did you get into lifeguarding?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "It's actually a bit of a family tradition. My parents were lifeguards, and they instilled a deep love for the water in me. I started training young and eventually decided to make it my career."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "That's wonderful. It sounds like you come from a family of water enthusiasts."

                            if myrandom == 3:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, I'm intrigued by your choice of profession. How did you end up becoming a lifeguard?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "It's a bit of a long story, but I'll keep it short. I've always been drawn to the ocean. I studied marine biology in college and realized I wanted to protect both people and the sea. Lifeguarding was the perfect way to do that."
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "That's quite the journey. It's great to meet someone who's so dedicated to their passion and the safety of others."
                        
                        "Ask her if she agree to a beach cafe days" if rbtok == 1 and avarbtok < 1:

                            if avabossauth == 0:
                                $ avabossauth = 1
                                $ myrandom = renpy.random.randint(1,3)

                                # ————————————————————————
                                # Ava will ask permission from her boss (3×, 4 replicas each)
                                # ————————————————————————
                                if myrandom == 1:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Ava, our chef wants to run a tiny pop-up café on the weekdays—would that fly down here?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "I’m into the idea, but I’ll need the head lifeguard’s sign-off. Beach rules are strict."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Totally get it. Any chance you could bring it up after your shift?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Count on me. I’ll hunt him down before sunset and text you the verdict."

                                if myrandom == 2:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Quick thought—weekday beach café, small footprint, lots of happy sunbathers."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Sounds refreshing! Let me clear it with my supervisor first—we need to keep emergency lanes open."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Makes sense. Let me know what they say and I’ll get the permits rolling."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Will do. I’m meeting her for a patrol debrief anyway."

                                if myrandom == 3:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Could we serve cold drinks and snacks down by the south jetty on weekdays?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Love it in theory, but protocol first—I’ll pitch it to the beach manager during lunch break."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Appreciate you running interference!"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Hey, anything for good coffee on duty."

                            if avabossauth == 1:
                                $ myrandom = renpy.random.randint(1,3)

                                # ————————————————————————
                                # Ava hasn’t spoken to her boss yet (3×, 3 replicas each)
                                # ————————————————————————
                                if myrandom == 1:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Any luck tracking down your supervisor?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Not yet—the rip-current briefing ran long. I’m grabbing him first thing tomorrow."

                                if myrandom == 2:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "How did the café talk go?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Didn’t get the chance—rescues kept us slammed. It’s on my to-do list for the morning."

                                if myrandom == 3:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Just checking in on the beach-café approval."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "My boss ducked out early for a meeting downtown. I’ll corner him at roll-call at dawn."

                            if avabossauth == 2:
                                $ avarbtok = 1
                                $ myrandom = renpy.random.randint(1,3)

                                # ————————————————————————
                                # Boss gave permission – Ava agrees (3×, 5 replicas each)
                                # ————————————————————————
                                if myrandom == 1:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "So… verdict?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Green light! My boss loves community vibes and okayed weekdays 08:00-16:00."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Fantastic—we’ll keep the path clear and pack up before patrol."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Perfect. He also wants trash bins nearby, so bring extra liners."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Done. Thanks for championing this!"

                                if myrandom == 2:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Any news from HQ?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Approved! As long as we don’t block the rescue-sled lane."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "We can set tables back by the dunes—no obstruction at all."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Exactly what I told him. He’s even letting us borrow the storage shed for gear."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Sweet. First round of smoothies is on me."

                                if myrandom == 3:
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Did the big boss bite?"
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "Yup—full thumbs-up! We just need a daily clean-up log."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Easy—you’ll have a spotless shoreline."
                                    $ position = "beachavacloseexplaining"
                                    call sceneimg
                                    Ava "He also suggested we put the menu on the notice board—free promo."
                                    $ position = "beachavacloselisten"
                                    call sceneimg
                                    player "Brilliant idea. Thanks for pushing this through!"
                        
                        "I want to leave you the equipment for the cafe" if rbtok == 3:
                            $ rbtok = 4
                            $ myrandom = renpy.random.randint(1,3)
                            
                            if myrandom == 1:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Ava, can I stash the café gear in your lifeguard building? It’s closest to the set-up spot."
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Absolutely. I’ve got a dry corner by the first-aid crates—no one touches it but me."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                player "Perfect. I’ll drop the cooler and grill after shift."
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Leave the keys with me; they’ll be safer than in the restaurant storeroom."

                            if myrandom == 2:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Mind if the pop-up tent and tables live in your tower overnight?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Not at all. I’ve got room behind the rescue boards and I lock up after dusk."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                player "Great—we’ll wheel everything over on the cart."
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "I’ll keep an eye out; nothing disappears on my watch."

                            if myrandom == 3:
                                $ position = "beachavacloselisten"
                                call sceneimg
                                player "Can I park the signage and battery blender in your shack till we launch?"
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Sure thing. The storage locker’s empty—I’ll padlock it and keep the combo."
                                $ position = "beachavaclosetalk"
                                call sceneimg
                                player "Thanks! Saves us hauling it back and forth."
                                $ position = "beachavacloseexplaining"
                                call sceneimg
                                Ava "Happy to help. Your gear’s safe with the lifeguards."

                        "Start the beach cafe event" if rbtok == 4 and calendar.Hours < 19 and calendar.Hours > 8 and calendar.WeekDay != "Sat" and calendar.WeekDay != "Sun":
                            if beachcafeevents > 0:
                                $ beachcafeevents -= 1
                                jump beachcafe
                            else:
                                "You, due to the beach regulations, can have it only 4 times a month, wait for the next month"
                            



                        "Nothing for now":
                            jump culinarychoices
                    jump avabeachloop
            "Just look at the sea":
                jump beachloop
                    
                    

    else:
        $ position = "beachlifeguardempty" 
        call sceneimg
        menu:
            "Look at the sea":
                label beachloop:
                    $ calendar.AddMinutes(15)
                    $ position = "beachempty"
                    call sceneimg
                    pause
                    menu:
                        "Lay on the beach" if avafirstmeet == 2 and calendar.Hours > 6 and calendar.Hours < 19 and (calendar.WeekDay == "Sat" or calendar.WeekDay == "Sun"):
                            
                            jump weekendbeach
                        "Go home":
                            jump culinarychoices
                        "Stay":
                            jump beachloop
            "Go home":
                            jump culinarychoices
            
                
    
    

    
    

    
    

    $ position = "beachavacloseplease"
    call sceneimg
    


    
    

    
   

    
    

    
    

    
    

jump culinarychoices


