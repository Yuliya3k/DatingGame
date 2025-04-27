label hayoonfirstmeet:
    $ position = "barhayoonwhat"
    call sceneimg
    
    
    
    # introduction
    menu:
        "How was your day?":
            $ myrandom = renpy.random.randint(1,3)


            
            if myrandom == 1:
                player "HaYoon, how was your day at the hospital today? I heard you work at the emergency department."
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "Oh, it was quite a day. You know, at the ER, you never really know what to expect.I had a if myrandom == 1:if myrandom == 2:-hour shift, and it was a rollercoaster."

                player "I can only imagine. What kind of cases did you handle?"
                $ position = "barhayoonclarifiying" 
                call sceneimg
                HaYoon "Well, it started with a car accident victim who needed immediate surgery. Then, we had a child with a high fever, and after that, a gentleman who'd injured himself in a DIY mishap.But the most unexpected one was a snakebite victim brought in by a worried hiker."

                player "A snakebite? That's not something you see every day."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Exactly. Turns out, it was a non-venomous snake, but the patient didn't know that. We had to reassure him while treating the wound.It's moments like these that make the job so unpredictable."

                player "You must have a lot of stories from your work."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Oh, definitely. Some heartwarming, some heart-wrenching. But in the end, I'm grateful I can make a difference when people need it the most."

                player "That's a remarkable attitude, HaYoon. It's clear you're passionate about what you do."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Thank you. It can be tough, but knowing I can help people during their most vulnerable moments makes it all worthwhile."


            if myrandom == 2:

                player "Hey, HaYoon, how was your day at the hospital? You work at the emergency department, right?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Oh, you know, it was one of those days. Yeah, I'm in the ER, and today felt like a rollercoaster of emotions."

                player "Really? What happened?"
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Well, it started with a car accident victim who came in with minor injuries but was terribly shaken. We had to reassure them and make sure they were okay."

                player "That sounds intense."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Yeah, but that's just the beginning. Right after that, we had a young kid with a severe allergic reaction. It was a race against time to stabilize him."

                player "That must have been stressful."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "You have no idea. And then, right when things were finally calming down, we had an elderly patient with chest pains. We had to act quickly, thinking it might be a heart attack."

                player "Your job is not easy. Dealing with all those different cases in one day takes a lot."
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "It can be challenging, but it's also incredibly rewarding. Knowing that I can make a difference, even on the toughest days, keeps me going."

                player "I have so much respect for what you do, HaYoon. It takes a special kind of person to handle all that pressure and still be there for the patients."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "Thank you. It means a lot. And hey, hearing about your day is a nice change of pace for me. How's your day been?"


            if myrandom == 3:
                player "Hey, HaYoon, how was your day at the hospital today?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Oh, it was quite a day, let me tell you. (pauses to gather her thoughts) I had a if myrandom == 1:if myrandom == 2:-hour shift at the emergency department, and it was filled with the unexpected, as usual."

                player "I can only imagine. What kind of cases did you deal with today?"
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "Well, it started with a car accident victim rushed in with severe injuries. We had to act fast and stabilize them. Then, we had an elderly gentleman who had a heart attack while gardening. It's always a race against time in those situations."

                player "That must have been intense."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "It was, but that's what we're trained for.Later, we had a young child come in with a high fever, and diagnosing the cause took some time. Turned out to be a rare viral infection."

                player "Your job can be really challenging."
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "It is, but it's also incredibly rewarding. Saving lives, helping people in their most vulnerable moments—it's what I signed up for."

                player "I admire your dedication, HaYoon. It takes a special kind of person to do what you do."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Thank you. And how about you? How's your day been so far?"

                player "Well, it hasn't been as eventful as yours, that's for sure. But I did try the Classic Cravings Burger at Crave Bites, and it was amazing."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "Sometimes, a good meal can make all the difference. If you ever need some stress relief after a hectic day, you know where to find me."

                player "I'll keep that in mind, HaYoon. Thanks for all you do."


        "How did she decide to become a doctor?" if hayoondocq == 0:
            $ myrandom = renpy.random.randint(1,3)
            $ hayoondocq = 1
            if myrandom == 1:
                player "HaYoon, I've always wondered, what made you decide to become a doctor?"
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "It's a question I get asked quite often.You know, growing up, I was always the kid who loved science. I was curious about how the human body worked, the intricacies of life, and the mysteries of medicine."

                player "Sounds like you had a passion for it from a young age."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Absolutely. But what solidified my decision was a personal experience. When I was a teenager, my younger sister fell seriously ill. We spent weeks in and out of hospitals, and I watched the doctors and nurses work tirelessly to help her recover. Their dedication and compassion left a profound impact on me."

                player "I can only imagine how that must have felt."
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "It was a challenging time, but it made me realize the difference healthcare professionals can make in people's lives. I wanted to be that person who brings hope and healing during someone's darkest hours."

                player "That's a noble reason to become a doctor."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Thank you.It hasn't been easy, but every day I'm reminded of why I chose this path. It's about making a positive impact and helping others in their time of need."

                player "Well, I have to say, the town is fortunate to have someone as dedicated as you on the medical team."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "I appreciate that. And if you ever have any health-related questions or concerns, don't hesitate to reach out. I'm here to help."

            if myrandom == 2:
                player "HaYoon, I've always been fascinated by people's journeys into their professions. How did you decide to become a doctor?"
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "Well, it wasn't a decision I made overnight. It all started when I was a child. My parents used to take me to the local clinic for regular check-ups, and I was always intrigued by the doctors and nurses there."

                player "So, it began at a young age?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Yes, but it really solidified during my high school years. I volunteered at a local hospital during my summer breaks, helping out wherever I could. The more I saw, the more I felt drawn to the medical field."

                player "That's quite an early start."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "I wanted to make a difference in people's lives, you know? There's something profoundly satisfying about being able to help someone when they're at their most vulnerable."

                player "I can imagine. It must be incredibly rewarding."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "It is, but it's also a continuous journey of learning and growth. Medical school was challenging, and the hours at the hospital can be long, but I wouldn't have it any other way."

                player "Your dedication is truly inspiring, HaYoon."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "Thank you. I believe that if you're passionate about something, the path becomes clearer, and the challenges become opportunities to become better."

                player "That's a great perspective to have. Thanks for sharing your journey with me, HaYoon."

            if myrandom == 3:
                player " HaYoon, I've always wondered, how did you decide to become a doctor?"
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "It's a question I get asked often.Well, it all started when I was a kid. My mother used to work as a nurse at our local hospital, and I would sometimes visit her after school. I was fascinated by the medical environment, all the machines, and the way the doctors and nurses helped people."

                player "So, it was a childhood fascination?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Yes, but it grew into something more. As I got older, I realized that I genuinely enjoyed science and the idea of using it to make a positive impact on people's lives. Plus, my mom's dedication to her job was inspiring."

                player "It sounds like you had a strong role model."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "I did. My mom always encouraged me to pursue my passions and dream big. She believed in me, and I wanted to make her proud."

                player "I'm sure you've done just that. You're making a real difference in the world."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Thank you. It's been a challenging journey, but I wouldn't trade it for anything. Helping people in their time of need, there's nothing quite like it."

                player "Well, I'm glad you followed your passion. We're lucky to have you in town."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "I'm lucky to be here. And who knows, maybe one day, I'll be able to help you too, even if it's just with some medical advice."



        "What do you do except your work?" if hayoonsparetime == 0:
            $ myrandom = renpy.random.randint(1,3)
            $ hayoonsparetime = 1
            if myrandom == 1:
                player " HaYoon, it's great to see you outside of work. What do you usually like to do when you're not at the hospital?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Oh, it's nice to unwind after those long shifts. I try to make the most of my free time. You'll often find me at the local park, taking in some fresh air, or just enjoying a good book."
                $ hayoonpark = 1
                player "That sounds relaxing. Do you have any favorite books or genres?"
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "I'm quite the bookworm, to be honest. I enjoy everything from classic literature to contemporary fiction. Lately, I've been into medical thrillers; they add a bit of excitement to my downtime."
                $ hayoonreading = 1
                player "A doctor who loves medical thrillers, that's intriguing. Anything else you like to do?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Well, I also like volunteering when I can. There's a local shelter nearby, and I occasionally help out there. It's a way to give back to the community and connect with people in a different setting."
                $ hayoonshelter = 1
                player "That's really admirable. It's clear that you have a passion for helping others, both in your profession and outside of it."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Thank you. I believe it's important to make a positive impact wherever we can, whether it's through medicine or a lending hand."

                player "I couldn't agree more. It's been great getting to know you better, HaYoon."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "Likewise. If you ever want to join me for a walk in the park or borrow a good book, just let me know."


            if myrandom == 2:
                player " HaYoon, it's great seeing you outside of work. What do you like to do in your free time?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Oh, I cherish my free time. After those long shifts, I love unwinding and doing something completely different. I'm a bit of a foodie, so I enjoy exploring new restaurants and cafes around town."

                player "That sounds like a delicious hobby."
                $ position = "barhayoonlecturing" 
                call sceneimg
                HaYoon "It is! There are so many hidden gems in this town when it comes to food. And beyond that, I enjoy hiking in the nearby trails and practicing yoga. It helps me relax and stay balanced."
                $ position = "barhayoonexplaining"
                call sceneimg
                player "Hiking and yoga, that's a great way to stay active and de-stress."
                $ hayoonpark = 1
                $ hayoonhiking = 1
                HaYoon "It definitely helps clear my mind after intense shifts at the hospital. Plus, the fresh air and nature are so rejuvenating."

                player "Have you found any favorite hiking spots around here?"
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Oh, yes! There's a beautiful trail in the nearby woods with a stunning view at the end. It's like a little slice of paradise. If you're ever interested, I'd be happy to show you sometime."

                player "I might take you up on that offer. It sounds like a fantastic way to spend a day. Thanks for sharing, HaYoon."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "My pleasure. It's always nice to chat with someone who's genuinely interested."


            if myrandom == 3:
                player " HaYoon, it's always interesting to see you outside of the hospital. What do you like to do when you're not at work?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Oh, I try to make the most of my free time.I love reading, especially medical journals and research papers. It helps me stay updated on the latest advancements in the field. But I also enjoy some more relaxing activities like gardening. It's therapeutic, you know?"

                player "That's quite the contrast – medical literature and gardening. How do you find the time for both?"
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Well, it's all about balance. Reading keeps my mind engaged, and gardening provides a nice change of pace. Plus, it allows me to be closer to nature, which I find calming. And on the weekends, I often volunteer at a local animal shelter."
                $ hayoonreading = 1
                $ hayoongardening = 1

                player "That's really admirable. You have such a wide range of interests."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Thank you. It's important to have a well-rounded life, don't you think?"

                player "Absolutely. It keeps things interesting and fulfilling."
                $ position = "barhayoonhey"
                call sceneimg
                HaYoon "I couldn't agree more. How about you? What do you like to do in your free time?"



        "Why are you visiting the bar?" if hayoonbarq == 0:
            $ hayoonbarq = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                player " HaYoon, I've noticed you sometimes come to this bar after work. Is there a particular reason why you like it here?"
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Well, it's partly about winding down after a long shift. The atmosphere here is relaxing, and it's a great place to decompress. But there's another reason too. Kira, the bartender, is a friend of mine. We've known each other for years."

                player "That's nice. It must be comforting to have a familiar face to chat with."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Absolutely. Sometimes, it's good to step away from the hospital environment and have a casual conversation with friends. Plus, Kira makes fantastic drinks, which doesn't hurt."
                $ hayoonkirafriends = 1
                player "I can't argue with that. Her drinks are indeed top-notch."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "So, do you come here often?"

                player "Not as often as I'd like. I'm still getting to know the town and its people, but I'm starting to feel more at home."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "That's great to hear. If you ever want to meet more people around here, just let me know. I can introduce you to some wonderful folks."

                player "Thanks, HaYoon. I might take you up on that offer."

            if myrandom == 2:
                player " HaYoon, I've noticed you come to this bar every now and then. What brings you here?"
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Well, it's a nice place to unwind after a long shift at the hospital. Sometimes, you just need a change of scenery and some good company, you know?"

                player "I can imagine the hospital can be quite intense. Do you ever find interesting people or stories here?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Absolutely! That's one of the things I enjoy about this place. You get to meet all sorts of people, each with their own unique stories. It's a nice reminder that there's a whole world outside the hospital walls."

                player "Have you made any close friends here at the bar?"
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Well, not close friends, but definitely some acquaintances. It's nice to have a few familiar faces to chat with and share a drink. And who knows, maybe you'll become one of them."
                $ position = "barhayoonhey"
                call sceneimg
                player "I'd like that. It's always good to have a friendly face around."

            if myrandom == 3:
                player " HaYoon, I've noticed you come to this bar sometimes after work. What brings you here?"
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Ah, well, it's a nice way to unwind after a long shift at the hospital. You know, a change of scenery and all that."

                player "I can imagine working at the emergency department can be really intense. Do you find relaxation in the bar's atmosphere?"
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Absolutely. The bar offers a different kind of ambiance. It's quieter, and I can just sit here, have a drink, and collect my thoughts. Plus, the company is usually pleasant."

                player "Speaking of company, I've been enjoying our conversation. It's been nice getting to know you."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "Likewise. I appreciate the company too. It's a welcome break from the hectic hospital routine."

                player "Well, if you ever need someone to talk to or share a drink with, you know where to find me."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "That's very kind of you. I'll keep that in mind. Thanks."

        "Do you want a drink?":
            
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "barhayoonlecturing"
                call sceneimg
                player " HaYoon, can I get you a drink? It's on me."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "That's really sweet of you, but I've got it covered, don't worry. I appreciate the offer, though."

                player "Alright, no problem. Just thought I'd ask. If you change your mind or want anything, feel free to let me know."
                $ position = "barhayoonhey"
                call sceneimg
                HaYoon "Thanks. I'll definitely keep that in mind. It's nice to know you're looking out for me."


            if myrandom == 2:
                $ position = "barhayoonlecturing"
                call sceneimg
                player " HaYoon, can I get you another drink?"
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Thanks for the offer, but I've got it covered. I like to take care of my own tab."

                player "Of course, HaYoon. Just wanted to make sure you were comfortable."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "I appreciate that. It's sweet of you to offer."

            if myrandom == 3:
                $ position = "barhayoonlecturing"
                call sceneimg
                player " HaYoon, can I get you another drink? It's on me."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "Thanks, but I can manage myself. I appreciate the offer, though."

                player "Alright, just let me know if you change your mind. I'm here to help."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "Will do. You're very kind. I enjoy our conversations."

        "What's your story, [name]?" if hayoonplayerstory == 1:
            $ hayoonplayerstory = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon " So, I've been sharing bits of my life with you. What about you? What do you do for a living?"

                player "Well, I'm actually a cook. Just moved to this town recently and started working at a local restaurant."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "A cook, huh? That sounds exciting. What kind of cuisine do you specialize in?"

                player "I love experimenting with different cuisines, but I'd say I'm pretty versatile. From Italian to Asian to classic American, I enjoy creating a variety of dishes."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "That's impressive. It must be fascinating to work with food every day."

                player "It definitely has its moments. I enjoy the creativity that comes with it, and the satisfaction of seeing people enjoy what I cook."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "It sounds like you're passionate about your work. I admire that. Cooking is an art, too, in its own way."

                player "Thanks, HaYoon. It's been great talking to you about it."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon "Likewise. I'm always here if you want to chat or need medical advice for your culinary adventures."

                player "I'll keep that in mind. Thanks for the offer, HaYoon."


            if myrandom == 2:
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon " So, I've shared quite a bit about my life. Tell me, what do you do for a living? What brought you to this town?"

                player "Well, I'm a cook, and I recently moved here looking for new opportunities. I thought this town had a lot to offer, and so far, it hasn't disappointed."
                $ position = "barhayoonclarifiying"
                call sceneimg
                HaYoon "That's intriguing. Cooking can be such a creative and fulfilling profession. Have you found work at a restaurant in town?"

                player "Yes, I've joined a local restaurant as their cook. It's been a great experience so far, and I'm enjoying every moment of it."
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon "That's wonderful to hear. I'm sure the town will appreciate your culinary skills. And it's always nice to have a variety of dining options. What's your specialty?"

                player "I love experimenting with flavors, but if I had to pick one, I'd say I'm known for my pasta dishes. There's something magical about creating the perfect pasta and sauce combination."
                $ position = "barhayoonclarifiying"
                call sceneimg


                HaYoon "Pasta is a favorite for many. I'll have to try your creations sometime. It's been great getting to know you."
                $ position = "barhayoonhey"
                call sceneimg

                player "Likewise, HaYoon. If you ever have a hankering for pasta or just want to chat, you know where to find me."

            if myrandom == 3:
                $ position = "barhayoonexplaining"
                call sceneimg
                HaYoon " So, tell me about yourself. What do you do for a living?"

                player "Well, I'm a cook, actually. I recently moved to this town and started working at a local restaurant."
                $ position = "barhayoonclarifiying"
                call sceneimg

                HaYoon "That sounds interesting. What kind of cuisine do you specialize in?"

                player " I love experimenting with different styles, but I'd say I have a passion for comfort food. You know, dishes that warm the soul."
                $ position = "barhayoonexplaining"
                call sceneimg

                HaYoon "Comfort food has a special place in everyone's heart. It's amazing how a meal can bring back memories and make you feel at home."

                player " Exactly! Food has this unique power to connect people, just like how we're connected here, chatting at the bar."

                HaYoon "That's true. And it's always great to meet new people in town. I hope you're enjoying your time here."
                $ position = "barhayoonhey"
                call sceneimg

                player " Thanks, HaYoon. It's been quite an adventure so far, and I'm looking forward to more."

        "See you next time!":
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                player " Well, HaYoon, it's been a pleasure chatting with you tonight."

                HaYoon " Likewise. Thanks for the company."

                player " Anytime. If you ever want to hang out again or need someone to listen after a tough day at the hospital, just swing by the bar. I'll be here."
                $ position = "barhayoonexplaining"
                call sceneimg

                HaYoon "That's a tempting offer. I might take you up on that sometime."

                player "I'll be looking forward to it. Take care, HaYoon, and have a great night."
                $ position = "barhayoonhey"
                call sceneimg

                HaYoon " You too. Goodnight!"
                
            if myrandom == 2:
                player " Well, HaYoon, it's been a pleasure getting to know you tonight. I hope you have a fantastic evening ahead."
                $ position = "barhayoonexplaining"
                call sceneimg

                HaYoon "Thank you. I had a wonderful time chatting with you. Don't be a stranger; you're always welcome at the bar."

                player " I'll keep that in mind. Take care, HaYoon, and have a great night."

                HaYoon " You too. Goodbye, and see you around!"

            if myrandom == 3:
                player " Well, HaYoon, it's been a pleasure getting to know you. I hope we can chat like this again soon."
                $ position = "barhayoonexplaining"
                call sceneimg

                HaYoon " Likewise. Don't be a stranger; I'll be here at the bar from time to time. Have a wonderful evening."
                $ position = "barhayoonhey"
                call sceneimg

                player " You too, HaYoon. Take care, and I'll see you around."
            jump bar3

jump hayoonfirstmeet