label linpark:

    if lin_attitude > 9:
        #meeting
        if linseen == 0:
            $ linseen = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "parklinrunning"
                call sceneimg
                "You see Lin, who has just finished her training, and she notices you, ready to engage in conversation"
                
                $ position = "parklintalkhi"
                call sceneimg
                Lin "Morning! Just wrapping up my workout. How's your day starting?"
                $ position = "parklintalklisten"
                call sceneimg

                player "Morning! It's starting great, especially with this beautiful view. Your training looks intense. HIIT, right?"
                $ position = "parklintalktalk"
                call sceneimg

                Lin "You got it! Keeps me on my toes. So, what brings you out here this morning?"
                $ position = "parklintalklisten"
                call sceneimg

                player "Oh, just enjoying the fresh air and the sunrise. Mind if I join you for a chat now that you're done?"
                $ position = "parklintalktalk"
                call sceneimg

                Lin "Not at all! I could use a good chat after all that. Let's catch up!"

                

            if myrandom == 2:
                $ position = "parklinrunning"
                call sceneimg
                "You see Lin, who has just finished her training, and she notices you, ready to engage in conversation."
                
                $ position = "parklintalkhi"
                call sceneimg

                Lin "Morning! Just wrapping up my workout. How's your day starting?"
                $ position = "parklintalklisten"
                call sceneimg

                player "Morning! It's starting great, especially with this beautiful view. Your training looks intense. HIIT, right?"
                $ position = "parklintalktalk"
                call sceneimg

                Lin "You got it! Keeps me on my toes. So, what brings you out here this morning?"
                $ position = "parklintalklisten"
                call sceneimg

                player "Oh, just enjoying the fresh air and the sunrise. Mind if I join you for a chat now that you're done?"
                $ position = "parklintalktalk"
                call sceneimg

                Lin "Not at all! I could use a good chat after all that. Let's catch up!"


            if myrandom == 3:
                $ position = "parklinrunning"
                call sceneimg
                "You see Lin, who has just finished her training, and she notices you, ready to engage in conversation."
                
                $ position = "parklintalkhi"
                call sceneimg

                Lin "Morning! Just wrapping up my workout. How's your day starting?"
                $ position = "parklintalklisten"
                call sceneimg

                player "Morning! It's starting great, especially with this beautiful view. Your training looks intense. HIIT, right?"
                $ position = "parklintalktalk"
                call sceneimg

                Lin "You got it! Keeps me on my toes. So, what brings you out here this morning?"
                $ position = "parklintalklisten"
                call sceneimg

                player "Oh, just enjoying the fresh air and the sunrise. Mind if I join you for a chat now that you're done?"
                $ position = "parklintalktalk"
                call sceneimg

                Lin "Not at all! I could use a good chat after all that. Let's catch up!"

        menu:
            "Do you train daily?" if lintrain == 0:
                $ lintrain = 1
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Do you do this kind of training every day?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "Yep, pretty much. I like to stay consistent. Plus, I need to be an example for my clients at the fitness club."
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "That's dedication right there. I can see why you're so good at what you do. How do you find the energy for it every day?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "It's all about motivation and discipline. Plus, the results are worth it. You're a regular at the fitness club, so you know what I mean!"

                if myrandom == 2:
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Do you do this kind of training every day?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "Yep, pretty much. I like to stay consistent. Plus, I need to be an example for my clients at the fitness club."
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "I get it. Consistency is key when it comes to fitness. I've been going to the fitness club regularly too, and it's been a game-changer for me."

                if myrandom == 3:
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Do you do this kind of training every day?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "Yep, pretty much. I like to stay consistent. Plus, I need to be an example for my clients at the fitness club."
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "I totally understand the importance of consistency. I've been a regular at the fitness club for a while now, and it's made a big difference in my life. It's great to see you're so dedicated to it too."

            "Make a compliment" if lincompliment == 0:
                $ lincompliment = 1
                
                menu:
                    "Compliment her as a professional":
                        $ myrandom = renpy.random.randint(1,10)
                        $ reputationchange = 1
                        $ nigirlimage = "nilin"
                        call reputationchange
                        if myrandom == 1:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " Lin, you're incredibly dedicated to your fitness routine, and it really shows. Your hard work is inspiring."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " Thank you so much. I believe in leading by example, and it's wonderful to hear that it's motivating for you."
                        if myrandom == 2:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " I have to say, Lin, your energy and passion for what you do are truly admirable. You motivate me to push harder at the fitness club."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " Your words mean a lot to me. Helping others achieve their fitness goals is what drives me, and I'm glad it shows."
                        if myrandom == 3:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " You're not just a great fitness trainer, Lin, but also a fantastic role model. Your commitment to a healthy lifestyle is impressive."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " That's very kind of you to say. I'm passionate about living a healthy life, and I'm thrilled that it inspires you."
                        if myrandom == 4:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " Your expertise and guidance at the fitness club have been invaluable to me. I appreciate all the support you provide."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " I'm here to support you every step of the way. Your progress is a testament to your hard work and dedication."
                        if myrandom == 5:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " Lin, I've seen real progress in my fitness journey thanks to your training. Your knowledge and encouragement make all the difference."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " It's been a pleasure working with you. Seeing your improvement is incredibly rewarding for me as a trainer."
                        if myrandom == 6:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " It's clear that you're not just in it for the job, Lin. You genuinely care about helping people achieve their fitness goals, and that's special."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " Thank you. Making a positive impact on my clients' lives is what keeps me going in this profession."
                        if myrandom == 7:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " Lin, your positive attitude and determination are contagious. You make every workout session enjoyable and effective."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " I'm delighted to hear that you enjoy our sessions. Let's keep up the good work together!"
                        if myrandom == 8:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " I can't thank you enough, Lin, for your dedication to improving the lives of your clients. You're a true asset to the fitness club."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " Your appreciation means a lot. I'll continue to give my best to help everyone reach their fitness goals."
                        if myrandom == 9:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " Your commitment to personal fitness is impressive, Lin. It's clear that you practice what you preach, and that's commendable."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " Leading a healthy lifestyle is essential to me. I'm glad you notice and appreciate it."
                        if myrandom == 10:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player " Lin, you're not just a trainer; you're a mentor. Your guidance has had a significant impact on my fitness journey, and I'm grateful for that."
                            $ position = "parklintalktalk"
                            call sceneimg
                            Lin " I'm honored to be a part of your fitness journey. Your progress is a reflection of your dedication and hard work. Keep it up!" 
                        

                    "Compliment her appearence":
                        $ myrandom = renpy.random.randint(1,10)
                        
                        if lin_fullstage < 5:
                            if myrandom == 1:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " Lin, you look incredibly fit and strong. Your hard work really shows, and it's inspiring!"
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " Thank you so much! I appreciate the compliment. I work hard to maintain my fitness level."
                            if myrandom == 2:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " I've always admired how toned and sculpted you are, Lin. You're a true fitness role model."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " It means a lot to hear that, especially from someone who's dedicated to fitness like you, Player."
                            if myrandom == 3:
                                $ position = "parklintalklisten"
                                call sceneimg

                                player " Your dedication to staying in shape is evident, Lin. You have an impressive physique."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " Thanks! Staying in shape is not just my job; it's my passion too."
                            if myrandom == 4:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " Your muscles are so well-defined, Lin. It's clear you put a lot of effort into your workouts."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " Your kind words motivate me to keep pushing myself in the gym. Thanks, Player!"
                            if myrandom == 5:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " Lin, your flat and defined belly is goals! You're an embodiment of fitness and health."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " I'm glad you noticed! Achieving a flat belly and muscle definition takes commitment."
                            if myrandom == 6:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " I've never seen someone with such a perfectly sculpted physique like yours, Lin. You're stunning!"
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " Wow, that's incredibly sweet of you to say, Player. I'm flattered!"
                            if myrandom == 7:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " You've got an amazing figure, Lin. Your hard work at the fitness club truly pays off."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " Thanks for noticing the results of my hard work. It's always nice to hear such positive feedback."
                            if myrandom == 8:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " Lin, your body looks like a work of art. You've achieved an enviable level of fitness."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " Your words are a great encouragement, Player. Fitness is a journey, and I'm on it every day."
                            if myrandom == 9:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " Your abs are incredible, Lin. You must have a killer workout routine!"
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " Haha, thanks! My abs are the product of countless planks and crunches."
                            if myrandom == 10:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player " You radiate confidence and strength, Lin. Your physique is absolutely fantastic!"
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin " Your compliments make my day, Player. Let's keep pushing ourselves to be the best versions of ourselves!"
                        else:
                            if myrandom == 1:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "Lin, your dedication to fitness is incredible. Your toned physique is proof of your hard work."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "Thank you so much! I do my best to stay hydrated, and it can cause a little bloating sometimes."
                            if myrandom == 2:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "You look stunning, Lin. Your fitness journey is truly inspiring, and your belly doesn't take away from that at all."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "I appreciate your kind words. Staying hydrated is crucial for overall health, and it's worth it."
                            if myrandom == 3:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "Lin, your positivity is contagious. You have such a beautiful, toned figure, even if your belly is a bit bloated."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "Thank you for understanding. Hydration is key, and I want to set a healthy example for my clients."
                            if myrandom == 4:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "You're a fitness role model, Lin. Your strong physique is impressive, even if your belly is showing a little bloating today."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "I'm touched by your compliments. Hydration can cause temporary changes, but it's essential."
                            if myrandom == 5:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "Lin, your commitment to health is inspiring. Your body looks fantastic, even with a slight bloated belly."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "I'm grateful for your support. Staying hydrated is crucial for everyone, including fitness enthusiasts."
                            if myrandom == 6:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "You're a true fitness guru, Lin. Your belly might be bloated, but it doesn't take away from your incredible physique."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "Thank you for your understanding. Hydration is a priority, even if it leads to temporary changes."
                            if myrandom == 7:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "Lin, your fitness journey is remarkable. Your body is a testament to your dedication, even with that little belly bloat."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "I appreciate your kind words. Staying hydrated is crucial for overall well-being."
                            if myrandom == 8:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "Your physique is awe-inspiring, Lin. Even with some bloating, you look fantastic."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "Thank you for your support. Staying hydrated is a top priority for me."
                            if myrandom == 9:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "Lin, your fitness progress is undeniable. Your toned body is incredible, even if you're dealing with a bit of belly bloat."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "I'm grateful for your compliments. Hydration is a vital part of my lifestyle."
                            if myrandom == 10:
                                $ position = "parklintalklisten"
                                call sceneimg
                                player "You have an amazing figure, Lin. Your belly might be showing some bloating, but it doesn't diminish your fitness achievements."
                                $ position = "parklintalktalk"
                                call sceneimg
                                Lin "Thank you for understanding. Staying hydrated is essential for both fitness and overall health."

            "Ask Lin about her story" if linstory == 0:
                $ linstory = 1
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:
                    $ position = "parklintalklisten"
                    call sceneimg
                    player " Lin, I'm really curious about your background. How did you end up becoming a fitness trainer?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "That's a great question. My path to becoming a fitness trainer was quite a transformative journey. A few years ago, I was stuck in a job that was taking a toll on my physical and mental health. I found myself feeling stressed out, constantly fatigued, and lacking the vitality I knew I should have. It was a turning point in my life when I realized that something had to change."

                    "One day, I decided to take matters into my own hands. I started exercising regularly and paying more attention to my diet. The results were astonishing. I not only regained my energy and health but also discovered a profound passion for fitness. The feeling of empowerment and well-being that I experienced was something I wanted to share with others."

                    "So, I embarked on a journey to become a certified fitness trainer. It wasn't easy, but the desire to help people transform their lives through fitness kept me going. Today, I'm proud to be a fitness trainer, guiding and inspiring others to achieve their health and wellness goals. It's been an incredibly fulfilling path, and I'm grateful for every step that led me here."

                if myrandom == 2:
                    $ position = "parklintalklisten"
                    call sceneimg
                    player " Lin, you're so dedicated to your fitness training career. Can you tell me what motivated you to pursue this path?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "Absolutely. My motivation to become a fitness trainer stems from a personal journey that profoundly changed my life. A few years back, I faced some health challenges that forced me to reevaluate my lifestyle. I was living a sedentary life, and it took a toll on both my physical and mental well-being."

                    "It was during this period that I discovered the incredible power of exercise. I started incorporating fitness into my daily routine, and the positive impact it had on my health was undeniable. Not only did I regain my strength and vitality, but I also found a sense of purpose and passion that had been missing in my life."

                    "Realizing the transformative potential of fitness, I decided to take a leap of faith. I pursued a certification in fitness training and began my journey to help others experience the same positive changes. Today, I'm living my dream by empowering individuals to take control of their health, just as I did."

                if myrandom == 3:
                    $ position = "parklintalklisten"
                    call sceneimg
                    player " Lin, your commitment to fitness is impressive. What's the story behind how you became a fitness trainer?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "Thank you for noticing. My journey into the world of fitness training is quite a personal one. Years ago, I was working in a high-stress job that left me feeling unfulfilled and drained both mentally and physically. I knew that something needed to change, but I wasn't sure what that change should be."

                    "One day, I decided to prioritize my well-being and started exploring various forms of exercise and healthier eating habits. The impact was astounding. I felt a renewed sense of energy and vitality, and my overall quality of life improved dramatically."

                    "That experience ignited a passion within me. I became fascinated by the connection between physical activity, mental well-being, and personal transformation. I knew that I wanted to share this knowledge and help others discover their own potential for positive change."

                    "So, I dedicated myself to becoming a certified fitness trainer. It was a challenging but incredibly rewarding journey. Today, I'm living my dream by helping individuals like you embrace a healthier and more vibrant lifestyle. It's a journey I'm deeply committed to, and I'm grateful for the opportunity to make a difference in people's lives through fitness."

            "Lin asks about you" if linaboutyou == 0:
                $ linaboutyou = 1
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "Thank you for sharing your story. It's fascinating to hear about your journey as a chef. Can you tell me more about what inspired you to pursue cooking professionally?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Absolutely, Lin. Cooking has been a part of my life since I was a child. I used to watch my grandmother in the kitchen, creating these incredible dishes from scratch. Her ability to turn simple ingredients into something extraordinary always amazed me. As I grew older, I started experimenting with cooking on my own. It wasn't just about the flavors; it was about the joy of bringing people together through food. The happiness and satisfaction on their faces when they taste something delicious, that's what made me decide to become a chef."

                if myrandom == 2:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "It's wonderful to hear about your journey into the culinary world. You mentioned your grandmother as an inspiration. Can you share a specific memory or dish that had a significant impact on you?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Certainly, Lin. There's this one dish my grandmother used to make, a simple family recipe for lasagna. She would layer it with homemade pasta, rich tomato sauce, and an assortment of cheeses. I remember the aroma that filled the house as it baked in the oven, and the first bite was like a burst of flavor in my mouth. That dish, to me, symbolizes comfort, love, and the power of food to create lasting memories. It was that kind of experience that made me want to pursue cooking professionally."

                if myrandom == 3:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "Your journey into the culinary world is truly inspiring. As a chef, you must have encountered various challenges and triumphs along the way. Could you share one memorable experience that helped shape your career?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Of course, Lin. There was a moment during my culinary training when I was tasked with preparing a complex, multi-course meal for a prestigious event. The pressure was intense, and I was working long hours, often without much sleep. But what I remember most is the satisfaction I felt when I saw the guests enjoying every bite of my creations. It was a turning point for me, realizing that all the hard work, dedication, and attention to detail were worth it. That experience solidified my passion for cooking and the desire to bring joy to people's lives through food."

                # Lin asks if he cooks at home also
            "Lin asks if you cook at home" if lincookhome == 0:  
                $ lincookhome = 1  
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "It's clear that you have a deep passion for cooking. Do you get the opportunity to cook at home as well, or is most of your culinary creativity expressed at the restaurant?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Absolutely, Lin. Cooking at home is like my creative sanctuary. After a long day at the restaurant, I relish the chance to experiment with new recipes or revisit old favorites. There's a certain joy in selecting the freshest ingredients, chopping, slicing, and sizzling away in my kitchen. Plus, it's a great way to unwind and share delicious meals with friends and family."
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "That sounds wonderful. Cooking can be such a personal and therapeutic experience. It's incredible that you find time for it even with your busy restaurant schedule."

                if myrandom == 2:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "It's clear that you have a deep passion for cooking. Do you get the opportunity to cook at home as well, or is most of your culinary creativity expressed at the restaurant?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Absolutely, Lin. I believe in bringing the restaurant experience home. I've designed my kitchen to be a mini version of a professional kitchen, complete with all the gadgets and equipment I need to whip up delicious meals. It's my haven for culinary experiments."
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "That's incredible. You must have a well-equipped kitchen! I'm sure your friends and family must adore your home-cooked dishes."

                if myrandom == 3:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "It's clear that you have a deep passion for cooking. Do you get the opportunity to cook at home as well, or is most of your culinary creativity expressed at the restaurant?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "You know, Lin, it's a balance. Cooking at the restaurant is my profession, and I pour my heart and soul into it. But when I'm home, I like to keep it simple. Sometimes it's just about a comforting bowl of pasta or whipping up a quick stir-fry. It's my way of disconnecting from the restaurant and enjoying food in its simplest form."
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "I can understand that. Cooking should bring joy, whether in a restaurant kitchen or your own. It's great to hear how you find your own rhythm with it."

            "Chat a little" if linparkchat == 0:
                $ linparkchat = 1
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:
                    $ position = "parklintalklisten"
                    call sceneimg
                    player "Lin, how did you spend your day yesterday?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "Yesterday was a great day. I started with an early morning run at the park, had a productive day at the fitness club, and in the evening, I met up with some friends for dinner. It was a nice balance of work and leisure. How about you? How was your day yesterday?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "That sounds like a well-rounded day, Lin. I spent most of my day at the restaurant, experimenting with some new recipes. Later in the evening, I took a walk along the beach and enjoyed the peaceful sunset. It was quite relaxing."

                if myrandom == 2:
                    $ position = "parklintalklisten"
                    call sceneimg
                    player "Lin, what did you do yesterday? Any interesting highlights?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "Oh, yesterday was a blast! I organized a fitness workshop at the club, which was a hit. Afterward, I treated myself to some frozen yogurt and caught up on a good book I've been reading. It was a perfect day. How about your day? Anything exciting?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Your day sounds productive and enjoyable, Lin. I had a busy day at the restaurant, too, trying out some new dishes. In the evening, I met up with a friend and we explored a new burger cafe in town. It was a fun time."

                if myrandom == 3:
                    $ position = "parklintalklisten"
                    call sceneimg
                    player "Lin, did you have a good day yesterday?"
                    $ position = "parklintalktalk"
                    call sceneimg

                    Lin "I did, thanks for asking. I started my day with a sunrise yoga session, then had a busy day at the fitness club. In the evening, I tried out a new Mediterranean restaurant in town. How about your day? How was it?"
                    $ position = "parklintalklisten"
                    call sceneimg

                    player "Your day sounds lovely, Lin. I spent most of my day working in the kitchen at the restaurant, experimenting with some new dishes. After work, I took a stroll through the park and enjoyed the fresh air. It was a nice way to unwind."

            "Would you like to ride a bike?" if linrideabike == 0:
                $ linrideabike = 1
                
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "Hey, do you enjoy riding a bicycle? I was thinking about going for a nature trip this weekend, and it could be a lot of fun. Would you be interested in joining me?"
                    menu:
                        "Sure":
                            $ linrideabikesat = 1
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Biking sounds like a great idea, Lin. I haven't ridden in a while, but I'd be up for the adventure. Count me in!"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "That's awesome! I love exploring the countryside on my bike. There's this beautiful trail I've been wanting to check out. We can soak up some fresh air, enjoy the scenery, and maybe even have a picnic along the way."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Sounds like a fantastic plan. It's been too long since I've connected with nature like that. What time should I meet you on Saturday?"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "How about we meet at the park entrance around 10 AM? That should give us plenty of daylight to make the most of our trip."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Perfect. I'll be there, bright and early. Do I need to bring anything specific?"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Just your adventurous spirit, a water bottle, and a sense of excitement. We'll enjoy the ride, and I'll bring some snacks for our pitstops. It's going to be a memorable day! See you at about 10:00 on Saturday"
                            
                        "No, thank you":
                            $ linrideabikesat = 0
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Well, Lin, I appreciate the offer, but I'm not really a fan of cycling. I think I'll pass this time."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Oh, that's totally fine! We all have our preferences. If you ever change your mind or want to try something else, just let me know. I'm always up for different activities."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Thanks, Lin. I'll keep that in mind. Have a fantastic time on your trip!"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Will do! Enjoy your weekend."

                if myrandom == 2:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "Have you ever tried cycling? I'm planning a nature trip on my bicycle this weekend. It's a fantastic way to enjoy the outdoors. Would you like to come along?"
                    menu:
                        "Sure":
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Cycling sounds like a great way to explore nature. I haven't done it in a long time, but I'd love to give it a try. I'm in!"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "That's fantastic to hear! There's something magical about pedaling through scenic routes. I've mapped out a trail with some breathtaking views. We can take our time, snap photos, and simply revel in nature's beauty."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "I'm definitely looking forward to it. What day are we talking about, and what should I prepare for?"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "How about this Saturday 10:00? It's usually quieter on the trails. As for preparations, just wear comfortable clothing and bring your enthusiasm. I'll make sure we have enough snacks and refreshments."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Saturday it is! I can't wait to see what you have in store for our adventure."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Get ready for a day of exploration and relaxation. It's going to be unforgettable!"

                            
                        "No, thank you":
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Lin, I appreciate the offer, but I'm not really into biking. I'll have to decline this time."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "No worries at all! Everyone has their own interests. If you ever want to explore nature in a different way or if there's something else you'd like to do, just let me know. I'm open to new adventures."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Thanks for understanding, Lin. Have a wonderful time on your bike trip!"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "I will. Enjoy your weekend, whatever you choose to do!"
                if myrandom == 3:
                    $ position = "parklintalktalk"
                    call sceneimg
                    Lin "Hey, do you have any interest in biking? I'm organizing a nature trip on my bicycle this weekend, and I thought it might be a nice way to spend time together. What do you say?"
                    menu:
                        "Sure":
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Biking in nature does sound appealing. It's been a while since I've been on a bicycle, but I'm up for the challenge. Let's do it!"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Awesome! I'm glad you're on board. I've got this fantastic route in mind that takes us through some stunning landscapes. We'll have opportunities to stop, take photos, and enjoy some peaceful moments."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "That sounds like a perfect way to unwind and connect with nature. When and where should I meet you?"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "How about meeting at the bike rental place near the park this Saturday at 9:30 AM? We can grab our bikes, and I'll bring some light snacks for our little adventure."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Great! I'll be there. Looking forward to it, Lin."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Me too. It's going to be a fantastic day outdoors!"
                        "No, thank you":
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Lin, I appreciate the invitation, but I'm not really a cyclist. I'll have to decline this time."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "No problem at all! Everyone has their own preferences when it comes to outdoor activities. If you ever want to do something else or just hang out, feel free to reach out. I'm always up for good company."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Thanks, Lin. I'll keep that in mind. Have a fantastic bike ride this weekend!"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Will do. Enjoy your weekend, too, whatever you decide to do!"
            


                    
            "Ask Lin out" if asklinout == 0 and promcafe >= 5:
                $ asklinout = 1
                $ myrandom = renpy.random.randint(1,3)
                menu:
                    "For lunch":
                        if myrandom == 1:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Hey Lin, I was thinking, how about grabbing lunch together at that beach cafe near the park? It's a great spot, and I'd love to spend more time with you."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "I appreciate the offer, but I'm swamped with work during the day, especially this time. Maybe we can plan for another time when I have a bit more flexibility?"
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Of course, Lin, no worries. Just let me know when you have some free time. We'll make it work."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Thanks for understanding. I'll definitely keep that in mind."

                        if myrandom == 2:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Lin, I've enjoyed our conversations, and I was wondering if you'd like to have lunch at that beach cafe near the park sometime?"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "I'd love to, but this time of the day is usually quite busy for me with work. Can we plan for another time when I'm less tied up?"
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Absolutely, no pressure, Lin. Just let me know when you're free, and we'll make it happen."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Thanks for being understanding. I'm looking forward to it."

                        if myrandom == 3:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Lin, I've been thinking about getting to know you better. How about we have lunch at that beach cafe near the park one of these days?"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "I really appreciate the offer, but my schedule during lunchtime is packed with work at the moment. Can we plan for another time when I have more availability?"
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Of course, Lin, I understand. Let's plan it for a time that works better for you."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Thank you for being so understanding. I'll make sure to let you know when I'm free."
                    "For dinner":
                        $ lin_cafetoday = 1
                        $ promcafetoday = 0
                        if myrandom == 1:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Lin, I have an idea. How about we have dinner at that beach cafe at the prom in the park this evening at 19:00? The view of the sunset is breathtaking."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "That sounds like a fantastic idea. I'd love to have dinner with you by the beach tonight at 19:00."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Wonderful! I'll make a reservation for 19:00, and we can enjoy the sunset together."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Just one thing, please make sure not to be late at 19:00."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "I promise I'll be there on time. I can't wait!"

                        if myrandom == 2:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Lin, I've found this charming beachside cafe at the prom in the park. The ambiance there is lovely, and I was wondering if you'd like to join me for dinner this evening at 19:00?"
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Dinner by the beach? That sounds wonderful. I'd be happy to join you at 19:00."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Great! I'll make sure to reserve a table with the best view for 19:00."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Just a little reminder, please be there at 19:00 sharp. I'm looking forward to it!"

                        if myrandom == 3:
                            $ position = "parklintalklisten"
                            call sceneimg
                            player "Lin, what do you say we grab dinner at that beach cafe in the park tonight at 19:00? The atmosphere there is really nice."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Dinner at the beach cafe? That sounds like a lovely idea. I'm in for 19:00."
                            $ position = "parklintalklisten"
                            call sceneimg

                            player "Awesome! I'll take care of the details, and I'll see you there at 19:00."
                            $ position = "parklintalktalk"
                            call sceneimg

                            Lin "Just a quick note, please make sure you're not running late. 19:00 it is! Looking forward to it."
                        $ lin_cafetoday = 1
            "How about hiking?" if linhike == 0:
                $ linhike = 1
                menu:
                    "I'm in":
                        $ linhikesun = 1
                        $ myrandom = renpy.random.randint(1,3)
                        if myrandom == 1:
                        

                            Lin "Hey, how about a hike this Sunday? I was thinking we could start after 10:00 AM. It's been too long since our last one."

                            player "Sunday after 10:00 sounds perfect, Lin. A morning hike is just what I need. I'm in."

                            Lin "Great! There’s this trail with amazing views around that time of day. It should be a relaxing yet invigorating hike."

                            player "I'm already looking forward to it. Your trail choices are always spot on. Let's touch base on Saturday for the final plan."

                            Lin "Sounds good. I'll send you the trail map and we can meet up at the trailhead. Excited for our hike!"
                        if myrandom == 2:

                            Lin "I'm planning a scenic hike this Sunday and thought you might want to join. How does starting after 10:00 AM sound?"

                            player "A scenic hike on Sunday post-10:00 AM is perfect for me. I'm always up for exploring nature, especially with good company."

                            Lin "Awesome! There’s a trail that’s just beautiful later in the morning. It's the perfect mix of sun and shade."

                            player "That sounds ideal. Your hiking recommendations are always a hit. Let's finalize our plans closer to the weekend."

                            Lin "Definitely! I’ll text you all the details. Can't wait for our Sunday adventure."
                        if myrandom == 3:

                            Lin "What do you think about a Sunday hike? I was thinking we could hit the trails after 10:00 AM. Interested?"

                            player "A hike on Sunday after 10:00? That's a great idea, Lin. I'd love to join. Where were you thinking of going?"

                            Lin "There's this one trail that really comes to life in the late morning. It’s not too crowded and offers some incredible views."

                            player "That sounds like a perfect way to spend a Sunday morning. Count me in. We can iron out the details later in the week."

                            Lin "Perfect! I'll get everything sorted and let you know. Looking forward to it!"
                    "Well, I'm not ready yet":
                        if myrandom == 1:

                            Lin "Hey, I'm planning a hike this Sunday and thought you might want to join. We'll start after 10:00 AM. Are you in?"

                            player "Lin, that sounds like a great plan, but I'm not quite ready for such a physical activity yet. I need to build up my endurance a bit more."

                            Lin "I understand completely. It's important to listen to your body. Maybe we can plan something less strenuous soon?"

                            player "That would be perfect. Thanks for being so understanding. I’d love to join once I feel more up to it."

                            Lin "No problem at all. Let’s keep in touch and find something that works for both of us. Take care!"
                        if myrandom == 2:

                            Lin "I was thinking about going for a hike this Sunday after 10:00 AM. It should be fun! Do you want to come along?"

                            player "Thanks for the invite, Lin, but I think I'll have to pass this time. I'm not quite ready for a hike yet. I need to work on my fitness a bit more."

                            Lin "I get that. It’s important to be comfortable with the activity level. Let me know when you're feeling up for it, and we can plan something together."

                            player "Definitely, I appreciate your understanding. Hopefully, I'll be ready to join you on one of your hikes soon."

                            Lin "Looking forward to it. In the meantime, if there’s something else you’d like to do, just let me know."
                        if myrandom == 3:

                            Lin "This Sunday, I'm going hiking after 10:00 AM. It's going to be a beautiful day for it. Want to join me?"

                            player "I really appreciate the offer, Lin, but I'm not ready for a hike right now. I need a bit more time to prepare myself physically."

                            Lin "No worries at all. It's important to do what feels right for you. Maybe we can plan a casual walk or something lighter soon?"

                            player "That sounds fantastic. Thanks for being so understanding. I’ll definitely take you up on that offer when I’m more prepared."

                            Lin "Great! Just let me know when you're ready. We can always find activities that suit us both."
            "Ask if she is thirsty" if water_bottle >= 1:
                
                $ myrandom = renpy.random.randint(1,2)
                if myrandom == 1:
                    
                    $ myrandom = renpy.random.randint(1,3)
                    if myrandom == 1:
                        $ position = "parklintalklisten"
                        call sceneimg
                        player "Lin, are you feeling thirsty? I could get us some refreshing drinks from the cafe nearby."
                        $ position = "parklintalktalk"
                        call sceneimg

                        Lin "That's very thoughtful of you, but I'm actually good for now. I appreciate the offer, though."
                        $ position = "parklintalklisten"
                        call sceneimg

                        player "No problem, Lin. If you change your mind, just let me know. I'm happy to grab something for you."
                        $ position = "parklintalktalk"
                        call sceneimg

                        Lin "Thank you. I'll keep that in mind."
                        $ reputationchange = 1
                        $ nigirlimage = "nilin"
                        call reputationchange
                    if myrandom == 2:
                        $ position = "parklintalklisten"
                        call sceneimg
                        player "Lin, are you feeling thirsty? I could get us some drinks from the cafe nearby."
                        $ position = "parklintalktalk"
                        call sceneimg

                        Lin "I appreciate the offer, but I'm actually quite hydrated at the moment. Thanks for thinking of me, though."
                        $ position = "parklintalklisten"
                        call sceneimg

                        player "No worries, Lin. If you ever need a drink or a snack, just give me a shout. I'm happy to help."
                        $ position = "parklintalktalk"
                        call sceneimg

                        Lin "That's very kind of you. I'll keep that in mind."
                        $ reputationchange = 1
                        $ nigirlimage = "nilin"
                        call reputationchange
                    if myrandom == 3:
                        $ position = "parklintalklisten"
                        call sceneimg
                        player "Lin, are you feeling thirsty? I could grab us some drinks from the cafe nearby."
                        $ position = "parklintalktalk"
                        call sceneimg

                        Lin "I'm actually quite good on the hydration front, but I appreciate your consideration. Thanks for offering."
                        $ position = "parklintalklisten"
                        call sceneimg

                        player "No problem, Lin. If you ever need a drink or a snack, just let me know. I'm here to help."
                        $ position = "parklintalktalk"
                        call sceneimg

                        Lin "That's very kind of you. I'll remember that."
                        $ reputationchange = 1
                        $ nigirlimage = "nilin"
                        call reputationchange
                if myrandom == 2:
                    $ position = "parklintalktalk"
                    call sceneimg
                    player "Lin, you look a bit thirsty. How about we grab a drink?"
                    $ position = "parklintalklisten"
                    call sceneimg
                    Lin "You're right, I could really use a drink. What are you thinking?"
                    menu:
                        "Water" if water_bottle >= 1:
                            $ position = "parklintalktalk"
                            call sceneimg
                            player "Water it is. Always the best for hydration."
                            $ lin_fullness += 250  # add 250ml to fullness after she drinks it
                            $ water_bottle -= 1    # remove one water bottle from inventory
                            $ position = "parklintalklisten"
                            call sceneimg
                            Lin "Thank you! This water is just perfect."
                        "Iced Tea" if iced_tea >= 1:
                            $ position = "parklintalktalk"
                            call sceneimg
                            player "How about some iced tea? It's both cooling and tasty."
                            $ lin_fullness += 300  # add 300ml to fullness after she drinks it
                            $ iced_tea -= 1        # remove one iced tea from inventory
                            $ position = "parklintalklisten"
                            call sceneimg
                            Lin "Thanks! Iced tea sounds really refreshing."
                        "Smoothie" if smoothie_drink >= 1:
                            $ position = "parklintalktalk"
                            call sceneimg
                            player "Maybe a smoothie? Something fruity and invigorating."
                            $ lin_fullness += 400  # add 400ml to fullness after she drinks it
                            $ smoothie_drink -= 1  # remove one smoothie from inventory
                            $ position = "parklintalklisten"
                            call sceneimg
                            Lin "Mmm, this smoothie is delicious! Thank you."
                    $ reputationchange = 1
                    $ nigirlimage = "nilin"
                    call reputationchange

            "Go for a walk":
                jump parknothing
                

        


    else:
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "parklinrunning"
            call sceneimg
            "Lin running intensely along the promenade, clearly focused on her workout."
            $ position = "parklinrunningthrough"
            call sceneimg
            "As she approaches, you wait for her to finish her current interval before attempting to strike up a conversation. But she runs through"

        if myrandom == 2:
            $ position = "parklinrunning"
            call sceneimg
            "You watch Lin as she goes through her high-intensity intervals, impressed by her dedication to her workout."
            $ position = "parklinrunningthrough"
            call sceneimg
            "You decide to wait until she takes a break to chat with her. But she runs through"

        if myrandom == 3:
            $ position = "parklinrunning"
            call sceneimg
            "You observes Lin's rigorous training routine and admires her commitment."
            $ position = "parklinrunningthrough"
            call sceneimg
            "You patiently wait for the right moment to engage in a conversation with her. But she runs through"
        
        
    
        $ position = "parklinrunningthrough"
        call sceneimg 
        jump parknothing
    
    jump linpark

    