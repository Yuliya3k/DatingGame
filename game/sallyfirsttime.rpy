label sallyfirsttime:
    $ sally_fullness = renpy.random.randint(800,4000)
    $ myrandom = renpy.random.randint(1,2)
    if sallypark == 1 and myrandom == 1:
        
        if calendar.Hours > 5 and calendar.Hours < 9:
            $ myrandom = renpy.random.randint(1,2)
            if myrandom == 1:
                $ position = "parksallymorningrunningback"
                call sceneimg
                "As I continued my morning jog along the beautiful beachside promenade, I couldn't help but notice Sally up ahead. She was in her usual spot, running gracefully as the early sunlight shimmered on the sea. I knew who she was; we had talked a few times before. However, today, something held me back from approaching her."

                "It was strange, really. We weren't strangers, and Sally had always been friendly and approachable. Yet, I found myself hesitating. Maybe it was the early hour, or perhaps it was the way she seemed so lost in her thoughts, her determination evident in each step. It felt like I would be interrupting something sacred, her peaceful morning ritual."

                "So, I continued my run, offering a friendly wave as I passed by, but not stopping to chat. Sometimes, even when you know someone, there are moments when silence speaks louder than words. As I jogged on, I couldn't help but wonder about the mysteries that lingered in the spaces between us, waiting to be explored when the time felt right."
            if myrandom == 2:
                $ position = "parksallymorningrunning"
                call sceneimg
                "The morning sun was just beginning to cast a warm glow over the seaside park as I embarked on my daily stroll. As I followed the path along the sea, I noticed Sally approaching me with purpose in her stride. Her dedication to the morning run was evident, and I decided it was a good time to strike up a conversation."

                "With a friendly wave, I greeted her..."
                jump morningsallytalk
        if calendar.Hours > 17 and calendar.Hours < 23:
            $ myrandom = renpy.random.randint(1,3)        
            if myrandom == 1:
                $ position = "parksallyeveninglookingatthesea"
                call sceneimg
                "The evening sun cast a warm, golden glow over the serene sea, painting the sky with shades of pink and orange. As I walked along the beach promenade, I noticed Sally standing near the edge, her gaze fixed on the horizon where the sun met the water. She seemed utterly captivated by the tranquil beauty of the scene, lost in her thoughts."

                "For a moment, I debated whether to approach her and strike up a conversation. It was one of those moments when the world felt still, and the beauty of nature was a powerful backdrop to any interaction. But as I watched her, standing there in quiet contemplation, I decided to respect her moment of solitude."

                "Sometimes, words are not necessary to convey the shared appreciation of a breathtaking sunset over the sea. I continued my walk, acknowledging her presence with a nod and a warm smile. It was a silent understanding that in moments like these, the beauty of the world could be a connection in itself, and sometimes, silence spoke louder than words ever could."

            if myrandom == 2:  
                $ position = "parksallyeveningwalkingback"
                call sceneimg
                "As the sun began to dip below the horizon, casting a warm and golden hue across the tranquil sea, I strolled along the beachside promenade. The evening was calm, and the gentle sound of waves breaking on the shore provided a soothing backdrop to my thoughts."

                "I noticed Sally ahead, walking at her own leisurely pace along the promenade. I had seen her around the town before, and while I knew her name, we had never actually spoken. It felt like one of those small-town quirks where you're aware of people's presence but haven't yet crossed paths in a meaningful way."

                "This evening, the sight of her walking alone as the sun painted the sky with hues of pink and orange was a beautiful one. I was tempted to strike up a conversation, to finally break that invisible barrier between us, but something held me back. It was the strangeness of approaching a stranger you already recognized, a hesitation to intrude on the solitude of the moment."

                "So, I continued my walk, offering a polite smile as I passed by, but not venturing into conversation. Sometimes, the beauty of a moment lies in its simplicity, and perhaps our paths would cross naturally one day, leading to the kind of connection that can only be forged through time and shared experiences."

            if myrandom == 3: 
                $ myrandom = renpy.random.randint(1,2)
                if myrandom == 1:
                    $ position = "parksallyeveningwalking"
                    call sceneimg
                    "The evening sun was beginning its descent on the horizon, casting a warm, orange hue over the tranquil sea. As I strolled along the beach promenade, I noticed Sally approaching, her steps purposeful and her gaze focused."

                    "Seeing her headed in my direction, I decided to initiate a conversation. After all, we had crossed paths a few times recently, and it felt like the right moment to exchange a few words."
                    "I offered a friendly smile as she drew near."
                    jump eveningsallytalk

                     
                if myrandom == 2:
                    $ position = "parksallybencheveningsitting"
                    call sceneimg
                    "The evening was settling in as I took a leisurely stroll along the promenade, savoring the calming sound of the waves. As I meandered, I spotted Sally sitting alone on a bench, gazing out at the tranquil sea."

                    "Approaching her, I couldn't resist the urge to say hello. After all, we had shared some pleasant conversations before, and the sight of her enjoying the serene view seemed like the perfect opportunity to reconnect."

                    "With a friendly smile, I greeted her..."
                    jump eveningsallytalk
        if calendar.Hours > 8 and calendar.Hours < 18:
            $ position = "parkwalk"
            call sceneimg
    else:
        jump parknothing

    jump culinarychoices
    
  
    


    

    label eveningsallytalk:
        menu:
            "Say hello" if sallyhello < 2 and sallyhellotoday == 0:
                $ sallyhellotoday = 1
                if sallyhello == 1:
                    $ myrandom = renpy.random.randint(1,3)
                    if myrandom == 1:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sally, it's good to see you again. How was your day?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally  "Oh, hi there! Well, my day was quite busy, to be honest. You know, the usual chores at Mr. Johnson's mansion, making sure everything's in order."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sounds like a lot of work. How do you manage it all?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg

                        Sally "It can be overwhelming at times, but Mr. Johnson is really considerate. He cares about his employees, so he makes sure we're well-fed and taken care of."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "That's great to hear. It's not every day you find an employer who looks out for their staff like that."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg

                        Sally "I know, right? I'm truly fortunate to work for him. And it's nice to unwind with a run in this serene park in the evening."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Well, it certainly is a lovely place for a stroll. I'm glad I bumped into you again."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg

                        Sally "Likewise. It's always nice to chat. How about you? How was your day?"

                    if myrandom == 2:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sally, good to see you. How did your day go?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Hey there! My day was quite eventful, actually. I had some unexpected tasks at Mr. Johnson's mansion, but I managed to get everything done."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg

                        player "Unexpected tasks? Anything interesting?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg

                        Sally "Well, let's just say Mr. Johnson decided to have a little dinner party, and I found myself preparing a feast with the leftover dishes. Quite the surprise, I must say."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "That does sound surprising! But I hope it went well."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "It did, thanks to some quick thinking. And now, I'm here, enjoying my evening run."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "You seem to handle everything with ease. It's admirable."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Thank you. Sometimes, you've got to adapt, right? How about your day? Anything exciting?"

                    if myrandom == 3:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sally, great to bump into you again. How was your day?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Hello! My day was busy but rewarding. I was working on the garden at Mr. Johnson's mansion. You wouldn't believe how many different types of plants he has!"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sounds like quite the garden. Do you enjoy working with plants?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, I love it. Being outdoors, tending to the garden, it's therapeutic for me. Plus, it's a nice change of pace from the regular chores."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "That does sound therapeutic. You must have a green thumb."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "I'd like to think so! And now, I'm just winding down with a run along this beautiful promenade."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Well, it's a pleasure to share this evening with you. How about you? How was your day?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally  (returning the warmth) "Likewise! My day was good, thanks for asking. It's always nice to chat."
                    $ sallyhello = 2
                    
                    $ myrandom = renpy.random.randint(1,3)
                    if myrandom == 1:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "My day was quite eventful, too, Sally. I explored more of the town, had a nice chat with some friendly locals, and even visited the beach during the afternoon. It's been a great day, and now, running into you here makes it even better."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "I'm glad to hear that. This town does have its charm, and it's wonderful to make new friends along the way."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Absolutely, Sally. Meeting people like you and getting to know the community here is what makes this place feel like home. Well, I should get going now. Have a fantastic evening!"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "You too. Take care!"

                    if myrandom == 2:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "My day was pretty laid-back, Sally. I decided to take it easy, strolled around the park for a while, and just enjoyed the peacefulness of this place. Seeing the sunset by the sea is always a highlight."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Sunsets here can be breathtaking. It's a perfect way to unwind and reflect on the day."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Exactly, Sally. Sometimes, it's the simple things that make life beautiful. Well, it's getting late, and I should head home. Have a wonderful night!"

                        

                    if myrandom == 3:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Well, Sally, my day had its ups and downs. Work was a bit hectic, but I managed to meet some interesting people and learned more about the town's history from Kira at the bar. Now, being here and catching up with you is definitely a highlight."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Kira's a good source for local stories. You'll find plenty of intriguing tales about this place."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "I'm looking forward to it. And speaking of stories, have you had any memorable moments today?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, not really, just the usual. Anyway, I should get back home now. Take care, and see you around!"
                        
                    

                    
                if sallyhello == 0:
                    $ myrandom = renpy.random.randint(1,3)
                    if myrandom == 1:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Hey there! Enjoying the evening by the sea?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Hi! Yes, it's so peaceful here. I just finished my duties at Mr. Johnson's mansion. You must be new in town, right?"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Yeah, I am. Just moved here recently. I'm [name], by the way."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Nice to meet you. I'm Sally, and I work as a maid at Mr. Johnson's mansion."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Pleasure to meet you, Sally. Working in a mansion must be quite an experience."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "It has its moments, that's for sure. Mr. Johnson can be quite particular about things, but the pay is good, and the mansion is lovely. What brings you to our town?"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Well, I'm a cook, and I heard there are some great places to eat around here. Figured I'd give it a shot."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, that's great! We do have some fantastic eateries. You should try the seafood at the Seashell Grill. It's a local favorite."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Thanks for the recommendation, Sally. I'll make sure to check it out."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "You're welcome. If you ever need anything or have any questions about the town, feel free to ask. We're a friendly community here."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "I appreciate that, Sally. It's nice to know I've got a friendly neighbor to show me the ropes."


                    if myrandom == 2:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Hey there! Enjoying the evening by the sea?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Hi! Yes, it's so peaceful here. I just finished my shift. You're new in town, right?"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Yeah, I am. Just moved here recently. I'm [name], by the way."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Nice to meet you. I work as a maid in one of the mansions along the coast."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Pleasure to meet you, Sally. Must be interesting working in one of those big houses."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "It has its moments. Some of those mansions are like something out of a movie. What about you? What brings you to our little town?"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        player "Well, I'm a cook, and I heard there are some great places to eat around here. Figured I'd give it a shot."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, that's awesome! We definitely have some fantastic eateries. You should try the seafood at the Seashell Grill. It's a local favorite."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg

                        player "Thanks for the tip, Sally. I'll make sure to check it out."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "No problem at all. If you ever need any recommendations or anything else, just let me know. We're a close-knit community, and we look out for each other here."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg

                        player "I appreciate that, Sally. It's nice to know I've got a friendly neighbor."


                    if myrandom == 3:
                        $ position = "arksallybencheveninglistening"
                        call sceneimg
                        player "Hey there! Enjoying the evening by the sea?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Hi! Yes, it's so peaceful here. I just finished my work at Mr. Johnson's mansion. You're new in town, right?"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Yeah, I am. Just moved here recently. I'm [name], by the way."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Nice to meet you. I'm Sally. I work as a maid at Mr. Johnson's mansion."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Pleasure to meet you, Sally. Must be interesting working in a place like that."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "It has its moments, for sure. Mr. Johnson is quite particular about things. What about you? What brings you to our little town?"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Well, I'm a cook, and I heard there are some great places to eat around here. Figured I'd give it a shot."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, that's awesome! We definitely have some fantastic eateries. You should try the seafood at the Seashell Grill. It's a local favorite."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Thanks for the tip, Sally. I'll make sure to check it out."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "No problem at all. If you ever need any recommendations or anything else, just let me know. We're a close-knit community, and we look out for each other here."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "I appreciate that, Sally. It's nice to know I've got a friendly neighbor."
                    $ sallyhello = 1
            
                


            "Ask her how she became a maid?" if sallyjob == 0 and (sallyhello == 1 or sallyhellotoday == 1):               
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "Sally, if you don't mind me asking, how did you end up becoming a maid for Mr. Johnson? It seems like quite a unique profession."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Oh, it's a bit of a story, really. I moved to this town a few years ago, and I was looking for work to make ends meet. I happened to come across a job listing for a maid position at the Johnson mansion."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "And what made you decide to give it a try?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Well, I've always been organized and meticulous, and the idea of working in such a grand place intrigued me. So, I applied, had an interview with Mr. Johnson, and he offered me the job."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "That's quite an interesting turn of events. I guess sometimes life takes you on unexpected journeys."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "You're absolutely right. I never would've thought I'd end up here, but I've grown to appreciate the work. It's not just about cleaning; it's about maintaining a sense of order and comfort for Mr. Johnson and his guests."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "It sounds like you take a lot of pride in what you do, Sally. That's admirable."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Thank you. It's been a pleasure chatting with you about my work. If you ever have more questions or want to know more about life in the mansion, don't hesitate to ask."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "I'll keep that in mind, Sally. Thanks for sharing your story with me."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "You're welcome. It's always nice to have a friendly neighbor to talk to."
                $ sallyjob = 1

            "Ask her does she like the job?" if sallyjob == 1:
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "Sally, I'm intrigued by your work as a maid. Do you enjoy being a maid for Mr. Johnson?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Well, it has its moments. There's a sense of satisfaction in keeping everything tidy and organized, and I get to see a glimpse of the more luxurious side of life. But it's not without its challenges too."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "Challenges? What kind of challenges do you face in your job?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Sometimes, Mr. Johnson hosts lavish parties and events at the mansion, and that means a lot of extra work to make sure everything is perfect. Plus, the mansion is pretty big, so it can be physically demanding at times."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "I can imagine that must be tough. But it sounds like you handle it well."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Thank you. I do my best. And I've also learned a lot about the finer details of maintaining a beautiful home, which I find quite fulfilling."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "It's great to hear that you find fulfillment in your work. That makes all the difference."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Yes, it does. And I appreciate your interest and understanding. If you ever have more questions or want to chat about anything else, feel free to ask."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "Absolutely, Sally. I'm always up for a good conversation. Thanks for sharing your thoughts with me."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "My pleasure. It's nice to have a friendly neighbor to talk to."
                $ sallyjob = 2


            "Ask her if the job is paid well?" if sallyjob == 3:
                menu:
                    "She answers":
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sally, I hope you don't mind me asking, but is being a maid a well-paying job?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Well, it's not bad, but it's not exceptionally high-paying either. I earn a decent wage, and Mr. Johnson is a fair employer when it comes to compensation."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "That's good to hear. It's important to be fairly compensated for the work you do."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "I agree. And I also have job security, which is valuable. Plus, the experience I gain here can open up doors to other opportunities in the future."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "It's great that you're looking at the bigger picture, Sally. Job security and future prospects are certainly important considerations."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg   
                        Sally "Thank you. I'm content with where I am for now. And who knows, maybe one day, I'll pursue my dreams outside of this profession."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "That sounds like a positive outlook. Whatever you decide to do, I'm sure you'll excel at it."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "I appreciate your kind words. If you ever have more questions or want to chat, feel free to ask anytime."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "I definitely will, Sally. It's been nice getting to know you."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Likewise. Have a wonderful day!"
                        $ sallyjob = 4
                    "Let's skip this question":
                        "Why do you ask such things? Do you want to talk about something else?"
                        $ sallyjob = 4

            "Ask her about her duties?" if sallyjob == 2:
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "Sally, I'm intrigued about your job as a maid. Could you tell me more about your daily duties?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Of course. My typical day involves various tasks to ensure Mr. Johnson's home is clean and comfortable. I start by cleaning and tidying up the living spaces, dusting, and vacuuming."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "That sounds thorough. What else do you do?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "I also handle laundry, washing and ironing clothes and linens. And I make sure the bathrooms and kitchen are spotless. Sometimes, I assist in meal preparations and serve at dinner parties."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "It sounds like you have quite a range of responsibilities. How do you manage it all?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Well, it's all about good organization and attention to detail. I've developed a routine that helps me efficiently complete my tasks each day."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "It sounds like you're very dedicated to your work, Sally. Mr. Johnson is lucky to have you."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Thank you. I take pride in what I do, and it's important to me that the household runs smoothly."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "That's evident, Sally. Keep up the good work, and if you ever need any assistance or have questions, don't hesitate to reach out."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "I will. It's been nice chatting with you. If you ever want to know more or just have a friendly conversation, feel free to stop by."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "I'll definitely do that, Sally. Have a wonderful day!"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "You too. Take care!"
                $ sallyjob = 3


            "Ask her about her employer" if sallyjob == 4:
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "Sally, you mentioned Mr. Johnson is a good employer. Can you tell me more about him?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Certainly. Besides being a good employer, Mr. Johnson is a remarkably caring man. He genuinely looks out for the well-being of his employees."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "That's quite admirable. How does he show his care and support?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Well, for one, he ensures that we have a safe and comfortable working environment. He values our input and often checks in to see if we need anything to make our jobs more manageable."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "It's rare to find employers who are so considerate. What kind of things has he done for his employees?"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "He's provided additional training opportunities to help us grow professionally. He also offers fair compensation and benefits. Plus, he fosters a sense of community among his staff, which I really appreciate."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "It sounds like Mr. Johnson goes above and beyond to make sure his employees are well taken care of."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Yes, he does. It makes working for him a rewarding experience. I feel fortunate to be part of his team."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "That's wonderful to hear, Sally. I hope your positive work environment continues to flourish."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Thank you. It's been great chatting with you. If you ever need assistance or just want to talk, feel free to reach out."
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player "I'll keep that in mind, Sally. Have a fantastic day!"
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "You too. Take care!"

                $ sallyjob = 5


                
            "Ask her how her day goes usually?" if sallyjob == 5:
                if sally_fullstage < 4:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sally, I've been wondering, what does a typical day look like for you working here for Mr. Johnson?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Well, my day usually starts early in the morning. I go for a refreshing run to get some exercise and clear my mind before work. Then, I make sure the mansion is spotless before anyone wakes up. That means cleaning, dusting, and tidying up every room."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That sounds like a lot of work."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It can be, but I'm used to it. After the cleaning, I prepare breakfast for everyone in the household. Mr. Johnson insists on a hearty breakfast for his family and staff."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "What happens after breakfast?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "After breakfast, I help Mrs. Johnson with any errands or tasks she needs assistance with. Sometimes it's grocery shopping, organizing, or managing the household chores. She's a lovely woman, and we work well together."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "It sounds like you have a close relationship with the Johnsons."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Yes, they've been wonderful employers. Mr. Johnson is especially caring. He makes sure we all have enough to eat and that we're comfortable working here."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That's really considerate of him."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It is. And in the evenings, after work, I take a leisurely walk in the park to unwind. It's a beautiful place to relax and reflect."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "It sounds like you stay busy, but it's good to hear that you're well taken care of."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Yes, I can't complain. It's been a rewarding experience working here."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Well, Sally, it's been great getting to know you a bit better. Thanks for sharing a glimpse of your daily routine."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "You're welcome. If you have any more questions or ever want to chat, feel free to reach out."
                    
                if sally_fullstage > 3 and sally_fullstage < 8:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sally, I've been wondering, what does a typical day look like for you working here for Mr. Johnson?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Well, my day usually starts early in the morning. I go for a refreshing run to get some exercise and clear my mind before work. Then, I make sure the mansion is spotless before anyone wakes up. That means cleaning, dusting, and tidying up every room."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That sounds like a lot of work."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It can be, but I'm used to it. After the cleaning, I prepare breakfast for everyone in the household. Mr. Johnson insists on a hearty breakfast for his family and staff."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "What happens after breakfast?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "After breakfast, I help Mrs. Johnson with any errands or tasks she needs assistance with. Sometimes it's grocery shopping, organizing, or managing the household chores. She's a lovely woman, and we work well together."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "It sounds like you have a close relationship with the Johnsons."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Yes, they've been wonderful employers. Mr. Johnson is especially caring. He makes sure we all have enough to eat and that we're comfortable working here."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sally, I hope you don't mind me asking, but I've noticed your belly looks quite round. Are you...?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Oh, no, I'm not pregnant. It's just that Mr. Johnson insists we eat well, and I find it hard to resist his delicious meals. I guess I'm just well-fed."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Ah, I see. Well, it's good to know you're well taken care of. And I'm sure Mr. Johnson appreciates all the hard work you do around here."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Yes, he does. And thank you for your concern. If you have any more questions or ever want to chat, feel free to reach out."

                if sally_fullstage > 7:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sally, I've been wondering, what does a typical day look like for you working here for Mr. Johnson?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Well, my day usually starts early in the morning. I go for a refreshing run to get some exercise and clear my mind before work. Then, I make sure the mansion is spotless before anyone wakes up. That means cleaning, dusting, and tidying up every room."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That sounds like a lot of work."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It can be, but I'm used to it. After the cleaning, I prepare breakfast for everyone in the household. Mr. Johnson insists on a hearty breakfast for his family and staff."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "What happens after breakfast?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "After breakfast, I help Mrs. Johnson with any errands or tasks she needs assistance with. Sometimes it's grocery shopping, organizing, or managing the household chores. She's a lovely woman, and we work well together."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "It sounds like you have a close relationship with the Johnsons."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Yes, they've been wonderful employers. Mr. Johnson is especially caring. He makes sure we all have enough to eat and that we're comfortable working here."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sally, I hope you don't mind me asking, but your belly looks quite round today. Are you...?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Oh, no, I'm not pregnant. Today was a dinner party, and I may have indulged in a bit too much. Leftovers are hard to resist."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "I see! Well, dinner parties can be quite tempting. I'm glad to hear it's not what I thought."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Thanks for understanding. If you have any more questions or ever want to chat, feel free to reach out."

                $ sallyjob = 6

            "Ask her about her belly?" if sallyjob > 5 and sally_fullstage > 3:
                if sally_fullstage > 3 and sally_fullstage < 8:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sally, I couldn't help but notice that your belly looks quite full tonight. Have you been enjoying some good meals recently?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Oh, you've got a keen eye, [name]. You're absolutely right. My employer makes sure we eat well, and sometimes, it shows."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That sounds wonderful, actually. What kind of meals does your employer prepare for you?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "He's a fantastic cook, I must admit. We have a variety of dishes—roasts, pastas, homemade desserts. He believes in hearty, home-cooked meals."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "He must be quite the chef. It's not every day you find an employer who cares so much about their staff's well-being."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "I'm really lucky in that regard. He's not just my employer; he's like family. And he insists we all eat together."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That's a wonderful tradition. Food has a way of bringing people closer."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It sure does. So, yes, my full belly is a testament to his generosity in the kitchen."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Well, it's great to see someone appreciate good food. Enjoy your evening, Sally."

                

                if sally_fullstage > 7:
                    $ myrandom = renpy.random.randint(1,2)
                    if myrandom == 1:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sally, forgive me for being forward, but your belly seems quite round. Are you... expecting?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, no, nothing like that. I can see why you might think so, though. It's just that I had a rather indulgent dinner party tonight. Leftovers and all that."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Leftovers? You mean you ate all that food tonight?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Well, when my employer hosts a dinner, he doesn't believe in small portions. I may have gotten carried away."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Hey, no judgment here. We all have our moments of culinary weakness. What was on the menu, if you don't mind me asking?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, it was a bit of everything—roast chicken, lasagna, pies, and a variety of desserts. It was like a feast!"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sounds delicious. It's hard to resist a spread like that."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Exactly! So, no baby on the way, just a satisfied stomach."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Well, it's good to hear. Thanks for clearing that up, Sally."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "No problem at all, [name]. Now you know the secret behind my round belly tonight."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Thanks for sharing, Sally. Have a great evening!"

                    

                    if myrandom == 2:
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Hey, Sally, I hope you don't mind me asking, but I couldn't help but notice your belly. It looks pretty round. Is there something special about it?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, you noticed, huh? Well, it's just that I had a rather hearty dinner tonight. My employer decided to throw a little feast, and, well, I may have indulged a bit."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Ah, I see. Feasts can be hard to resist sometimes, especially when someone else is doing the cooking. So, what was on the menu?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "It was a bit of everything, really. Roast chicken, pasta, pies, and dessert galore. My employer insists that we all eat well, and he's quite generous with his portions."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Well, it sounds like you had a feast indeed. Sometimes, a good meal is just what we need to unwind."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Exactly, [name]. And after a long day, it's hard to say no to a delicious dinner."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "No judgment here, Sally. We all deserve to treat ourselves once in a while. If you enjoyed it, that's what matters."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Thanks for understanding, [name]. It's been a pleasure chatting with you. I hope you have a wonderful evening!"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "You too, Sally! Take care, and see you around!"

                    
                    
            "Ask Sally if she likes to eat" if sallyjob == 6:
                
                menu:
                    "Yes":
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sally, I've noticed that you're often enjoying some delicious food. Do you really like to eat?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Oh, absolutely! I do enjoy good food. Mr. Johnson insists that we all have satisfying meals here, and I'm grateful for it. Food has a way of bringing people together, don't you think?"
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "It certainly does. It's nice to have an employer who cares about your well-being."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Yes, it truly is. Food is not just about nourishment; it's about comfort and connection. Plus, it's a wonderful way to explore different flavors and cultures."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "I couldn't agree more! Food can be an adventure in itself. Have you tried any particularly exciting dishes recently?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Well, we had a special event last week, and there were some exquisite dishes on the menu. I got to try a delightful seafood paella that was absolutely mouthwatering."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Seafood paella sounds amazing. It must be a perk of working here to enjoy such delicious meals."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "It definitely is. And it's not just about the food; it's about creating memorable moments and savoring life's pleasures."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "That's a wonderful way to look at it, Sally. Enjoying good food and good company is what life is all about."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "I couldn't agree more. If you ever want to join me for a meal or chat about food, you're always welcome."
                        $ sallylovesfood = 1

                    "No":
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Sally, I've noticed that you seem to enjoy your meals. Do you really like to eat?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Well, not particularly. It's not that I don't like food, but it's more about Mr. Johnson's insistence that all the employees have hearty meals. I don't want to disappoint him."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Ah, I see. So it's more about keeping your employer happy?"
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Yes, exactly. Mr. Johnson is quite caring, and he believes that good food is essential for everyone's well-being. So, I oblige to maintain a positive work environment."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "That makes sense. It's nice that he looks out for his employees' welfare."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Yes, it is. And it's not that I don't appreciate a good meal now and then. It's just that my appetite isn't as big as it might seem."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "Well, it's essential to keep a harmonious workplace. I respect your dedication to your job."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "Thank you. It's not always easy, but it's all part of the job."
                        $ position = "parksallybencheveninglistening"
                        call sceneimg
                        player "If you ever need someone to share a meal with or just chat, I'm here."
                        $ position = "parksallybencheveningtalking"
                        call sceneimg
                        Sally "I appreciate that, and I might take you up on the offer someday."

                        
                        $ sallylovesfood = 0
                $ sallyjob = 7

            "Ask her if she loves running?" if sallyjob == 7:    
                if sallylovesfood == 0:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player " Sally, I noticed you mentioned your morning runs. Do you enjoy running?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Not really, to be honest. It's more of a necessity. You see, Mr. Johnson, my employer, is quite insistent on his employees staying in good shape. He believes it helps with our overall well-being."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    
                    player "Ah, I see. So, you do it to keep yourself fit and healthy?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Exactly. It's not my favorite activity, but I don't want to disappoint him. He's a very caring man and looks after his employees' well-being, even if it means morning runs."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg

                    player "That's quite dedicated of you to keep up with it despite not being a fan."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Well, we all have our obligations, don't we? It's a small price to pay for the job security and care he provides."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg

                    player "I can see that. It's important to do what's necessary sometimes."

                if sallylovesfood == 1:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    
                    player " Sally, do you enjoy running? I noticed you mentioned your morning runs."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Oh, I do! I find it quite refreshing. To be honest, I try not to do anything I don't enjoy."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg

                    player "That's a great way to live, doing what you love."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "I think so too. Life's too short to spend it doing things you don't find joy in. Running in the morning helps me start the day on the right foot."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg

                    player "It's fantastic that you prioritize your happiness and well-being."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Thank you. It's something I've learned over time. How about you? Do you have any hobbies or activities that you're passionate about?"
                    $ position = "parksallybencheveninglistening"
                    call sceneimg

                    player " (sharing) Well, I do enjoy cooking. It's my profession, and it's something I've always loved."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Cooking, you say? That's wonderful! You must be quite skilled in the kitchen."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg

                    player " (modest) I like to think so. Maybe someday, I'll get the chance to prepare a meal for you."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "I'd look forward to that. It sounds like a delightful idea."
                $ sallyjob = 8
            "Tell her about yourself" if sallyjob > 6 and sallytellyourself == 0:
                $ sallyhowstheday = 1
                $ position = "parksallybencheveninglistening"
                call sceneimg
                player " Speaking of obligations and responsibilities, I recently moved to this town. I'm actually a cook by profession. It's been quite an adjustment getting used to everything here."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "A cook? That's fascinating! What brought you to our town, if you don't mind me asking?"
                $ position = "parksallybencheveninglistening"
                call sceneimg

                player "Well, I was looking for a fresh start, and this town seemed like a peaceful and welcoming place. I'm still exploring the area and trying to settle in."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "It sounds like you're on a journey of your own. If you ever need any help or advice about the town, feel free to ask. We're a friendly community here."
                $ position = "parksallybencheveninglistening"
                call sceneimg

                player "Thank you, Sally. I appreciate that. It's been great getting to know you, and I look forward to becoming more acquainted with the town and its people."
                $ position = "parksallybencheveningtalking"
                call sceneimg
                Sally "Likewise. We're here to support each other, so don't hesitate to reach out if you need anything."

                
                $ sallytellyourself = 1
            
            
            "How was your day today?" if sallyhowstheday == 0 and sallyjob > 6:
                $ sallyhowstheday = 1
                $ sally_calories += 10000
                $ notify_success("Sally +10000 calories")
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Hey, Sally! How was your day today?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Oh, it was pretty eventful, actually. I started with my morning run, of course. It was a bit windy, but I enjoy the challenge."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That sounds great. What else did you do today?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Well, today was quite a day. After my run, I spent a busy morning at work, taking care of Mr. Johnson's mansion."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "What tasks were you handling today?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Today, I focused on deep cleaning the mansion's grand entrance and staircase. It's quite a sight when it's spotless."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sounds like a lot of responsibility."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It is, but I'm used to it now. Anyway, after work, I decided to enjoy the evening at the park, watching the sunset over the sea. It's so peaceful."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That does sound peaceful. And it's a great way to unwind after a long day."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Indeed it is. How about you? How was your day today?"

                if myrandom == 2:
                    player "Hey, Sally! How's your day been?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Hello! Well, today was quite productive. I started with my usual morning run, which always energizes me."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Nice! What else did you do today?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "After my run, I headed to Mr. Johnson's place to take care of some cleaning tasks. Today, I focused on the large windows; they need to be sparkling clean, you know."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That sounds like a meticulous job."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It can be, but I take pride in keeping the mansion looking its best. After work, I went to the park and watched the sunset by the sea. It's so calming."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sounds like a lovely way to end the day."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It truly is. How about you? How was your day today?"

                if myrandom == 3:
                    player "Hey, Sally! How's your day been?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Hello! Today was quite a day. I kicked it off with my morning run, which always sets a positive tone."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sounds like a great start. What else did you do today?"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Well, after my run, I headed to Mr. Johnson's place. Today, my focus was on giving the mansion's grand entrance a thorough cleaning. Those marble floors are a beauty when they're polished."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "That must be a lot of work."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It can be, but I enjoy it. Later, I went to the park to catch the sunset by the sea. It's my favorite way to relax."
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Watching the sunset sounds lovely."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "It truly is. Now, how about you? How was your day today?"
            
            
            
            
            
            
            
            
            
            
            
            
            "I need to go":
                $ myrandom = renpy.random.randint(1,2)
                if myrandom == 1:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Alright, Sally, I'll let you get back to your evening. Take care!"
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "Thanks. Have a great night!"
                    jump culinarychoices

                if myrandom == 1:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Well, it's been nice chatting with you, Sally. Enjoy the rest of your evening."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "You too. Until next time!"
                    jump culinarychoices

                if myrandom == 1:
                    $ position = "parksallybencheveninglistening"
                    call sceneimg
                    player "Sally, it's been a pleasure talking to you. I hope you have a wonderful evening."
                    $ position = "parksallybencheveningtalking"
                    call sceneimg
                    Sally "You too. Thanks for the company. See you around!"
                    jump culinarychoices
        jump eveningsallytalk         



    label morningsallytalk:
        menu:
            "Say hello" if sallyhellotoday == 0:         
                if sallylovesfood == 0:
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    
                    player "Hey, Sally! Fancy meeting you here at the park."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Oh, hello there! Nice to see you too. Just getting in my morning run. How's your day starting?"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Off to a good start, seeing you here. I try to keep up with my own morning routine. So, you're quite the early riser, huh?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Yep, I find it's the best time to squeeze in some exercise before the day gets busy. Plus, the view of the sea in the morning is just breathtaking."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg

                    player "I can't argue with that. It's a beautiful place for a run. By the way, do you run here every day?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Well, most days, yes. But I mix it up sometimes with a walk in the evening."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Sounds like a good balance. Do you enjoy running?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Honestly, not as much as I'd like. But staying active is essential, especially with the kind of work I do."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Oh, I see. So, it's not just about enjoying it but also about staying fit?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "You got it. Mr. Johnson, my employer, insists on all his employees being in good shape and taking care of their health."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "That's considerate of him. I guess it's a way to ensure everyone's well-being."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Yes, he's a caring man, looking out for us in more ways than one."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Well, Sally, keep up the fantastic work. I'll let you get back to your run. See you around!"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Thanks. Have a great day!"


                if sallylovesfood == 1:
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Hey, Sally! Looks like you're really enjoying your run today."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Oh, hi there! You bet I am. There's something about the sea breeze and the sound of the waves that makes running here pure bliss."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "I can't argue with that. It's a stunning view. Do you come here every morning?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Almost without fail! I just can't resist starting my day like this. It's invigorating."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Your enthusiasm for it is contagious. I've been trying to stick to my morning routine too, but I have to admit, it's not always easy."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Well, you're here now, right? That's what counts. Keep at it, and it'll become a habit."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Thanks, Sally. I appreciate the motivation. By the way, do you have any tips for someone like me trying to get into the routine of morning runs?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Absolutely! One tip I'd give is to set achievable goals. Start with shorter runs and gradually increase your distance. And remember, consistency is key."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "That makes sense. I'll keep that in mind. Thanks for the advice."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "No problem. If you ever need a running buddy or more tips, you know where to find me."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "I might take you up on that offer one day. Enjoy the rest of your run, Sally!"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "You too! Have a great day!"
                $ sallyhellotoday = 1
            
            
            "Chat a little and say goodbye":
                $ myrandom = renpy.random.randint(1,2)
                if myrandom == 1:

                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Good morning, Sally! How's your day starting off?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Morning! It's off to a great start. Can't complain with this view."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "You've got that right. The sea always looks so peaceful in the morning. How far are you planning to run today?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Oh, I'm thinking of doing a few extra laps today. Helps me clear my head and stay energized."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Sounds like a good plan. Running can be so refreshing. By the way, how's work been treating you?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Work's been busy as usual, but Mr. Johnson's been kind enough to give me some time off in the evenings. I've been enjoying the park and the sea breeze."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "That's great to hear. Mr. Johnson seems like a considerate employer. And it's nice that you get to unwind like this. Any exciting plans for the rest of the day?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Well, I've got some errands to run and a bit of housework to catch up on. Then, it's back to the usual routine. How about you? Any plans for your day?"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Not much on the agenda, to be honest. I might explore the town a bit more or hit the local burger cafe for lunch. If you ever want to join me for a meal or a chat, feel free to give me a shout."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "That's very kind of you. I'll keep that in mind. Enjoy the rest of your run, and have a wonderful day!"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "You too, Sally! Take care out here."

                if myrandom == 2:
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Hey there, Sally! You're always up and running early, huh?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "You know it. Gotta seize the day!"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "I admire your dedication. Morning runs can be so invigorating. How do you manage to keep this routine?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "It's become a habit, really. Plus, with this fantastic view, who could resist?"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "You're absolutely right. The ocean has a way of making everything better. So, what's on your schedule for the day after this?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Well, I'll head home after this and do some chores. Then, I've got a few hours off before work. Might take a stroll in the park or relax with a book."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Sounds like a balanced day. And how's work been lately?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Work's been busy, but I can't complain. Mr. Johnson is a good employer, and I appreciate that he values his employees' well-being."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "That's wonderful to hear. Having a caring employer can make a big difference. If you ever want to grab a coffee or just chat, feel free to reach out."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Thanks. I'll keep that in mind. Enjoy your run, and have a great day!"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "You too, Sally! Take care."

                if myrandom == 3:
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Sally, morning! You're already in your element."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Good morning. Nothing like a run to kickstart the day."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "I couldn't agree more. The sea looks amazing today. How's your run going so far?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "It's been good, a nice way to clear my mind. Do you run here often?"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Yeah, it's become a regular routine for me. Helps me stay active and focused. So, how's life outside of jogging?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Life's been all right, work keeps me busy, but I enjoy my job. Mr. Johnson is quite considerate, and I'm grateful for that."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "It's always good to have a supportive employer. Anything exciting planned for the rest of the day?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Just some errands and a bit of relaxation. Maybe a walk in the park later. How about you? Any plans?"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Not much on my plate today. Might explore the town a bit or grab a bite to eat. If you ever want to join me for lunch or a chat, you know where to find me."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Thanks. I appreciate the offer. Enjoy the rest of your run, and have a wonderful day!"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Same to you, Sally! Stay well."
                jump culinarychoices
            "Ask her about her belly" if sally_fullstage > 2:
                if sally_fullstage > 0 and sally_fullstage < 4:
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Sally, I couldn't help but notice, even in the morning, your belly isn't exactly flat. Is there a reason for that?"
                    $ position = "sallymorningseaviewbellyholding"
                    call sceneimg
                    Sally "Oh, that... Well, it's just the way my body is, I suppose. I've always had a bit of a rounded tummy, even when I'm not full."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Ah, I see. Well, you look great, regardless. It's just something I noticed."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Thank you. You're too kind. It's all the more reason for me to keep up with my running, I guess!"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Well, you're doing a great job at it. Keep it up, Sally!"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "I will, and thanks for not making it awkward. Have a wonderful day!"
                if sally_fullstage > 3 and sally_fullstage < 8:
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Sally, I couldn't help but notice, even in the morning, your belly looks quite nicely rounded. Is there a specific reason for that?"
                    $ position = "sallymorningseaviewbellyholding"
                    call sceneimg
                    Sally "Oh, you're observant, aren't you? Well, it's because I tend to eat quite a bit, especially during the evenings. I love food, and it seems my belly decides to stick around in the morning as a reminder."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "That's completely understandable. Food is a wonderful thing to enjoy. Plus, it's nice to have a little reminder of a good meal, right?"
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Exactly! And it's not something that bothers me. Life's too short to worry about having a perfectly flat belly all the time."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "You're absolutely right, Sally. Embracing who you are is important. Keep enjoying your meals and your runs in the morning."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Thanks. It's been nice talking to you. Have a fantastic day!"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "You too, Sally. Take care!"

                if sally_fullstage > 7:
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Sally, I couldn't help but notice, even in the morning, your belly looks like you're 7-9 months pregnant. What happened?"
                    $ position = "sallymorningseaviewbellyholding"
                    call sceneimg
                    Sally "Oh, that! Well, yesterday, I indulged in so much food that I thought I'd pop. My belly just decided to hang around this morning as a reminder. But don't worry, it's empty now, so it doesn't hinder my morning run."
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "I see! You must have had quite the feast. It's impressive how your belly can handle all that."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "You have no idea. Sometimes, indulging in a good meal is just too tempting to resist. But hey, it's all part of enjoying life, right?"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "Absolutely! As long as you're comfortable and happy, that's what matters. Plus, it's always nice to have a good story about your belly."
                    $ position = "parksallyseaviewmorningtalking"
                    call sceneimg
                    Sally "Thanks. It's been nice talking to you. Have a fantastic day!"
                    $ position = "parksallyseaviewmorninglistening"
                    call sceneimg
                    player "You too, Sally. Take care and enjoy your morning run!"
            
    jump morningsallytalk