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
                    "Ask her what other interests she has?" if hayoon_randomotherinterests = False:
                        $ hayoon_randomotherinterests = True
                        $ myrandom = renpy.random.randint(1,3)
                        if myrandom == 1:
                            "She is telling here that she enjoys psychology, biology and math, especially she is thrilled with current AI state, make it in 5 replicas"
                        if myrandom == 2:
                            "She is telling here that she enjoys psychology, biology and math, especially she is thrilled with current AI state, make it in 5 replicas"
                        if myrandom == 3:
                            "She is telling here that she enjoys psychology, biology and math, especially she is thrilled with current AI state, make it in 5 replicas"
                        menu:
                            "Talk about psychology" if hayoon_psychology == False:
                                $ hayoon_psychology = True
                                $ myrandom = renpy.random.randint(1,3)
                                if myrandom == 1:
                                    "Ha-Yoon tells to the player how important is psychology in her work with different kind of patients, like metabolic patients (diabetes type 2 and obesity) and cancer patients. make it at least in 5 replicas"
                                if myrandom == 2:
                                    "Ha-Yoon tells to the player how important is psychology in her work with different kind of patients, like metabolic patients (diabetes type 2 and obesity) and cancer patients. make it at least in 5 replicas"
                                if myrandom == 3:
                                    "Ha-Yoon tells to the player how important is psychology in her work with different kind of patients, like metabolic patients (diabetes type 2 and obesity) and cancer patients. make it at least in 5 replicas"
                                
                                menu:
                                    "Tell her your aspects of using psychology" if player_customerfirst == True:
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            "Player tells her that his primary goal is a client satisfaction, it is not the same as in medicine, because in medicine client should get something to get better and it is not always satisfactory, so it makes doctor's work much harder. . make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Player tells her that his primary goal is a client satisfaction, it is not the same as in medicine, because in medicine client should get something to get better and it is not always satisfactory, so it makes doctor's work much harder. . make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Player tells her that his primary goal is a client satisfaction, it is not the same as in medicine, because in medicine client should get something to get better and it is not always satisfactory, so it makes doctor's work much harder. Ha-Yoon shares his opinion . make it at least in 5 replicas"

                                        $ reputationchange = 10
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                        
                                    "Tell her your aspects of using psychology" if player_socialaverage == True:  
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            "Player tells her that he is not good at public relations, so he prefere to stay in the kitchen and cook ,this is what he does best. make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Player tells her that his primary goal is a client satisfaction, it is not the same as in medicine, because in medicine client should get something to get better and it is not always satisfactory, so it makes doctor's work much harder. . make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Player tells her that his primary goal is a client satisfaction, it is not the same as in medicine, because in medicine client should get something to get better and it is not always satisfactory, so it makes doctor's work much harder. Ha-Yoon supports him, saying tht it is a hard work to communicate . make it at least in 5 replicas"

                                        $ reputationchange = 5
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange

                                    "Tell her your aspects of using psychology" if player_asocial == True:
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            "Player tells her that he does not like to talk to clients, he is more focused on the cooking and it is better for someone else to deal with the clients and his job is to be best cook so there would be less complaints. make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Player tells her that he does not like to talk to clients, he is more focused on the cooking and it is better for someone else to deal with the clients and his job is to be best cook so there would be less complaints. make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Player tells her that he does not like to talk to clients, he is more focused on the cooking and it is better for someone else to deal with the clients and his job is to be best cook so there would be less complaints. make it at least in 5 replicas"

                                        $ reputationchange = 3
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    
                                    "!Lie! Tell her what you think she wants to hear from you about psychology" if player_asocial == True or player_socialaverage == True:
                                        $ lied_to_hayoon_margo_knowsthetruth = 1                                        
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            "Player tells her that his work is a very complicated too and he has to deal with many kinds of problems, like talking with his boss and clients and that he need a lot of social skills to do it. make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Player tells her that his work is a very complicated too and he has to deal with many kinds of problems, like talking with his boss and clients and that he need a lot of social skills to do it. make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Player tells her that his work is a very complicated too and he has to deal with many kinds of problems, like talking with his boss and clients and that he need a lot of social skills to do it. Ha-Yoon is polite, but nothing more. Make it at least in 5 replicas"
                                        $ reputationchange = -1
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                        
                            "Talk about biology" if hayoon_biology == False:
                                $ hayoon_biology = True
                                $ myrandom = renpy.random.randint(1,3)
                                if myrandom == 1:
                                    "Ha-Yoon tells the player how important is to know bilogical and biochemical background of all the processes in the body to understand current guidelines and also to think out of the box, in areas that are not described in guideline. make it at least in 5 replicas"
                                if myrandom == 2:
                                    "Ha-Yoon tells the player how important is to know bilogical and biochemical background of all the processes in the body to understand current guidelines and also to think out of the box, in areas that are not described in guideline. make it at least in 5 replicas"
                                if myrandom == 3:
                                    "Ha-Yoon tells the player how important is to know bilogical and biochemical background of all the processes in the body to understand current guidelines and also to think out of the box, in areas that are not described in guideline. make it at least in 5 replicas"
                                menu:
                                    "Tell her she is right":
                                        if myrandom == 1:
                                            "Player just agrees with her, trying to hide that he understoon almost nothing. make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Player just agrees with her, trying to hide that he understoon almost nothing. make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Player just agrees with her, trying to hide that he understoon almost nothing. make it at least in 5 replicas"

                                        $ reputationchange = 3
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Ask her if she thinks out of the box, then she does not follow the standards?":
                                        if myrandom == 1:
                                            "player asks her if she does not follow standards with caution, Ha-Yoon appreciate it and understands what's lying beneath the question and answers that there are quite a lot of thing in medcicne that are not described in guidelines, so you have to improvise (act according to lower evidence) to make a solution for the problem. make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "player asks her if she does not follow standards with caution, Ha-Yoon appreciate it and understands what's lying beneath the question and answers that there are quite a lot of thing in medcicne that are not described in guidelines, so you have to improvise (act according to lower evidence) to make a solution for the problem. make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "player asks her if she does not follow standards with caution, Ha-Yoon appreciate it and understands what's lying beneath the question and answers that there are quite a lot of thing in medcicne that are not described in guidelines, so you have to improvise (act according to lower evidence) to make a solution for the problem. make it at least in 5 replicas"
                                        $ reputationchange = 10
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Ask her if it is punishable to treat patients non standard way?":
                                        if myrandom == 1:
                                            "Player asks it, but Ha-Yoon sees that he does this in a slight negative way, so she answers formally that doctors indeed take all the responsibility for the treatmen t if something goes wrong and knowing what she knows helps her to avoid such situations. And yes she can act as she sees best fpr the patient. The problem usually is that doctors would like to follw the guidelines, but these guidelines cover only most frequent things. But they do not cover full treatment logic, so in most cases doctors have to use all their knowledge and experience to make proper decision. make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Player asks it, but Ha-Yoon sees that he does this in a slight negative way, so she answers formally that doctors indeed take all the responsibility for the treatmen t if something goes wrong and knowing what she knows helps her to avoid such situations. And yes she can act as she sees best fpr the patient. The problem usually is that doctors would like to follw the guidelines, but these guidelines cover only most frequent things. But they do not cover full treatment logic, so in most cases doctors have to use all their knowledge and experience to make proper decision. make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Player asks it, but Ha-Yoon sees that he does this in a slight negative way, so she answers formally that doctors indeed take all the responsibility for the treatmen t if something goes wrong and knowing what she knows helps her to avoid such situations. And yes she can act as she sees best fpr the patient. The problem usually is that doctors would like to follw the guidelines, but these guidelines cover only most frequent things. But they do not cover full treatment logic, so in most cases doctors have to use all their knowledge and experience to make proper decision. make it at least in 5 replicas"
                                        $ reputationchange = 1
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Tell her you think that doctors should act according to the standards":
                                        if myrandom == 1:
                                            "In this option, player afforded himself to tell what doctors and Ha-Yoon in particular should do and she in her doctor calm manner will set him in place. she should say something like we doctors have a lot of associacions and supervision and law that may tell us what we are doing wrong. And eventhey may not have enough competence in some cases vs acting doctor with his/ her patient. So she just tells him this idea and stops this topic. make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "In this option, player afforded himself to tell what doctors and Ha-Yoon in particular should do and she in her doctor calm manner will set him in place. she should say something like we doctors have a lot of associacions and supervision and law that may tell us what we are doing wrong. And eventhey may not have enough competence in some cases vs acting doctor with his/ her patient. So she just tells him this idea and stops this topic. make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "In this option, player afforded himself to tell what doctors and Ha-Yoon in particular should do and she in her doctor calm manner will set him in place. she should say something like we doctors have a lot of associacions and supervision and law that may tell us what we are doing wrong. And eventhey may not have enough competence in some cases vs acting doctor with his/ her patient. So she just tells him this idea and stops this topic. make it at least in 5 replicas"
                                        $ reputationchange = -5
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                            
                            "Talk about AI" if hayoon_ai == False:
                                $ hayoon_ai = True
                                $ myrandom = renpy.random.randint(1,3)
                                if myrandom == 1:
                                    "Ha-Yoon tells to the player how she sees the future of AI, it could help fill all the forms faster, find best solutions for treatment, make appointments for the patients according to the plan and many more automated things. Buy it is not all. AI can also work as an AI agent do 90% of work for the doctor in initial communiaction and summarizing the request and of course, AI may treat patients or at least help them to find best ways to help while no doctor is available.  make it at least in 5 replicas"
                                if myrandom == 2:
                                    "Ha-Yoon tells to the player how she sees the future of AI, it could help fill all the forms faster, find best solutions for treatment, make appointments for the patients according to the plan and many more automated things. Buy it is not all. AI can also work as an AI agent do 90% of work for the doctor in initial communiaction and summarizing the request and of course, AI may treat patients or at least help them to find best ways to help while no doctor is available.  make it at least in 5 replicas"
                                if myrandom == 3:
                                    "Ha-Yoon tells to the player how she sees the future of AI, it could help fill all the forms faster, find best solutions for treatment, make appointments for the patients according to the plan and many more automated things. Buy it is not all. AI can also work as an AI agent do 90% of work for the doctor in initial communiaction and summarizing the request and of course, AI may treat patients or at least help them to find best ways to help while no doctor is available.  make it at least in 5 replicas"
                                menu:
                                    "So you think AI may replace the doctor?":
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            "Ha-Yoon answers that in fact it can and we may be in a new era of suffecient medicine for all people. As for the doctors, we have a vast shortage in them now 11-47 millions in different estimations, we will be in the AI industry, in quality control etc. We have a lot to improve in healthcare today and our routine keeps us from developing and making lives better for all people.  make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Ha-Yoon answers that in fact it can and we may be in a new era of suffecient medicine for all people. As for the doctors, we have a vast shortage in them now 11-47 millions in different estimations, we will be in the AI industry, in quality control etc. We have a lot to improve in healthcare today and our routine keeps us from developing and making lives better for all people.  make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Ha-Yoon answers that in fact it can and we may be in a new era of suffecient medicine for all people. As for the doctors, we have a vast shortage in them now 11-47 millions in different estimations, we will be in the AI industry, in quality control etc. We have a lot to improve in healthcare today and our routine keeps us from developing and making lives better for all people.  make it at least in 5 replicas"
                                        $ reputationchange = 10
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "Do you think we can trust AI the treatment?":
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            "Ha-Yoon tells the player that he is right and we can't fully trust AI, not because it is evil, but because it was teached on human database that contains errors and misinterpretations. So the key problem is in us. so the question in fact, can we trust us? And the answer is no, we should create a system, where we should be able to control, what is happening. Make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Ha-Yoon tells to the player how she sees the future of AI, it could help fill all the forms faster, find best solutions for treatment, make appointments for the patients according to the plan and many more automated things. Buy it is not all. AI can also work as an AI agent do 90% of work for the doctor in initial communiaction and summarizing the request and of course, AI may treat patients or at least help them to find best ways to help while no doctor is available.  make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Ha-Yoon tells to the player how she sees the future of AI, it could help fill all the forms faster, find best solutions for treatment, make appointments for the patients according to the plan and many more automated things. Buy it is not all. AI can also work as an AI agent do 90% of work for the doctor in initial communiaction and summarizing the request and of course, AI may treat patients or at least help them to find best ways to help while no doctor is available.  make it at least in 5 replicas"
                                        $ reputationchange = 5
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    "I do not believe in AI, it is just a black box with random answers":
                                        $ myrandom = renpy.random.randint(1,3)
                                        if myrandom == 1:
                                            "Ha-Yoon tells the player that he probaly have no idea how AI works, but she will tell him, that it is model of mathematics probabilities, so it is built on the math, but it is some kind of word math for LMs and she was talking about all kind of AIs. So in fact we may hot always trace the logic in AI's, but now we already have reasoning models, so I think in nearest future we will be able to trust it even better than us and to know what chain of thoughts it used, better than actual doctors.  make it at least in 5 replicas"
                                        if myrandom == 2:
                                            "Ha-Yoon tells the player that he probaly have no idea how AI works, but she will tell him, that it is model of mathematics probabilities, so it is built on the math, but it is some kind of word math for LMs and she was talking about all kind of AIs. So in fact we may hot always trace the logic in AI's, but now we already have reasoning models, so I think in nearest future we will be able to trust it even better than us and to know what chain of thoughts it used, better than actual doctors.  make it at least in 5 replicas"
                                        if myrandom == 3:
                                            "Ha-Yoon tells the player that he probaly have no idea how AI works, but she will tell him, that it is model of mathematics probabilities, so it is built on the math, but it is some kind of word math for LMs and she was talking about all kind of AIs. So in fact we may hot always trace the logic in AI's, but now we already have reasoning models, so I think in nearest future we will be able to trust it even better than us and to know what chain of thoughts it used, better than actual doctors.  make it at least in 5 replicas"
                                        $ reputationchange = -1
                                        $ nigirlimage = "nihayoon"
                                        call reputationchange
                                    
                                    
                                
                                

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




