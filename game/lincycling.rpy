label lincycling:  

    if calendar.Hours > 11 and calendar.Hours < 16 and calendar.WeekDay == "Sat":
        pass
    else:
        $ linrideabikesat = 0
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            $ position = "linbikeparklistening"
            call sceneimg
            player "Lin, today's ride was fantastic. Thanks for leading the way and showing me those amazing trails."
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "I'm so glad you enjoyed it! It was great having you along. We should definitely do this again soon."
            $ position = "linbikeparklistening"
            call sceneimg

            player "Absolutely, I'd love that. Let's plan another ride in the near future. You've shown me a new side to cycling."
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "It's a date! Take care and rest up after today's workout. You did really well out there."
            $ position = "linbikeparklistening"
            call sceneimg

            player "Thanks, Lin. You too. Have a great rest of your day!"
        if myrandom == 2:
            $ position = "linbikeparklistening"
            call sceneimg

            player "What an exhilarating ride, Lin! I had a blast. You really know how to pick a route."
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "It's always more fun with good company. I'm happy you had a good time. Let's not wait too long for our next ride!"
            $ position = "linbikeparklistening"
            call sceneimg

            player "Definitely, count me in. It's always a pleasure riding with you. Thanks for a great day."
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "You're welcome! And thank you for joining me. See you soon, and take care!"
            $ position = "linbikeparklistening"
            call sceneimg

            player "See you, Lin. Enjoy the rest of your day!"
        if myrandom == 3:
            $ position = "linbikeparklistening"
            call sceneimg

            player "Lin, that was an amazing cycling experience. Thanks for inviting me along."
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "Of course! It’s always more enjoyable with a friend. I hope we can do it again sometime."
            $ position = "linbikeparklistening"
            call sceneimg

            player "I'd really like that. You’ve made cycling even more enjoyable for me. Let's plan another outing soon."
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "Sounds like a plan! Have a great rest of your day and take it easy after all that pedaling."
            $ position = "linbikeparklistening"
            call sceneimg

            player "Will do, Lin. You too, take care!"
        jump culinarychoices

    if lincycling == 0:
        $ lincycling = 1
        $ position = "linbikeparkmeeting"
        call sceneimg
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            

            player "Hey Lin, ready for our cycling adventure? It's a perfect day for it!"
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "Absolutely! I've been looking forward to this. It's great to switch things up from hiking to cycling."
            $ position = "linbikeparklistening"
            call sceneimg

            player "Same here. It's always exciting to explore new trails. Have you got your water and snacks?"
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "All set. I brought some energy bars too. Let's hit the road and enjoy the ride!"
            $ position = "linbikeparklistening"
            call sceneimg

            player "Fantastic, let's make the most of it. And who knows, we might find some new inspiration for our cooking and training."

        if myrandom == 2:
            

            player "Good morning, Lin! Ready to conquer some trails on our bikes today?"
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "Morning! Yes, I can't wait. It's always refreshing to get out and pedal through nature."
            $ position = "linbikeparklistening"
            call sceneimg

            player "Couldn't agree more. Cycling gives a whole new perspective on the outdoors. Did you bring everything you need?"
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "I did, including plenty of water. I'm all about staying hydrated on these rides."
            $ position = "linbikeparklistening"
            call sceneimg

            player "Excellent. Stay safe, and let's enjoy the journey. Maybe we'll find a nice spot for a break and a snack."
        if myrandom == 3:
            

            player "Hey Lin, great to see you! Ready for some cycling fun?"
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "Definitely, it's a nice change from our regular hikes. I'm all geared up for today."
            $ position = "linbikeparklistening"
            call sceneimg

            player "That's the spirit. Cycling is a great way to mix up our fitness routine. You got your helmet and gear?"
            $ position = "linbikeparktalk"
            call sceneimg

            Lin "Yes, safety first! And I packed some light snacks too. Can't wait to see what the trail has in store for us."
            $ position = "linbikeparklistening"
            call sceneimg

            player "Perfect, let's keep it safe and enjoyable. Maybe we’ll discover some scenic spots for future outings."

    menu:    
        "So you are the boss, what's the plan?" if lincyclingboss == 0:
            $ lincyclingboss = 1

            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "linbikeparklistening"
                call sceneimg
            

                player "Lin, do you have any suggestions on where we could go cycling today? Maybe somewhere with a nice view?"
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "Yes, I have the perfect place in mind. Let's head to the park. It has some fantastic views and excellent bike paths."
                $ position = "linbikeparklistening"
                call sceneimg

                player "That sounds like a plan! Is it a challenging route, or more on the relaxed side?"
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "It's pretty relaxed but with enough variety to keep it interesting. The park is known for its scenic routes and lush landscapes."
                $ position = "linbikeparklistening"
                call sceneimg

                player "Sounds like a photographer's dream. I'll make sure to bring my camera. Let's enjoy the day and the views!"
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "Great idea! It'll be a fun ride with lots of photo opportunities. Ready to roll out?"
                $ position = "linbikeparklistening"
                call sceneimg

                player "Absolutely! Let's make the most of this beautiful day and explore the park."
            if myrandom == 2:
                $ position = "linbikeparklistening"
                call sceneimg

                player "Lin, any thoughts on where we should cycle today? Something scenic would be lovely."
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "Definitely! Let's go to the park. It's got the best bike roads and the views are simply breathtaking."
                $ position = "linbikeparklistening"
                call sceneimg

                player "Oh, that sounds wonderful. I haven't been there yet. Are the paths beginner-friendly?"
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "They are perfect for all levels. The park offers a mix of easy and slightly challenging paths, all surrounded by natural beauty."
                $ position = "linbikeparklistening"
                call sceneimg

                player "That’s exactly what I was hoping for. A peaceful ride surrounded by nature. Shall we get going?"
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "Let's do it. You're going to love the views and the peaceful atmosphere. The park is a cyclist's delight."
                $ position = "linbikeparklistening"
                call sceneimg

                player "Can't wait to experience it. Today's going to be a great day for a ride."
            if myrandom == 3:
                $ position = "linbikeparklistening"
                call sceneimg

                player "Hey Lin, any good cycling spots you’d recommend for today? I’d love somewhere with great views."
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "I know just the place. How about we cycle to the park? It has some stunning views and the bike paths are top-notch."
                $ position = "linbikeparklistening"
                call sceneimg

                player "Sounds like an adventure. I'm looking forward to it. Are the paths suitable for a leisurely ride?"
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "Absolutely. The park has a variety of paths, from easy to moderately challenging, all with gorgeous scenery."
                $ position = "linbikeparklistening"
                call sceneimg

                player "That sounds ideal. A bit of exercise, fresh air, and nature. Let’s get going and enjoy the day."
                $ position = "linbikeparktalk"
                call sceneimg

                Lin "Yes, let's set off. The park is a beautiful spot for cycling, and I think you're going to really enjoy the ride."
                $ position = "linbikeparklistening"
                call sceneimg

                player "Alright, let's make today an adventure. The park awaits!"


        "Make her a compliment":
            $ calendar.AddMinutes(15)
            $ myrandom = renpy.random.randint(1,20)
            $ reputationchange = 1
            $ nigirlimage = "nilin"
            call reputationchange
            if myrandom == 1:
                
                call linbikeimg
                player "You're really setting a great pace, Lin. Impressive!"
                Lin "Thanks! I've been practicing. It's nice to have a good cycling partner like you."
            if myrandom == 2:
                
                call linbikeimg
                player "Your energy is contagious, Lin. It makes this ride even more enjoyable."
                Lin "I'm glad to hear that. Cycling with you is a lot of fun!"
            
            if myrandom == 3:
                
                
                call linbikeimg

                player "You handle your bike so well. It's like you were born to cycle."
                Lin "That's kind of you to say. I just love being on a bike, especially on days like this."
            
            if myrandom == 4:
                
                call linbikeimg


                player "Your enthusiasm for cycling is really motivating. It pushes me to do better."
                Lin "We motivate each other! That's what makes cycling together so rewarding."
            
            if myrandom == 5:
                
                call linbikeimg


                player "You know, you have an incredible sense of direction on these trails."
                Lin "Thanks! I've spent a lot of time exploring these paths. It's great to share them with you."
            
            if myrandom == 6:
                
                call linbikeimg


                player "I admire how effortlessly you tackle these hills. Truly inspiring."
                Lin "Cycling’s all about the challenge and the thrill. I’m happy to inspire you!"
                
            if myrandom == 7:
                
                call linbikeimg

                player "Your choice of route is perfect. You really know the best spots."
                Lin "I’m glad you like it. There’s nothing like sharing my favorite trails with a friend."
            
            if myrandom == 8:
                
                call linbikeimg


                player "You're in great shape, Lin. It's amazing how you keep up such a strong pace."
                Lin "Thanks! Regular cycling does wonders. And it's more fun with a companion like you."

            if myrandom == 9:
                
                call linbikeimg


                player "Your stamina is something else! You’re like the Energizer Bunny on a bike."
                Lin "Haha, that's a fun comparison! I just love cycling, it energizes me."
            
            if myrandom == 10:
                
                call linbikeimg


                player "I'm impressed by your cycling skills. You make it look so easy."
                Lin "Thank you! It's all about practice. And having a good cycling buddy helps too."
            
            if myrandom == 11:
                
                call linbikeimg


                player "You've got a real knack for finding the most scenic routes."
                Lin "I always keep an eye out for the best views. Glad you're enjoying it."
            
            if myrandom == 11:
                
                call linbikeimg


                player "Your enthusiasm really brightens up the ride. It’s infectious!"
                Lin "That's sweet of you to say. I always enjoy our cycling trips."
            
            if myrandom == 13:
                
                call linbikeimg


                player "You’re like a professional cyclist. It’s amazing to watch you ride."
                Lin "You're making me blush! I just love cycling, that's all."

            if myrandom == 14:
                
                call linbikeimg


                player "This route is fantastic. Your choice in trails is top-notch."
                Lin "I'm happy you think so. I always try to pick the best routes for us."

            if myrandom == 15:
                
                call linbikeimg


                player "Your energy levels are incredible, Lin. I'm trying to keep up!"
                Lin "You're doing great! It’s all about enjoying the ride together."
            
            if myrandom == 16:
                
                call linbikeimg


                player "You're an excellent guide, Lin. I feel like I'm on a professional tour."
                Lin "I’m flattered! I just want to make sure we have a great time cycling."
            
            if myrandom == 17:
                
                call linbikeimg


                player "Your passion for cycling really shines through. It’s inspiring."
                Lin "Cycling's my way of connecting with nature. I'm glad it inspires you."

            if myrandom == 18:
                
                call linbikeimg


                player "You've really planned out a great route. It's the perfect balance of challenge and beauty."
                Lin "Thank you! I thought you'd enjoy this mix. It's great to have you along."

            if myrandom == 19:
                
                call linbikeimg


                player "You've got a real talent for this, Lin. Your cycling skills are top-level."
                Lin "Thanks! I’ve been cycling for a while now. It’s one of my favorite things to do."

            if myrandom == 20:
                
                call linbikeimg


                player "You make cycling look so graceful. It’s like watching an athlete in action."
                Lin "What a compliment! I just try to be smooth and steady on the bike."


    jump lincycling