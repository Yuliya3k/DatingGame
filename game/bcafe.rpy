label bcafe:
    call closescreens
    $ calendar.AddMinutes(20)
    # $ alexa_fullness = 3000
    $ alexa_fullness = renpy.random.randint(0,4000)
    $ alexa_calories += renpy.random.randint(0,500)
    # "Alexa fullness [alexa_fullness]"
    
    # "Alexa fullstage [alexa_fullstage]"
    # "ALexa imgindex [alexaimgindex]"
    # "Alexa weightstage [alexa_weightstage]"
    # $ renpy.movie_cutscene("videos/avabeachaftersurfingfrontstand10.webm")
    # $ renpy.movie_cutscene("videos/avabeachsurtlisten1.webm")

    if alexafirsttime == 0:
        play music "audio/streetquiet.mp3" volume 0.5
        $ position = "cafeenterance"
        call sceneimg
        #if speech == 1:        
        #    play sound "audio/Waren-1946580.mp3"
        player "My first week in the city I wandered into a busy fast food cafe. It was the kind of place where counter orders turn into hot meals in seconds."
        play music "audio/bcafe.mp3" volume 0.5
        
        $ position = "alexaworking"
        call sceneimg
        #if speech == 1:        
        #    play sound "audio/Waren-1946584.mp3"
        player "The smell of burgers and fries hit me like a warm hug. I spotted the Classic Cravings Burger and met my server Alexa whose energy was contagious."
        $ alexafirsttime = 1
    else:
        pass    
    play music "audio/bcafe.mp3" volume 0.5

    if avaintro == 1 and (calendar.Hours < 9 or calendar.Hours > 17) and ava_fullstage < 10:
        $ myrandom = renpy.random.randint(1,5)
        if myrandom == 3:
            $ avafirstmeet = 1
            $ avabcafe = 1
            $ position = "cafeenteranceavaalexafar"
            call sceneimg
            pause 3.0
            menu:
                "Approach Alexa to order":
                    pass
        else:
            pass
    else:
        pass

    $ position = "alexaexplaining"
    call sceneimg
    #if speech == 1:        
    #    play sound "audio/Kayla-1946726.mp3"
    Alexa "Welcome to Crave Bites. What can I get for you today?"

    menu:
        "Not hungry right now":
            $ position = "alexasurprised"
            call sceneimg
            #if speech == 1:        
            #    play sound "audio/Waren-1946602.mp3"
            player "Actually I think I will pass this time."
            $ position = "alexahappy"
            call sceneimg
            #if speech == 1:        
            #    play sound "audio/Kayla-1946736.mp3"
            Alexa "No problem. Come back anytime."
            jump culinarychoices  

        "Order the Classic Cravings Burger":
            $ position = "alexahappy"
            call sceneimg
            #if speech == 1:        
            #    play sound "audio/Waren-1946608.mp3"
            player "I will have the Classic Cravings Burger and a frappe please."
            $ position = "alexaworking"
            call sceneimg
            #if speech == 1:        
            #    play sound "audio/Waren-1946611.mp3"
            $ moneytoadd = -15
            call moneynotification
            if notenoughmoney == False:
                player "Alexa punched in my order and gave me a friendly smile. I grabbed a seat by the window and watched the city stir."
                
                $ position = "foodburgerfrappe"
                call sceneimg
                #if speech == 1:        
                #    play sound "audio/Waren-1946615.mp3"
                player "The first bite was pure bliss - juicy, crispy, and just the right kick of sauce. I savored every mouthful."
                
                if avabcafe == 1:
                    $ position = "cafeavasitting"
                    call sceneimg
                    player "Nearby a woman in a leather jacket ate with fierce delight. Her confident bite told its own story."
                    $ fullnesschange = renpy.random.randint(200,600)
                    $ nigirlimage = "niava"
                    call fullnesschange
                    pause 0.7
                    $ calorieschange = renpy.random.randint(200,600)
                    $ nigirlimage = "niava"
                    call calorieschange                    
                    call sceneimg

                    $ position = "avawalkingout"
                    call sceneimg
                    player "When she finally left she gave a nod that felt like a challenge - adventure waits around every corner."
                    $ avabcafe = 0
                    $ position = "foodburger"
                    call sceneimg
                    player "I returned to my burger the city humming with possibility."

                $ position = "alexaskingtable"
                call sceneimg
                #if speech == 1:        
                #    play sound "audio/Waren-1946617.mp3"
                player "I told Alexa how amazing the burger was. She beamed clearly proud of her creation."
                $ calendar.AddMinutes(15)
                $ position = "foodnofood"
                call sceneimg
                pause 1

                if alexa_fullstage > 1 and alexa_bloatask == 0:
                    player "At one point I noticed Alexas dress gently stretched over her round belly - soft, unashamed, and strangely captivating."
                    player "I wondered if I should ask; her confidence suggested she would not mind. Maybe a playful compliment would feel natural."

                    menu:
                        "Compliment her confidence":
                            $ calendar.AddMinutes(5)
                            $ alexa_bloatask = 1
                            $ position = "alexasurprised"
                            call sceneimg
                            #if speech == 1:        
                            #    play sound "audio/Waren-1946632.mp3"
                            player "Your joy in food is contagious - the way you carry yourself is beautiful."
                            $ position = "alexaexplaining"
                            call sceneimg
                            #if speech == 1:        
                            #    play sound "audio/Kayla-1946748.mp3"
                            Alexa "Thanks. I believe confidence is the best accessory."
                            $ position = "alexahappy"
                            call sceneimg
                            stop music
                            $ position = "home"
                            call sceneimg
                            
                            player "I left Crave Bites smiling feeling the warmth of new friendships and flavors yet to discover."
                            jump culinarychoices

                        "Let it be":
                            jump culinarychoices
                else:
                    $ position = "home"
                    call sceneimg
                    player "That burger was a perfect welcome to this city - full of warmth and surprises."
                    jump culinarychoices
            else:
                jump bcafe

       
    # if alexafirsttime == 0:
    #     play music "audio/streetquiet.mp3" volume 0.5
    #     $ position = "cafeenterance"
    #     call sceneimg
    #     if speech == 1:        
    #         play sound "audio/Waren-1946580.mp3"
    #     player "As I settled into my new life in the city, my taste buds were eager for adventure. One sunny afternoon, I decided to step into a bustling fast-food cafe near my place. It was the kind of spot where you ordered at the counter, and within moments, your meal would appear, hot and ready."
    #     play music "audio/bcafe.mp3" volume 0.5
        
    #     $ position = "alexaworking"
    #     call sceneimg
    #     if speech == 1:        
    #         play sound "audio/Waren-1946584.mp3"
    #     player "I walked in, and the aroma of sizzling burgers and crispy fries greeted me like an old friend. The menu board overhead displayed an array of options, but one in particular caught my eye - the Classic Cravings Burger. I approached the counter, and a cheerful young woman named Alexa stood ready to take my order."
    #     $ alexafirsttime = 1
    #     if alexafirsttime == 1:
    #         if speech == 1:        
    #             play sound "audio/Waren-1946588.mp3"
    #         player "This is the first time you see Alexa, so I will tell you about her a bit"
    #         if speech == 1:        
    #             play sound "audio/Waren-1946590.mp3"
    #         player "My exploration of the city led me to a bustling fast-food cafe where I met Alexa, a vivacious waitress. She's got an infectious enthusiasm that brightens up even the busiest of days. Though I've just moved here, I can sense a shared passion for food and cooking between us. Alexa and I haven't had a proper conversation yet, but I look forward to visiting the cafe more often and maybe striking up a friendship."
    #         $ alexafirsttime = 2
    # else:
    #     pass    
    # play music "audio/bcafe.mp3" volume 0.5

    # if avaintro == 1 and (calendar.Hours < 9 or calendar.Hours > 17) and ava_fullstage < 10:
    #     $ myrandom = renpy.random.randint(1,5)
    #     if myrandom == 3:
    #         $ avafirstmeet = 1
    #         $ avabcafe = 1
    #         $ position = "cafeenteranceavaalexafar"
    #         call sceneimg
    #         pause 3.0
            
    #         menu:
    #             "Come to Alexa to order":
    #                 pass
    #             # "Sneak peek at the girl that is ordering":
    #             #     $ position = "cafeavaorderingside"
    #             #     call sceneimg
    #             #     pause
    #     else:
    #         pass
    # else:
    #     pass

    # $ position = "alexaexplaining"
    # call sceneimg
    # if speech == 1:        
    #     play sound "audio/Kayla-1946726.mp3"
    # Alexa "Hello, welcome to Crave Bites. What can I get for you today?"
    
    # menu:
    #     "You do not seem to be hungry for now":
    #         $ position = "alexasurprised"
    #         call sceneimg
    #         if speech == 1:        
    #             play sound "audio/Waren-1946602.mp3"
    #         player "Hello! Sorry, not today I've changed my mind"
    #         $ position = "alexahappy"
    #         call sceneimg
    #         if speech == 1:        
    #             play sound "audio/Kayla-1946736.mp3"
    #         Alexa "No worries! Bye!"
    #         jump culinarychoices  
    #     "You order some food":
    #         $ position = "alexahappy"
    #         call sceneimg
    #         if speech == 1:        
    #             play sound "audio/Waren-1946608.mp3"
    #         player "I didn't hesitate. 'I'll have the Classic Cravings Burger, please, with a frappe.'"
    #         $ position = "alexaworking"
    #         call sceneimg
    #         if speech == 1:        
    #             play sound "audio/Waren-1946611.mp3"
    #         player "Alexa's nimble fingers danced across the register keys as she processed my order. She handed me a small receipt and a friendly nod, indicating my meal would be ready shortly. I took a seat by the window, the anticipation building with each passing second."
            
    #         $ position = "foodburgerfrappe"
    #         call sceneimg
    #         if speech == 1:        
    #             play sound "audio/Waren-1946615.mp3"
    #         player "I picked up the burger, its warmth radiating through the paper wrapping. My first bite was an explosion of flavors - the juicy beef, the tangy sauce, the crunch of lettuce - it was a symphony of taste. I couldn't help but savor each bite, sipping on a cold drink that accompanied the meal."
            
            
    #         if avabcafe == 1:
    #             $ position = "cafeavasitting"
    #             call sceneimg
    #             player "As I sat at Crave Bites, savoring every bite of my meal, I couldn't help but notice a newcomer. She was hard to miss, sitting at a nearby table in her leather jacket and shorts combination. Her aura seemed to exude a certain edginess, and I couldn't help but be intrigued."
    #             $ ava_fullness += renpy.random.randint(200,2000)
    #             $ ava_calories += renpy.random.randint(200,2000)
    #             call sceneimg
    #             player "The way she ate her meal with a certain enthusiasm caught my attention. It wasn't just about eating; it was an experience, and she seemed to relish every moment of it. With each bite, her expressions told a story of satisfaction and delight."
    #             $ position = "avawalkingout"
    #             call sceneimg
    #             player "But as quickly as she had arrived, she remained seated until she finished her meal. With a casual nod to the staff, she gathered her belongings and sauntered towards the exit, her leather jacket swinging gently with her every step. There was an air of mystery about her, and I couldn't help but wonder what her story was, where she was headed, and what adventures lay ahead for her."
    #             $ avabcafe = 0
    #             $ position = "foodburger"
    #             call sceneimg
    #             player "I returned my focus to my own meal, but the memory of the girl in the leather jacket lingered in the back of my mind, a fleeting encounter that left me with a sense of curiosity and a reminder that in this city, there were countless stories waiting to be discovered."

    #         $ position = "alexaskingtable"
    #         call sceneimg
    #         if speech == 1:        
    #             play sound "audio/Waren-1946617.mp3"
    #         player "As I enjoyed my burger, Alexa came over to ensure everything was to my liking. I couldn't contain my enthusiasm and praised the burger's deliciousness. She chuckled, clearly pleased, and mentioned that their burgers were a local favorite."
    #         $ calendar.AddMinutes(15)
    #         $ position = "foodnofood"
    #         call sceneimg
    #         pause 1
    #         if alexa_fullstage > 1 and alexa_bloatask == 0:
    #             if speech == 1:        
    #                 play sound "audio/Waren-1946622.mp3"
    #             player "As I sat at my regular spot in Crave Bites, savoring every bite of my Classic Cravings Burger, I couldn't help but notice something unusual. Alexa, the cheerful server who had taken my order and shared a bit of her story, had a noticeably bloated belly. It was hard not to notice, given her usually slender frame."
                
    #             if speech == 1:        
    #                 play sound "audio/Waren-1946623.mp3"
    #             player "Thoughts raced through my mind as I continued to enjoy my meal. Should I ask her if everything's alright? Maybe it's just a minor thing, like overindulging during her break. But what if there's more to it? I didn't want to pry, but I also didn't want her to feel uncomfortable or unwell."

    #             if speech == 1:        
    #                 play sound "audio/Waren-1946627.mp3"
    #             player "As I took another bite of my burger, I decided it wouldn't hurt to inquire gently. Alexa had been friendly, and it felt like the right thing to do, just to make sure she was okay. After all, we were becoming acquaintances, and sometimes a simple question could lead to a meaningful conversation."
                
    #             menu:
    #                 "Ask her about her belly bloat" :
    #                     $ calendar.AddMinutes(5)
    #                     $ myrandom = renpy.random.randint(1,3)
    #                     $ alexa_bloatask = 1
    #                     if myrandom == 1:
    #                         $ position = "alexasurprised"
    #                         call sceneimg
    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946632.mp3"
    #                         player " Alexa, I couldn't help but notice your belly looks quite bloated today. Are you feeling alright?"
    #                         $ position = "alexaexplaining"
    #                         call sceneimg
    #                         if speech == 1:        
    #                             play sound "audio/Kayla-1946748.mp3"
    #                         Alexa " Oh, yeah, it's just a little post-lunch bloat. I tend to indulge a bit too much when it comes to our food."

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946638.mp3"
    #                         player " Well, if it tastes as good as it looks, I don't blame you!"
    #                         $ position = "alexahappy"
    #                         call sceneimg

    #                         if speech == 1:        
    #                             play sound "audio/Kayla-1946753.mp3"
    #                         Alexa " Haha, you've got that right! This place has some irresistible treats."

    #                     if myrandom == 2:
    #                         $ position = "alexasurprised"
    #                         call sceneimg

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946643.mp3"
    #                         player " Alexa, forgive me for asking, but is everything okay? Your belly seems a bit swollen."
    #                         $ position = "alexaexplaining"
    #                         call sceneimg

    #                         if speech == 1:        
    #                             play sound "audio/Kayla-1946768.mp3"
    #                         Alexa " Oh, you noticed that, huh? It's just the aftermath of trying a few too many menu items for quality control."
    #                         $ position = "alexahappy"
    #                         call sceneimg

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946648.mp3"
    #                         player " Quality control, huh? That must be quite the job perk."
                            
    #                         $ position = "alexaexplaining"
    #                         call sceneimg

    #                         if speech == 1:        
    #                             play sound "audio/Kayla-1946776.mp3"
    #                         Alexa " Well, it has its moments, but sometimes my eyes are bigger than my stomach!"

    #                     if myrandom == 3:
    #                         $ position = "alexasurprised"
    #                         call sceneimg

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946655.mp3"
    #                         player " Alexa, I hope I'm not prying, but your belly looks like it's about to burst! Did you have a food marathon or something?"
    #                         $ position = "alexaexplaining"
    #                         call sceneimg

    #                         if speech == 1:        
    #                             play sound "audio/Kayla-1946782.mp3"
    #                         Alexa " Haha, you've got a keen eye! I may have gone a little overboard with taste-testing today."
    #                         $ position = "alexahappy"
    #                         call sceneimg

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946660.mp3"
    #                         player " Well, it's a tough job, but someone's got to do it, right?"

    #                         if speech == 1:        
    #                             play sound "audio/Kayla-1946787.mp3"
    #                         Alexa " You know it! Gotta make sure everything's up to our high standards."  

    #                     $ myrandom = renpy.random.randint(1,5)
    #                     $ position = "home"
    #                     call sceneimg
    #                     if myrandom == 1:

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946670.mp3"
    #                         player "I decided to send her a message on the cafe's social media page. It was a simple note, expressing my hope that she was doing well and assuring her that she could reach out if she ever needed to talk. It was a small gesture, but sometimes, that's all it took to brighten someone's day."
    #                     if myrandom == 2:

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946672.mp3"
    #                         player "I hesitated for a moment, unsure if it was appropriate to ask about her belly. After all, we had just met. But my curiosity got the best of me, and I crafted a polite message, asking if everything was alright and mentioning her belly in the most delicate way possible."
    #                     if myrandom == 3:

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946674.mp3"
    #                         player "Instead of reaching out immediately, I decided to do some research. I wanted to understand if a bloated belly was a common occurrence for her or if it was something unusual. I scrolled through the cafe's social media, looking for any clues or hints."
    #                     if myrandom == 4:

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946675.mp3"
    #                         player "As I continued my walk, I debated whether I should mention the bloated belly at all. It might come across as nosy or intrusive. Perhaps I should just wait for our next encounter and see if the topic naturally arose."
    #                     if myrandom == 5:

    #                         if speech == 1:        
    #                             play sound "audio/Waren-1946677.mp3"
    #                         player "The thought of Alexa's bloated belly lingered in my mind, but I couldn't bring myself to message her just yet. I needed more context, a better understanding of our connection. So, I decided to simply keep an eye out for her on my next visit to Crave Bites, hoping for a chance to talk again. "
    #                     jump culinarychoices
    #                 "Do not ask her anything":
    #                     pass 
    #         if alexafirsttime == 2 and alexa_bloatask == 0:

    #             if speech == 1:        
    #                 play sound "audio/Waren-1946683.mp3"
    #             player "That first bite of the Classic Cravings Burger at Crave Bites marked the beginning of my culinary journey in the city. Little did I know that this simple meal would be the first thread in a tapestry of connections, leading me to explore more about the city, its flavors, and the people who made it all so memorable."

    #             if speech == 1:        
    #                 play sound "audio/Waren-1946684.mp3"
    #             player "While I was thinking I found myself at home"
    #             jump culinarychoices
            
    #         if alexa_bloatask == 0 and alexa_fullstage > 1:
    #             $ position = "home"
    #             call sceneimg
    #             $ myrandom = renpy.random.randint(1,5)
    #             if myrandom == 1:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946686.mp3"
    #                 player "As I settled into my cozy apartment, I couldn't help but wonder about Alexa's unexpected bloating. I considered reaching out to her to see if she was okay, but our interaction had been brief, and I didn't want to overstep any boundaries."
    #             if myrandom == 2:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946691.mp3"
    #                 player "Back in my apartment, I replayed the day's events in my mind. Alexa's bloated belly was an enigma I couldn't ignore. I thought about messaging her to ask if everything was alright, but I hesitated. We were practically strangers, after all."
    #             if myrandom == 3:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946694.mp3"
    #                 player "Inside my apartment, the image of Alexa's bloated belly lingered in my thoughts. I contemplated sending her a friendly message, perhaps mentioning our shared love for burgers, but I didn't want to seem nosy."
    #             if myrandom == 4:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946695.mp3"
    #                 player "Settling into my apartment, I pondered the mystery of Alexa's bloated belly. It was clear she enjoyed the food she served, but was there more to it? I considered sending her a message to compliment the food and ask if she had any secret menu recommendations."
    #             if myrandom == 5:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946696.mp3"
    #                 player "As I entered my apartment, I couldn't shake the curiosity about Alexa's bloated belly. Should I send her a message, I wondered? I decided to play it safe for now, but my intrigue remained."
    #             jump culinarychoices

    #         if alexa_bloatask == 0 and alexa_fullstage == 1:
    #             $ position = "home"
    #             call sceneimg
    #             $ myrandom = renpy.random.randint(1,5)
    #             if myrandom == 1:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946698.mp3"
    #                 player "While I savored the delicious Classic Cravings Burger, I couldn't help but appreciate Alexa's warm and welcoming demeanor. She made my first visit memorable, and I considered going back to the cafe soon."
    #             if myrandom == 2:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946699.mp3"
    #                 player "Alexa's cheerful attitude at Crave Bites had left a positive impression on me. The burger was fantastic, but her friendly service was equally delightful. I looked forward to more visits to the cafe."
    #             if myrandom == 3:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946700.mp3"
    #                 player "As I settled into my apartment, I found myself thinking about Crave Bites and the fantastic burger I had enjoyed there. Alexa's attentive service had made the experience even better, and I planned to return."
    #             if myrandom == 4:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946704.mp3"
    #                 player "Back in my apartment, I reminisced about the tasty burger at Crave Bites and the friendly service Alexa had provided. It was a great introduction to the city's culinary offerings, and I couldn't wait to explore more."
    #             if myrandom == 5:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946707.mp3"
    #                 player "Inside my apartment, I felt content after a satisfying meal at Crave Bites. Alexa's friendly demeanor had made the experience enjoyable, and I hoped to discover more culinary gems in the city."
    #             jump culinarychoices

    #         if alexa_bloatask == 1:
    #             $ position = "home"
    #             call sceneimg
    #             $ myrandom = renpy.random.randint(1,5)
    #             if myrandom == 1:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946708.mp3"
    #                 player "While I savored the delicious Classic Cravings Burger, I couldn't help but appreciate Alexa's warm and welcoming demeanor. She made my first visit memorable, and I considered going back to the cafe soon."
    #             if myrandom == 2:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946709.mp3"
    #                 player "Alexa's cheerful attitude at Crave Bites had left a positive impression on me. The burger was fantastic, but her friendly service was equally delightful. I looked forward to more visits to the cafe."
    #             if myrandom == 3:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946712.mp3"
    #                 player "As I settled into my apartment, I found myself thinking about Crave Bites and the fantastic burger I had enjoyed there. Alexa's attentive service had made the experience even better, and I planned to return."
    #             if myrandom == 4:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946713.mp3"
    #                 player "Back in my apartment, I reminisced about the tasty burger at Crave Bites and the friendly service Alexa had provided. It was a great introduction to the city's culinary offerings, and I couldn't wait to explore more."
    #             if myrandom == 5:

    #                 if speech == 1:        
    #                     play sound "audio/Waren-1946707.mp3"
    #                 player "Inside my apartment, I felt content after a satisfying meal at Crave Bites. Alexa's friendly demeanor had made the experience enjoyable, and I hoped to discover more culinary gems in the city."
    #             jump culinarychoices


"something went wrong!"
jump bcafe