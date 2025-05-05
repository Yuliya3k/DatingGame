label linpromcafetalk:

    menu:
        
        "Say sorry again" if lintoolate == 1 and lintoolatesorry == 0:
            $ lintoolatesorry = 1
            $ position = "parkpromlincafesittinglistening"
            call sceneimg
            player "  Lin, I'm really sorry I'm late. I had to stay at work longer than expected, and I don't have a car, so I couldn't get here any faster. My clients needed my help, and I couldn't say no."
            $ position = "parkpromlincafesittingtalking"
            call sceneimg

            Lin "  I get it, Player. I'm also client-oriented, and I respect that. But this is the third time you've been late, and it's starting to affect our plans."
            $ position = "parkpromlincafesittinglistening"
            call sceneimg

            player "  I know, and I hate that I keep letting you down. I value our time together, and I promise to make it up to you somehow."
            $ position = "parkpromlincafesittingtalking"
            call sceneimg
            Lin "  Look, I know how work can be demanding. Let's try to find a solution together so this doesn't happen again. Maybe we can adjust our meeting times or days."
            $ position = "parkpromlincafesittinglistening"
            call sceneimg

            player "  That sounds like a great idea, Lin. I'll do whatever it takes to ensure this doesn't become a problem again."
            $ position = "parkpromlincafesittingtalking"
            call sceneimg

            Lin "  I appreciate your willingness to work this out. Let's make sure our future meetings go smoothly."
            $ position = "parkpromlincafesittinglistening"
            call sceneimg

            player "  Thanks, Lin. I won't take your time for granted, and I'll make sure to prioritize our plans."

    



        "What would you like to eat?" if lindtaeeatq == 0:
            
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                call lindatelistening
                player "  Lin, I've been looking forward to our dinner all day. What do you feel like eating tonight?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Well, I'm in the mood for something light and healthy. How about a nice salad with grilled chicken?"
                call lindatelistening
                

                player "  That sounds great! A salad it is, then. Anything specific you'd like in it?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Let's go with mixed greens, cherry tomatoes, cucumbers, and some balsamic vinaigrette dressing. And, of course, a generous portion of grilled chicken on top."
                call lindatelistening

                player "  Perfect choice. I'll make sure to get that for you. Anything else you're craving?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Maybe a side of garlic bread if they have it. I do love a good garlic bread."
                call lindatelistening

                player "  Noted. Salad with grilled chicken and garlic bread it is. Anything to drink?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Just some water with a slice of lemon, please. Keeping it refreshing."

            if myrandom == 2:
                call lindatelistening
                player "  Lin, what's your preference for dinner tonight? Any particular cuisine in mind?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  I've been craving Italian lately. How about we go for some delicious pasta?"
                call lindatelistening

                player "  Italian it is! What type of pasta do you like? Spaghetti, fettuccine, or something else?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Let's go with fettuccine Alfredo. Creamy pasta is always a comforting choice."
                call lindatelistening

                player "  Excellent choice. Fettuccine Alfredo it is. Do you want any toppings or additions to it?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Some grilled shrimp on top would be amazing. It adds that extra flavor I love."
                call lindatelistening

                player "  You got it. Fettuccine Alfredo with grilled shrimp. Anything to drink?"

                Lin "  Just some iced tea with a slice of lemon, please. It complements the pasta nicely."

            if myrandom == 3:
                call lindatelistening
                player "  Lin, I'm up for anything tonight. What's your favorite type of cuisine?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  How about some Mexican food? I'm in the mood for some tasty tacos."
                call lindatelistening

                player "  Mexican it is! Tacos sound like a great choice. What kind do you prefer?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Let's go for chicken tacos with plenty of salsa and guacamole."
                call lindatelistening

                player "  Chicken tacos it is. Do you like them spicy or mild?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Spicy, definitely. I can handle some heat."
                call lindatelistening

                player "  Spicy chicken tacos with all the fixings. What would you like to drink?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  A classic margarita, please. It's the perfect match for Mexican food."

            $ lindtaeeatq = 1
            $ moneytoadd = -50
            call moneynotification
        "How was your day?" if lindatehowstheday == 0:
            $ lindatehowstheday = 1
            $ myrandom = renpy.random.randint(1,3)

            if myrandom == 1:
                call lindatelistening
                player "  Lin, I hope you had a good day today. How did everything go for you?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Thanks for asking! It was quite busy at the fitness club, but I love helping my clients reach their goals. So, it was a fulfilling day. We had some new members join, and I conducted a few group sessions."
                call lindatelistening

                player "  That's great to hear. Your dedication to your clients is admirable. It sounds like your club is growing."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Well, I learned from the best. How about you, how was your day?"
                call lindatelistening

                player "  My day was interesting. I tried a new recipe at the restaurant, and it turned out to be a hit with our customers. Plus, we had a lively crowd during dinner service."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  That's fantastic! It's always nice to experiment and see positive results. What kind of dish did you create?"

            if myrandom == 2:
                call lindatelistening
                player "  Lin, I'm always curious about how your day goes. Anything interesting happen today?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Today was a fantastic day at the fitness club! One of my clients hit a personal best, and it was such a rewarding moment. I also had a consultation with someone who's just starting their fitness journey."
                call lindatelistening

                player "  That must have been a proud moment for both of you. It's clear you're passionate about your work."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Absolutely. It's incredibly fulfilling to witness their progress. How about your day? Anything noteworthy?"
                call lindatelistening

                player "  Well, at the restaurant, we had a surprise visit from a food critic, which made things a bit nerve-wracking. But they enjoyed their meal, and we received a glowing review, so it was worth it."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  A food critic? That's impressive! It sounds like you're maintaining the restaurant's high standards."

            if myrandom == 3:
                call lindatelistening
                player "  Lin, I hope your day treated you well. What kept you busy today?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Thanks for asking! It was a productive day at the fitness club. I had back-to-back training sessions, and my clients are making great progress. We also had a team meeting to plan upcoming fitness events."
                call lindatelistening

                player "  Your clients are lucky to have you guiding them. It's clear you're making a positive impact."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  I do my best. Speaking of making an impact, how about your day? Anything exciting happening at the restaurant?"
                call lindatelistening

                player "  Well, we had a local charity event at the restaurant today. We partnered with them to raise funds, and it was heartwarming to see so many people come together for a good cause."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  That's wonderful! It's important to give back to the community. Kudos to you and the restaurant for making a difference."


        "Ask Lin about her bloat" if linbloatq == 0 and lin_fullstage < 6 and lin_attitude < 50:
            $ linbloatq = 1
            $ myrandom = renpy.random.randint(1,3)
            $ position = "linpromcafebellyview"
            call sceneimg
            if myrandom == 1:
                # call lindatelistening
                player "  Lin, are you feeling alright? Your belly seems a bit bloated today."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Oh, that's just from a hearty meal earlier. I may have indulged in some comfort food. Don't worry; it's nothing serious."
                call lindatelistening

                player "  Alright, as long as you're okay. Sometimes, indulging in comfort food is just what we need."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Exactly! It's all about balance, right?"

            if myrandom == 2:
                # call lindatelistening
                player "  Lin, did you have a feast before our meeting? Your belly looks quite full."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Guilty as charged! I couldn't resist those delicious treats. It's not often I indulge like this."
                call lindatelistening

                player "  Well, you deserve a treat now and then. Enjoy your food coma!"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Thanks, I will!"

            if myrandom == 3:
                # call lindatelistening
                player "  Lin, it looks like you've been enjoying some good food lately. Your belly is giving it away."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  You caught me! I couldn't resist some of my favorite dishes. It's like a little celebration."
                call lindatelistening
                

                player "  Celebrations are important! Food is one of life's pleasures. Enjoy every bite."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Thanks for understanding. It's nice to indulge once in a while."


        "Ask Lin about her bloat" if linbloatq == 0 and lin_fullstage < 6 and lin_attitude > 49:
            $ linbloatq = 1
            $ myrandom = renpy.random.randint(1,3)
            $ position = "linpromcafebellyview"
            call sceneimg
            if myrandom == 1:
                # call lindatelistening
                player "  Lin, it looks like your belly's enjoying the good life lately."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Oh, you noticed? Well, you've got good taste, and I know you like it."
                call lindatelistening
                player "  Guilty as charged!"

            if myrandom == 2:
                # call lindatelistening
                player "  Lin, your belly seems to be in a delightful state today."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  You know me too well. And I know you like it this way."
                call lindatelistening

                player "  You caught me! I can't deny it."

            if myrandom == 3:
                # call lindatelistening
                player "  Lin, someone's been savoring some delicious meals recently. Your belly is proof of that."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  It's hard to resist, and I know you appreciate it."
                call lindatelistening

                player "  You're absolutely right, I do!"

        "Ask Lin about her bloat" if linbloatq == 0 and lin_fullstage > 5 and lin_attitude < 50:
            $ linbloatq = 1
            $ myrandom = renpy.random.randint(1,3)
            $ position = "linpromcafebellyview"
            call sceneimg
            if myrandom == 1:
                # call lindatelistening
                player " Lin, your belly looks like it's about to give birth to triplets! Are you sure you're not secretly expecting?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Trust me, it's just a food baby, not a real one. But I appreciate the concern!"

                player "  Well, your food baby is quite impressive."

            if myrandom == 2:
                # call lindatelistening
                player " Lin, I have to ask, is there a secret pregnancy announcement I missed? Your belly is looking very convincing!"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  No, no, it's just a result of a hearty meal. But thanks for checking in!"
                call lindatelistening

                player "  Just making sure I'm not missing any big news!"

            if myrandom == 3:
                # call lindatelistening
                player " Lin, if I didn't know better, I'd say you were expecting. Your belly is really showing today!"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Oh, I assure you, it's just a post-meal situation. But I'm flattered you noticed!"
                call lindatelistening

                player "  Well, you do have a way of making it look convincing!"

        "Ask Lin about her bloat" if linbloatq == 0 and lin_fullstage > 5 and lin_attitude > 49:
            $ linbloatq = 1
            $ myrandom = renpy.random.randint(1,3)
            $ position = "linpromcafebellyview"
            call sceneimg

            if myrandom == 1:
                # call lindatelistening
                player " Lin, your belly is incredibly bloated right now. You look like you're about to have a baby."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Well, I did have a pretty big meal. You know how you like it when I'm all full and round."
                call lindatelistening

                player "  Guilty as charged. I have to admit, seeing you like this is quite the sight. It's a reminder of how much we enjoyed our meal together."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  You always know how to make me feel special, even when I'm stuffed."
                call lindatelistening

                player "  That's because you are special, Lin. I love every moment we spend together."

            if myrandom == 2:
                # call lindatelistening
                player " Lin, seriously, your belly looks like it's ready to pop. It's so round and full."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  You always seem to enjoy it when I indulge. I couldn't resist the temptation today."
                call lindatelistening

                player "  Temptation suits you well. You're a vision, and it's hard to look away."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Flattery will get you everywhere, you know. But I do enjoy knowing that you appreciate how much I ate."

                player "  I appreciate everything about you, especially moments like this."

            if myrandom == 3:
                # call lindatelistening
                player " Lin, your belly is impressively bloated. You know I can't resist when you look like this."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Well, someone knows how to appreciate a well-fed belly."
                call lindatelistening

                player "  What can I say? You wear it well, my dear. It's like you're carrying all the delicious memories of our meal."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  You always find a way to make me smile, even when I'm feeling a bit self-conscious about my full belly."
                call lindatelistening

                player "  There's no need to be self-conscious, Lin. I adore every part of you, especially when you're happy and content like this."

        "Ask Lin about her family" if lindatefamilyq == 0:
            $ lindatefamilyq = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                call lindatelistening
                player " Lin, tell me more about your family background. Do you have any siblings?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Sure, I don't mind sharing. I have a Chinese father and a European mother. They taught me to appreciate different cultures and perspectives."
                call lindatelistening
                player "  That's fascinating. I can see how your diverse upbringing has shaped you into the amazing person you are today."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Absolutely. It's all about embracing the best of both worlds. But one thing they both emphasized was discipline. It's been a crucial part of my life."
                call lindatelistening

                player "  Discipline can certainly lead to success. I can see that in your dedication to your fitness and training."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Well, I guess they did a good job instilling that in me."

            if myrandom == 2:
                call lindatelistening
                player " Lin, I'm curious about your family. What's your background?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Well, my dad is Chinese, and my mom is European. So, I've got this blend of cultures in my blood."
                call lindatelistening

                player "  That's quite the mix. How has that influenced your outlook on life?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  It's made me appreciate diversity and different viewpoints. But it also instilled discipline in me from a young age."
                call lindatelistening

                player "  Discipline is often the key to success. I can see how it's played a role in your fitness journey."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Absolutely. It's been a driving force behind my determination."

            if myrandom == 3:
                call lindatelistening
                player " Lin, can you share a bit about your family background with me?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Of course. My father is Chinese, and my mother is European. Growing up in a multicultural household was quite an experience."
                call lindatelistening

                player "  I can imagine. Did it shape your perspective on life in any particular way?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  It definitely did. I've learned to appreciate different cultures and viewpoints. But one thing that was consistent in my upbringing was the importance of discipline."
                call lindatelistening

                player "  Discipline seems to be a recurring theme in your life. It's evident in your dedication to your fitness routines and goals."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Yes, it's a quality I hold dear, and it has served me well in many aspects of life."


        "Ask if Lin likes the place" if linhowstheplaceq == 0:
            $ linhowstheplaceq = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                call lindatelistening
                player " Lin, do you like this place? The view of the sea from here is amazing."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Oh, I love it! The sea view is breathtaking, and it adds to the whole dining experience. You know, I've always found solace in the sound of the waves and the vastness of the sea. It's like a beautiful canvas that never ceases to amaze me."
                call lindatelistening

                player "  I'm glad you enjoy it, Lin. It's a perfect spot for a relaxing evening."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Absolutely. And the food here is delicious too, which makes it even better."

            if myrandom == 2:
                call lindatelistening
                player " Lin, how do you find this restaurant? It's got quite a view, doesn't it?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Absolutely! The sea view is stunning. It's a great choice for dinner. I've always been drawn to places near the water; there's something serene about it."
                call lindatelistening

                player "  I thought you'd appreciate it, Lin. It's nice to have a peaceful dinner while watching the waves."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Indeed, it's quite therapeutic, isn't it?"

            if myrandom == 3:
                call lindatelistening
                player " Lin, what do you think of this place? The sea view is something else, isn't it?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  I'm loving it! The sea view makes the dining experience even more special. You know, there's just this sense of tranquility that comes from being close to the water."
                call lindatelistening

                player "  I knew you'd appreciate it, Lin. It's a perfect spot to unwind after a long day."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  You've got that right. It's moments like these that make life truly beautiful."

        "Finish the date":
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                call lindatelistening
                player " Lin, this has been a wonderful evening. Thank you for joining me."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  I had a great time too. Thank you for the lovely dinner and conversation."
                call lindatelistening

                player "  It was my pleasure. Have a safe journey back, Lin."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  You too, take care. Goodnight."

            if myrandom == 2:
                call lindatelistening
                player " Lin, I must say, this evening was fantastic. Thank you for making it special."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  I'm glad to hear that. I had a wonderful time as well."
                call lindatelistening

                player "  It's always a pleasure spending time with you, Lin. Until next time."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Until next time indeed. Have a great night."

            if myrandom == 3:
                call lindatelistening
                player " Lin, I just wanted to say this was an amazing evening. Thanks for being a part of it."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  You're too kind. I truly enjoyed it too."
                call lindatelistening

                player "  Let's do this again sometime, Lin."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Absolutely! Looking forward to it. Goodnight."
            jump culinarychoices


        "What's your life plans?" if linwhatsthelifeplansq == 0:
            $ linwhatsthelifeplansq = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                call lindatelistening
                player " Lin, I'm curious about your plans for the future. What do you see yourself doing?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Well, I'm definitely passionate about fitness and helping others achieve their health goals. I want to continue growing as a fitness trainer and maybe even open my own studio someday."
                call lindatelistening

                player "  That sounds like a fantastic plan, Lin. You'd be an incredible studio owner."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Thank you. I hope to make it happen someday."

            if myrandom == 2:
                call lindatelistening
                player " Lin, where do you see your life heading in the coming years? Any big plans?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  I'm a big believer in setting goals. I want to excel in my career as a fitness trainer and hopefully inspire more people to lead healthier lives."
                call lindatelistening

                player "  Your dedication and passion are inspiring, Lin. I'm sure you'll achieve everything you set your mind to."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Your encouragement means a lot."

            if myrandom == 3:
                call lindatelistening
                player " Lin, have you thought about your future plans and aspirations?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Absolutely! I see myself continuing to help people reach their fitness goals. It's my calling, and I want to make a positive impact on as many lives as I can."
                call lindatelistening

                player "  Your commitment to helping others is truly commendable, Lin. The world needs more people like you."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Thank you so much. I'm just doing what I love."

        "Does she has a boyfriennd?" if lindatebfq == 0:
            $ lindatebfq = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                call lindatelistening
                player " Lin, I've really enjoyed our time together. Are you seeing anyone special?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Well, I wouldn't be here if I were, would I?"
                call lindatelistening

                player "  I guess not. Lucky for me, then."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Lucky indeed."

            if myrandom == 2:
                call lindatelistening
                player " Lin, I'm curious, are you currently in a relationship?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Nope, no significant other in the picture right now. Why do you ask?"
                call lindatelistening

                player "  Just making sure I'm not overstepping any boundaries."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Don't worry, you're not."

            if myrandom == 3:
                call lindatelistening
                player " Lin, can I ask if you're dating anyone at the moment?"
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Nope, I'm currently enjoying my single life."
                call lindatelistening

                player "  That's good to know. I'm having a great time too."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg

                Lin "  Looks like we're on the same page then."



jump linpromcafetalk