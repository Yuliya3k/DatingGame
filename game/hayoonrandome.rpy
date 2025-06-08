label hayoonrandome:    
    $ hayoonrandome = 1
    $ hayoonmettoday = True
    $ position = "randomencounterhayoon"
    call sceneimg 
    "You can see Ha-Yoon sitting and reading the book. What will you do?"
    $ position = "randomencounterhayoonclose"
    call sceneimg 
    menu:
        "Come and say hello!":
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                

                player "Ha-Yoon! It's a surprise to see you here, engrossed in a book. What are you reading?"
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 
                HaYoon "Oh, hello! I'm just taking a break with some light reading. It's a book on herbal remedies. How have you been?"
                $ position = "randomencounterhayooncloselisten"
                call sceneimg 
                player "That's interesting! I'm doing well, thanks. Keeping busy with culinary experiments. Always trying to blend taste and health."
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 

                HaYoon "That sounds quite like a culinary adventure. Maybe your dishes could complement some of the natural remedies I study."
                $ position = "randomencounterhayooncloselisten"
                call sceneimg 

                player "Absolutely! Perhaps we could exchange ideas over coffee sometime. I’d love to learn more about your work."
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 

                HaYoon "I'd enjoy that. It’s always good to discuss health and nutrition. Let’s make a plan soon."
            if myrandom == 2:

                player "Ha-Yoon! What a pleasant surprise. That looks like an interesting book. What are you reading?"
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 

                HaYoon "Hi there! Just unwinding with a book on holistic health. It's good to step away from the clinic. How are things with you?"
                $ position = "randomencounterhayooncloselisten"
                call sceneimg 

                player "All good on my end. I’ve been exploring healthy recipes in the kitchen, trying to find that perfect balance."
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 

                HaYoon "Your passion for cooking must be quite the journey. I'm always interested in the intersection of food and health."
                $ position = "randomencounterhayooncloselisten"
                call sceneimg 

                player "Maybe I can share some of my latest creations with you. Could be beneficial for your health practice."
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 

                HaYoon "That sounds wonderful. Combining our expertise could lead to some great insights. Let's meet up soon."
            if myrandom == 3:

                player "Hey, Ha-Yoon! Fancy meeting you here. What's caught your interest in that book?"
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 

                HaYoon "Hello! Just taking some time for myself with a book on nutrition and wellness. It's quite fascinating. How are you?"
                $ position = "randomencounterhayooncloselisten"
                call sceneimg 

                player "I’m great, thanks. Been busy in the kitchen, experimenting with nutritious meals. It's quite the culinary challenge."
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 

                HaYoon "That's impressive. There’s so much to explore in the realm of nutritional cooking. It’s essential for health."
                $ position = "randomencounterhayooncloselisten"
                call sceneimg 

                player "I agree. It would be great to get your thoughts on some of my dishes. Maybe we could collaborate on something."
                $ position = "randomencounterhayoonclosetalk"
                call sceneimg 

                HaYoon "I’d love that. It’s important to have a holistic approach to health. Let’s set up a time to discuss this further."

            label hayoonrandomencounterdialogueloop:
                menu:
                    "Give her some food" if hayoon_randomgivefood == False and hayoon_attitude > 10 and (water_bottle >= 1 or iced_tea >= 1 or smoothie_drink >= 1):
                        $ hayoon_randomgivefood = True
                        $ position = "randomencounterhayooncloselisten"
                        call sceneimg
                        player "I brought a few snacks along. Want something while you read?"
                        $ position = "randomencounterhayoonclosetalk"
                        call sceneimg
                        HaYoon "That's thoughtful. I'd love a quick bite."
                        menu:
                            "Water" if water_bottle >= 1:
                                $ position = "randomencounterhayoonclosetalk"
                                call sceneimg
                                player "Here, have a bottle of water."
                                $ water_bottle -= 1
                                $ fullnesschange = 250
                                $ nigirlimage = "nihayoon"
                                call fullnesschange
                                pause 0.5
                                $ calorieschange = 0
                                $ nigirlimage = "nihayoon"
                                call calorieschange
                                $ position = "randomencounterhayooncloselisten"
                                call sceneimg
                                HaYoon "Thanks, that hits the spot."
                            "Iced Tea" if iced_tea >= 1:
                                $ position = "randomencounterhayoonclosetalk"
                                call sceneimg
                                player "Maybe some iced tea?"
                                $ iced_tea -= 1
                                $ fullnesschange = 300
                                $ nigirlimage = "nihayoon"
                                call fullnesschange
                                pause 0.5
                                $ calorieschange = 100
                                $ nigirlimage = "nihayoon"
                                call calorieschange
                                $ position = "randomencounterhayooncloselisten"
                                call sceneimg
                                HaYoon "Nice and refreshing, thank you."
                            "Smoothie" if smoothie_drink >= 1:
                                $ position = "randomencounterhayoonclosetalk"
                                call sceneimg
                                player "How about a smoothie?"
                                $ smoothie_drink -= 1
                                $ fullnesschange = 400
                                $ nigirlimage = "nihayoon"
                                call fullnesschange
                                pause 0.5
                                $ calorieschange = 200
                                $ nigirlimage = "nihayoon"
                                call calorieschange
                                $ position = "randomencounterhayooncloselisten"
                                call sceneimg
                                HaYoon "Delicious! Thanks."
                        $ reputationchange = 3
                        $ nigirlimage = "nihayoon"
                        call reputationchange
                    "Ask if she usually reads here?" if hayoon_randomreadhere == False:
                        $ hayoon_randomreadhere = True
                        $ myrandom = renpy.random.randint(1,3)
                        if myrandom == 1:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "I didn't expect to see you here with a book. Do you come here often to read?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Yes, actually. Whenever I'm not on shift at the hospital, I find this place perfect for some daytime reading. It's my little escape."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "That sounds like a great way to unwind. It must be a nice change from the busy hospital environment."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Absolutely, it's important to find these peaceful moments. It helps to balance the intensity of my work."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "I can imagine. It's great that you've found a spot where you can relax and enjoy your books."
                        if myrandom == 2:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "You seem quite absorbed in your book. Is this your regular spot for reading?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Yes, it is. On days when I'm not at the hospital, I like to spend my time here, reading. It's peaceful and rejuvenating."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "That's a nice routine. It must be quite a contrast from your work at the hospital."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "It really is. These moments of tranquility are essential for me to recharge and stay focused."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "Well, it's great to see you making time for yourself like this. Enjoy your reading!"
                        if myrandom == 3:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "Catching you here with a book is a pleasant surprise. Do you often read here during the day?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "I do, actually. When I'm not working at the hospital, this is my go-to place. It's quiet and perfect for reading."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "That must be a nice break from the demands of being a doctor."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Indeed, it is. A bit of reading in a calm environment really helps me maintain my balance."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "Sounds like a perfect way to spend your free time. I hope your book is as enjoyable as this place seems to be."

                    "What's your books of choice?" if hayoon_randombookschoice == False:
                        $ hayoon_randombookschoice = True
                        $ myrandom = renpy.random.randint(1,3)
                        if myrandom == 1:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "I'm curious, Ha-Yoon, what kind of books do you usually read here?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Well, when I'm not at the hospital, I like to read books related to my field – mostly medical journals and publications on new health trends. It keeps me updated and inspired."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "That's dedication! It must be fascinating to keep up with all the latest developments in medicine."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "It is! I love learning about new research and findings. It helps me in my practice and to advise my patients better."
                        if myrandom == 2:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "What type of books do you find yourself drawn to when you're here?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "I usually use this time away from the hospital to catch up on a variety of subjects. I enjoy reading about wellness, nutrition, and sometimes a bit of fiction to unwind."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "That sounds like a well-rounded selection. It's great that you have such diverse interests."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Yes, I find that a mix of professional and leisure reading keeps me balanced. It's my way of staying informed and entertained."
                        if myrandom == 3:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "You seem quite invested in your reading. What genres do you typically enjoy here?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "On days when I'm not working at the hospital, I prefer reading about mindfulness and holistic health. It complements my medical background and helps me relax."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "Mindfulness is such an important aspect of health. It's impressive how you integrate it into your reading."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "I believe in treating both the mind and body. These books offer me insights and techniques that I can apply both personally and professionally."
                    "Ask her what other interests she has?":
                        
                        $ myrandom = renpy.random.randint(1,3)
                        if myrandom == 1:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg

                            player "Aside from reading, what other subjects fascinate you, Ha-Yoon?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg

                            HaYoon "I have a deep love for psychology, biology, and mathematics. Right now I'm especially excited about how fast artificial intelligence is advancing."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg

                            player "AI is moving quickly indeed. Do you keep up with the latest developments?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg

                            HaYoon "Whenever I can. The intersection of tech and medicine is fascinating. It feels like every month there's some new breakthrough."
                        if myrandom == 2:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg

                            player "Do you have any hobbies outside of medicine and reading?"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg

                            HaYoon "Definitely. I'm quite interested in psychology and biology. Lately I'm captivated by how AI might change our daily routines."
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg

                            player "That does sound intriguing."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg

                            HaYoon "It is. Math ties it all together for me—it helps explain the patterns behind everything." 
                        if myrandom == 3:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg

                            player "I'd love to know more about your interests when you're not at the hospital."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg

                            HaYoon "Well, I'm fascinated by psychology and biology, and I'm a bit of a math nerd. Recently I've been following the developments in AI quite closely." 
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg

                            player "No wonder you're always so knowledgeable. AI does open many doors."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg

                            HaYoon "Exactly. It's thrilling to imagine how these fields will converge in the near future."
                        label hayoonotherintertestsloop:
                        menu:
                            "Talk about psychology" if hayoon_psychology == False:
                                $ hayoon_psychology = True
                                $ myrandom = renpy.random.randint(1,3)
                                if myrandom == 1:
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Psychology is crucial in my work. With metabolic patients or those facing cancer, understanding their mindset can make treatments far more effective."
                                    $ position = "randomencounterhayooncloselisten"
                                    call sceneimg

                                    player "So you tailor your approach depending on how they respond emotionally?"
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Exactly. It guides how I speak with them and what support I offer."
                                if myrandom == 2:
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Mental state plays a huge role for my diabetic and obese patients. Encouragement and empathy help them adopt healthier habits."
                                    $ position = "randomencounterhayooncloselisten"
                                    call sceneimg

                                    player "That makes sense. A little motivation can go a long way."
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Right, and with cancer cases it's often even more important because stress can affect recovery." 
                                if myrandom == 3:
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Over the years I've seen how understanding psychology helps connect with patients, especially those facing long-term illnesses." 
                                    $ position = "randomencounterhayooncloselisten"
                                    call sceneimg

                                    player "It's impressive how you integrate that knowledge." 
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Thank you. It definitely improves outcomes." 

                                menu:
                                    "Tell her your aspects of using psychology" if player_customerfirst == True:
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            player "In my work customer satisfaction is everything. Unlike medicine where treatment can be uncomfortable, I focus on making diners happy." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "I imagine that contrast can be challenging." 
                                            $ position = "randomencounterhayooncloselisten"
                                            call sceneimg

                                            player "It is, but it also pushes me to understand people better." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "That perspective would certainly help in any field." 
                                        if myrandom == 2 or myrandom == 3:
                                            player "Satisfying customers is my priority. Sometimes it's easier than what you face in medicine, since diners usually leave happy." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "Still, it sounds like a lot of pressure." 
                                            $ position = "randomencounterhayooncloselisten"
                                            call sceneimg

                                            player "It can be, but good feedback makes it worthwhile." 

                                        $ reputationchange = 10
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Tell her your aspects of using psychology" if player_socialaverage == True:
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            player "Honestly I'm better off in the kitchen than chatting with customers. Cooking is what I do best." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "Sticking to strengths is smart." 
                                            $ position = "randomencounterhayooncloselisten"
                                            call sceneimg

                                            player "Exactly. I let others handle most of the PR." 
                                        if myrandom == 2 or myrandom == 3:
                                            player "Customer satisfaction is still my goal, though medicine seems tougher since patients might resist what's good for them." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "True, sometimes we have to deliver hard news." 

                                        $ reputationchange = 5
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Tell her your aspects of using psychology" if player_asocial == True:
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                            player "I tend to avoid talking to customers altogether and focus purely on cooking. If the food is great, complaints are fewer." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "I understand. Everyone plays to their strengths." 

                                        $ reputationchange = 3
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "!Lie! Tell her what you think she wants to hear from you about psychology" if player_asocial == True or player_socialaverage == True:
                                        $ lied_to_hayoon_margo_knowsthetruth = 1
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                            player "My job involves constant conversation with clients and management, so I rely heavily on social skills." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "That's good to hear." 

                                        $ reputationchange = -1
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                jump hayoonotherintertestsloop
                            "Talk about biology" if hayoon_biology == False:
                                $ hayoon_biology = True
                                $ myrandom = renpy.random.randint(1,3)
                                if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Knowing the biochemical background helps me understand guidelines and also improvise when cases don't fit neatly." 
                                    $ position = "randomencounterhayooncloselisten"
                                    call sceneimg

                                    player "So it gives you confidence to act even without direct instructions?" 
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Exactly. A strong foundation lets me think outside the box." 
                                menu:
                                    "Tell her she is right":
                                        if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                            player "You're absolutely right." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "I'm glad you agree." 

                                        $ reputationchange = 3
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Ask her if she thinks out of the box, then she does not follow the standards?":
                                        if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                            player "If you improvise, does that mean ignoring standards sometimes?" 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "Not at all. Guidelines cover common cases, but unique situations require judgment based on everything we know." 

                                        $ reputationchange = 10
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Ask her if it is punishable to treat patients non standard way?":
                                        if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                            player "Is there a risk of punishment if you treat patients differently from the guidelines?" 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "Doctors take responsibility for every decision. The rules can't cover everything, so we rely on expertise." 

                                        $ reputationchange = 1
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Tell her you think that doctors should act according to the standards":
                                        if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                            player "I think doctors should always stick strictly to the guidelines." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "We are monitored closely already. Sometimes creativity is needed to truly help a patient." 

                                        $ reputationchange = -5
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                jump hayoonotherintertestsloop
                            
                            "Talk about AI" if hayoon_ai == False:
                                $ hayoon_ai = True
                                $ myrandom = renpy.random.randint(1,3)
                                if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "AI could streamline paperwork, suggest treatments, even handle early patient conversations. It's an exciting tool." 
                                    $ position = "randomencounterhayooncloselisten"
                                    call sceneimg

                                    player "Do you think AI might replace doctors someday?" 
                                    $ position = "randomencounterhayoonclosetalk"
                                    call sceneimg

                                    HaYoon "Possibly for routine care. There aren't enough doctors worldwide, so AI could fill gaps while we focus on complex cases." 
                                    $ reputationchange = 10
                                    $ nigirlimage = "nihayoon"
                                    call reputationchange
                                menu:
                                    "Do you think we can trust AI the treatment?":
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                            player "Is it really safe to trust AI with treatment decisions?" 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "It's only as good as the data we train it on. We need oversight, but it could become very reliable." 

                                        $ reputationchange = 5
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "I do not believe in AI, it is just a black box with random answers":
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1 or myrandom == 2 or myrandom == 3:
                                            player "I'm skeptical of AI—it feels like a black box producing random answers." 
                                            $ position = "randomencounterhayoonclosetalk"
                                            call sceneimg

                                            HaYoon "It's actually built on mathematical probabilities. Soon we'll be able to trace its reasoning even better than we do with human doctors." 

                                        $ reputationchange = -1
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                
                                jump hayoonotherintertestsloop    

                            "Nothing":
                                jump hayoonrandomencounterdialogueloop        
                                
                        jump hayoonrandomencounterdialogueloop         

                    "I need to go":
                        $ myrandom = renpy.random.randint(1,3)
                        if myrandom == 1:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 
                            player "It was really nice running into you, Ha-Yoon. I should let you get back to your book. Take care!"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Yes, it was lovely to see you too. Thanks for the chat. Enjoy the rest of your day!"
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "You too. Hope to catch up again soon under less serendipitous circumstances!"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Definitely. Have a great day, and see you around!"
                        if myrandom == 2:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "Well, Ha-Yoon, I won't keep you from your reading any longer. It was great seeing you."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Great seeing you too. Thanks for stopping by to say hello. Have a wonderful day!"
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "You too, Ha-Yoon. Maybe next time we can grab a coffee together."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "I'd like that. Take care and see you soon!"
                        if myrandom == 3:
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "I'll let you get back to your reading, Ha-Yoon. Always a pleasure to catch up. Have a good read!"
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "Thank you, it was nice talking to you as well. Enjoy your day and take care!"
                            $ position = "randomencounterhayooncloselisten"
                            call sceneimg 

                            player "Thanks, and maybe we can plan a proper meet-up sometime soon."
                            $ position = "randomencounterhayoonclosetalk"
                            call sceneimg 

                            HaYoon "That sounds lovely. Looking forward to it. Goodbye for now!"

                        jump rm
                jump hayoonrandomencounterdialogueloop
        "Just go":
            
            return

    
"something went wrong"
return




