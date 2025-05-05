label krisfirstmeet:
    $ position = "kriswalking"
    call sceneimg
    play music "audio/countryside_birds.mp3" volume 0.3
    "You can see Kris is walking at the street while you are going home"
    "What will you do?"
    menu:
        "Say hello!" if krisfirstmeet == 0:
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "krisshy"
                call sceneimg
                player "Hey there, I'm [name], your new neighbor. I just moved in a couple of days ago."
                $ position = "krishi"
                call sceneimg
                Kris "Oh, hi! I'm Kris. Nice to meet you. So, what brings you to this neck of the woods?"
                $ position = "krisshy"
                call sceneimg
                player "Well, I got a job in town, and this place seemed like a great spot to settle down. How about you?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "I've been living here for a while. It's a quiet neighborhood, perfect for me."
                $ position = "krisshy"
                call sceneimg
                player "Quiet sounds nice. I'm looking forward to getting to know the area better."
                $ position = "krisexplaining"
                call sceneimg
                Kris "It is. And if you need any info about the area or anything else, just give me a shout."
                $ krisfirstmeet = 1

            if myrandom == 2:
                $ position = "krisshy"
                call sceneimg
                player "Hello, I'm [name]. I moved in next door recently."
                $ position = "krishi"
                call sceneimg
                Kris "Hi. I'm Kris. Nice to meet you. How's the new place treating you?"
                $ position = "krisshy"
                call sceneimg
                player "It's been good so far. Quiet neighborhood, which I like. How long have you been living here?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "I've been here for a few years now. It's a pretty chill area, and the neighbors are friendly."
                $ position = "krisshy"
                call sceneimg
                player "That's great to hear. Looking forward to getting to know everyone around here."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Likewise. If you have any questions about the neighborhood or need a hand with anything, just give me a shout."
                $ krisfirstmeet = 1

            if myrandom == 3:
                $ position = "krisshy"
                call sceneimg
                player "Hey, I'm [name]. Just moved into the house down the street."
                $ position = "krishi"
                call sceneimg
                Kris "Hi. Kris here. Welcome to the neighborhood. Need any help settling in?"
                $ position = "krisshy"
                call sceneimg
                player "Thanks, Kris. I appreciate that. It's always nice to have a friendly face nearby. How long have you lived here?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "I've been around for a few years now. It's a quiet place, and I like the community vibe here."
                $ position = "krisshy"
                call sceneimg
                player "Community vibe, huh? That's great to hear. I'm looking forward to being a part of it."
                $ position = "krisexplaining"
                call sceneimg
                Kris "You'll fit right in. If you ever want to chat or need anything, don't hesitate to reach out. Welcome!"
                $ krisfirstmeet = 1


        "Ask about neighbours" if krisfirstmeet == 1:
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                player "Kris, I'm still getting to know our immediate neighbors. Anything interesting I should know?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Well, Aurora lives just a few houses down from you. She's an eco-friendly enthusiast, always taking care of her garden and keeping things tidy."
                $ position = "krisshy"
                call sceneimg
                player "That's intriguing. Anyone else nearby?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Of course, we've got Mr. Johnson next door, who enjoys fishing by the river. And let's not forget Mrs. Roberts across the street, she's a retired teacher and a delightful neighbor."
                $ position = "krisshy"
                call sceneimg
                player "Thanks for the introductions, Kris. I'll be sure to say hi."
                $ position = "krisexplaining"
                call sceneimg
                Kris "You're welcome! Enjoy getting to know the neighborhood."
                $ krisfirstmeet = 2
            if myrandom == 2:
                player "Kris, can you tell me more about our immediate neighbors? I'd like to get to know who's around."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Certainly! Aurora lives nearby; she's really into gardening and eco-friendly practices. Then there's Mr. Johnson, who loves fishing in the river."
                $ position = "krisshy"
                call sceneimg
                player "Sounds like a nice mix of people. Who else should I be aware of?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Right across the street, there's Mrs. Roberts, a retired teacher who's always up for a chat. And of course, there's you!"
                $ position = "krisshy"
                call sceneimg
                player "Thanks, Kris. I'll make an effort to connect with our neighbors."
                $ position = "krisexplaining"
                call sceneimg
                Kris "You'll fit right in. We're a friendly bunch."
                $ krisfirstmeet = 2
            if myrandom == 3:
                player "Kris, since I'm new here, I'd love to know more about our immediate neighbors. Who are the folks living nearby?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Sure thing! Aurora is your neighbor a few houses down; she's passionate about her garden and sustainability."
                $ position = "krisshy"
                call sceneimg
                player "That's good to know. Who else is in the neighborhood?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Well, right next door, there's Mr. Johnson, who's always out by the river, fishing. And across the street, you'll find Mrs. Roberts, a retired teacher who's quite friendly."
                $ position = "krisshy"
                call sceneimg
                player "Thanks for the info, Kris. I'll make sure to introduce myself."
                $ position = "krisexplaining"
                call sceneimg
                Kris "No problem at all. Enjoy getting to know the neighborhood!"
                $ krisfirstmeet = 2


        "Ask Kris about her free time choices" if krisfirstmeet == 2:
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "krisshy"
                call sceneimg
                player "Kris, since we're getting to know each other, what do you like to do in your free time?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Well, I enjoy going for long walks in the park, especially on sunny days. It's a great way to clear my head and stay active."
                $ position = "krisshy"
                call sceneimg
                player "That sounds relaxing. Anything else you're passionate about?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Yes, I'm a bit of a fitness enthusiast, as you might have guessed. I find working out at the fitness club really energizing. It helps me stay in shape and de-stress."
                $ krisfitness = 1
                $ position = "krisshy"
                call sceneimg
                player "That's great to hear. Staying active is important. What about your hobbies?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "I'm also into cooking, trying out new recipes. It's a fun way to unwind and experiment with different flavors."
                $ kriscooking = 1
                $ position = "krisshy"
                call sceneimg
                player "Cooking, huh? That's fascinating. I'm actually a cook myself. We'll have to swap some recipes sometime."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Absolutely! I'd love to exchange culinary tips. It's always a pleasure to meet someone who shares a passion for good food."
                $ position = "krisshy"
                call sceneimg
                player "Sounds like we have some common interests. I'm looking forward to getting to know you better, Kris."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Likewise! It's great to have friendly neighbors like you."
                $ krisfirstmeet = 3
            if myrandom == 2:
                $ position = "krisshy"
                call sceneimg
                player "Kris, we've talked a lot about the neighborhood, but I'd like to get to know you better too. What do you like to do in your free time?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Well, when I'm not at the fitness club, I enjoy painting. It's a great way to relax and express myself creatively."
                $ position = "krisshy"
                call sceneimg
                player "That's fascinating! What kind of art do you usually create?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "I mostly do abstract art. I find it liberating, as it allows me to let my thoughts and emotions flow onto the canvas without any constraints."
                $ krisartist = 1
                player "Sounds like a wonderful way to unwind. I've always admired artists. Do you ever exhibit your work?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "I've exhibited a few times locally, but it's more of a personal passion than a profession. How about you? What do you like to do in your free time?"
                $ position = "krisshy"
                call sceneimg
                player "Well, I'm a bit of a foodie, so I enjoy experimenting with new recipes. Cooking is like a culinary adventure for me."
                $ position = "krisexplaining"
                call sceneimg
                Kris "That's intriguing! Maybe you can whip up something special for our neighbors one day. It could be a great way to get to know everyone better."
                $ position = "krisshy"
                call sceneimg
                player "That's a fantastic idea, Kris. I'll have to put together a menu."
                $ position = "krisexplaining"
                call sceneimg
                Kris "I'm sure they'll appreciate it. Let me know if you need any help with the cooking or organizing."
                $ position = "krisshy"
                call sceneimg
                player "Thanks, Kris. I'll keep that in mind. It's been great chatting with you."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Likewise! It's always nice to connect with neighbors."
                $ krisfirstmeet = 3
            if myrandom == 3:  
                $ position = "krisshy"
                call sceneimg
                player "Kris, we've talked about the neighborhood and all, but what's your story? Got any exciting hobbies or interests?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Well, I'm pretty laid-back. I enjoy working out and keeping fit, as you can probably tell. Fitness is a big part of my life."
                $ krisfitness = 1
                $ position = "krisshy"
                call sceneimg
                player "That's great! Staying healthy is important. Anything else you're passionate about?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Actually, I'm a bit of a foodie. I love trying out new dishes and experimenting in the kitchen. Cooking is like therapy for me."
                $ kriscooking = 1
                $ position = "krisshy"
                call sceneimg
                player "Wow, a fitness enthusiast and a food lover! That's an interesting combination. Any favorite dishes you like to whip up?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Definitely! I make a mean avocado and spinach salad with a zesty lemon dressing. It's refreshing after a good workout."
                $ position = "krisshy"
                call sceneimg
                player "Sounds delicious. Maybe you could give me some cooking tips sometime?"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Absolutely! We should exchange fitness and cooking secrets. What about you? Any interesting hobbies or passions?"
                $ position = "krisshy"
                call sceneimg
                player "Well, I'm a bit of a gamer and love reading sci-fi novels. Plus, I'm always up for a good adventure, like exploring our new town."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Gaming and sci-fi, huh? That's cool! If you ever need a workout buddy or someone to talk about the latest sci-fi releases, you know where to find me."
                $ position = "krisshy"
                call sceneimg
                player "Likewise, Kris. It's good to know we've got some shared interests."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Absolutely. Here's to new friendships and exciting adventures in our neighborhood!"
                $ krisfirstmeet = 3

            
            
            
        "Invite her to spend time with you at your backyard" if krisfirstmeet == 3 and krisbackyard == 0:
            
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "krisshy"
                call sceneimg
                player "Hey, Kris, you know, I've got this nice backyard with a fireplace. I often hang out there to relax, especially when it gets colder. You're welcome to join me anytime you want."
                $ position = "krisexplaining"
                call sceneimg
                Kris "A fireplace, huh? That sounds cozy. What do you do out there?"
                $ position = "krisshy"
                call sceneimg
                player "Well, I use it to stay warm, of course, but I also enjoy cooking some delicious stuff on the open flame. It's like having a little outdoor kitchen."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Cooking outside sounds like fun! What kind of dishes do you make?"
                $ position = "krisshy"
                call sceneimg
                player "I've grilled some fantastic burgers, roasted marshmallows for s'mores, and even made a few kebabs. It's all about that smoky flavor."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Wow, that sounds amazing! I'd love to join you sometime. Cooking together and enjoying the warmth of a fire sounds like a great way to spend an evening."
                $ position = "krisshy"
                call sceneimg
                player "That's the spirit! Whenever you're up for it, just give me a heads up, and I'll fire up the grill. Pun intended."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Thanks, that's really nice of you. Looking forward to it!"
                $ krisbackyard = 1
            if myrandom == 2:
                $ position = "krisshy"
                call sceneimg
                player "Kris, you know, I've got this cozy backyard with a nice fireplace. Whenever you want to hang out, maybe roast some marshmallows or cook something together, you're welcome."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Oh, that sounds really nice! A backyard fireplace? I'm in! I'd love to try some outdoor cooking."
                $ position = "krisshy"
                call sceneimg
                player "Great! It's a deal then. We can have a barbecue night or just relax by the fire. Let me know when you're free."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Thanks for the invite! It sounds like a lot of fun. I'll definitely take you up on that offer."
                $ position = "krisshy"
                call sceneimg
                player "Looking forward to it, Kris. It'll be a blast!"
                $ position = "krisexplaining"
                call sceneimg
                Kris "Me too! Our own little backyard adventures."
                $ krisbackyard = 1
            if myrandom == 3:
                $ position = "krisshy"
                call sceneimg
                player "Hey, Kris, you know, I've got this cozy backyard with a nice fireplace. I often hang out there, especially during evenings. You're welcome to join anytime, and we can whip up some good food together."
                $ position = "krisexplaining"
                call sceneimg
                Kris "Oh, that sounds like a lot of fun! A fireplace in the backyard for cooking? Count me in. What kind of dishes do you usually make there?"
                $ position = "krisshy"
                call sceneimg
                player "Well, it's a versatile setup. We can grill some barbecue, roast marshmallows, or even try some outdoor pizza-making. It's all about good food and good company."
                $ position = "krisexplaining"
                call sceneimg
                Kris "I love the sound of that! Grilling and roasting marshmallows by the fire? That's my idea of a perfect evening."
                $ position = "krisshy"
                call sceneimg
                player "Great! Whenever you're in the mood for some outdoor cooking and relaxation, just give me a shout. We'll make it happen."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Thanks, that's really kind of you. I'll definitely take you up on that offer. Looking forward to some backyard cooking adventures!"
                $ position = "krisshy"
                call sceneimg
                player "It's a plan then! Can't wait to share some good times and delicious meals with you, Kris."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Likewise, neighbor. Here's to tasty adventures in our backyard!"
                $ krisbackyard = 1

            

        "Ask her about her story" if krisfirstmeet == 3 and krisstory == 0:
            $ krisstory = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "krisshy"
                call sceneimg
                player "So, Kris, I've learned a bit about the neighborhood and some of our neighbors. How about you? What's your story?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Oh, I've been living here for a while now. Moved in when I got this job nearby. It's a nice, quiet place."
                $ position = "krisshy"
                call sceneimg
                player "That sounds great. What brought you to this part of town?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Well, it was mainly the job. But also, I've always liked this neighborhood. It's close to the park, the fitness club, and not too far from the ocean. Plus, the neighbors are pretty friendly."
                $ position = "krisshy"
                call sceneimg
                player "Sounds like you've got it all figured out. How about you? What's your story?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Me? I'm still settling in, actually. Just moved here not too long ago. Trying to explore the city and get to know my neighbors. It's been quite an adventure."
                $ position = "krisshy"
                call sceneimg
                player "Well, you're in the right place for adventures. If you ever need any tips or company for exploring, I'm here."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Thanks, that's really nice of you. Exploring the city together sounds like a plan. We'll have some good times, I'm sure."
                $ position = "krisshy"
                call sceneimg
                player "Absolutely! Looking forward to it, Kris. Here's to new beginnings and exciting adventures."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Cheers to that, neighbor!"
                
            if myrandom == 2:
                $ position = "krisshy"
                call sceneimg
                player "So, Kris, we've talked a lot about our neighborhood, but I realized I don't know much about your background. What's your story?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Ah, well, there's not much to tell, really. I grew up not too far from here, in the city. After finishing school, I moved here to get away from the bustling urban life and enjoy a more peaceful atmosphere."
                $ position = "krisshy"
                call sceneimg
                player "Sounds like a big change. What brought you to our neighborhood specifically?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "You know, I visited a friend who lived here once, and I fell in love with the tranquility and the friendly vibe. So, I decided to make it my home too."
                $ position = "krisshy"
                call sceneimg
                player "That's nice. And what do you do for a living, Kris?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "I'm a freelance graphic designer. I've always been into art and design, so it felt like the perfect fit for me. I get to work on various projects and have the flexibility to set my own schedule."
                $ position = "krisshy"
                call sceneimg
                player "That sounds pretty awesome, actually. Creative freedom and flexibility, who wouldn't want that?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "I know, right? I feel lucky to have found my passion. But enough about me, what's your story, Player?"
                $ position = "krisshy"
                call sceneimg
                player "Well, I recently moved here from out of town. I'm a cook, and I'm hoping to find a place in the culinary scene around here."
                $ position = "krisexplaining"
                call sceneimg

                Kris "A cook? That's fantastic! We've got some great food spots in the neighborhood. I'm sure you'll find your niche."
                $ position = "krisshy"
                call sceneimg
                player "Thanks, Kris. It's been a bit of an adjustment, but meeting neighbors like you is making the transition easier."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Anytime, Player. We're all in this neighborhood together, after all."
                $ position = "krisshy"
                call sceneimg
                player "Absolutely, Kris. Cheers to good neighbors and new beginnings."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Cheers!"

            if myrandom == 3:
                $ position = "krisshy"
                call sceneimg
                player "So, Kris, we've talked about the neighborhood, but I realized we haven't shared much about our own stories. What's your life history? Any interesting tales?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Ah, my life history, huh? Well, it's not the most thrilling, but I grew up in a small town not too far from here. I've always been a bit of a free spirit, you know, taking life as it comes."
                $ position = "krisshy"
                call sceneimg
                player "Sounds nice. And what brought you to this city? Was it the hustle and bustle or something else?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Well, I've always been drawn to new experiences. The city offered more opportunities, and it's been an interesting journey so far. Plus, I'm living closer to the beach now, which is a dream come true."
                $ position = "krisshy"
                call sceneimg
                player "That's great to hear! As for me, I'm quite the newcomer here. Just moved to the city recently for a fresh start. It's a big change, but I'm excited about all the possibilities."
                $ position = "krisexplaining"
                call sceneimg

                Kris "A fresh start can be amazing. New places, new faces, and who knows what adventures lie ahead?"
                $ position = "krisshy"
                call sceneimg
                player "Exactly! I'm looking forward to exploring more of the city and getting to know my awesome neighbors better."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Well, you're off to a good start, getting to know your neighbors. We're a diverse bunch, and there's always something happening around here."
                $ position = "krisshy"
                call sceneimg
                player "I've noticed that, and I'm glad to be part of this vibrant community. Thanks for sharing a bit of your story, Kris."
                $ position = "krisexplaining"
                call sceneimg

                Kris "No problem at all, neighbor. We're all in this together, right?"



        "Tell Kris how you ended up here" if krisstory == 1:
            $ krisstory = 2
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "krisshy"
                call sceneimg
                player "You know, Kris, I've been meaning to share a bit more about myself too. I moved here from a small town, looking for a change of scenery and new opportunities."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Oh, really? What was your small town like?"
                $ position = "krisshy"
                call sceneimg
                player "It was one of those places where everyone knows everyone else's business. I had a stable job, a cozy little house, and some close friends, but I felt like something was missing. I needed a fresh start."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I can understand that feeling. Sometimes, you just need to break free from your comfort zone and see what else life has to offer."
                $ position = "krisshy"
                call sceneimg
                player "Exactly. So, I packed my bags and landed here in the city. It's been quite an adjustment, but I'm excited about the possibilities."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Well, you've certainly come to a lively neighborhood. We may be a bit quirky at times, but there's never a dull moment around here."
                $ position = "krisshy"
                call sceneimg
                player "That's what I've noticed, and honestly, I'm loving it. Meeting new people like you and exploring the city has been an adventure in itself."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I'm glad to hear that. And hey, if you ever need someone to show you the ropes or share a few stories, I'm just next door."
                $ position = "krisshy"
                call sceneimg
                player "Thanks, Kris. I appreciate the warm welcome. It's good to know I've got friendly neighbors to count on."
                $ position = "krisexplaining"
                call sceneimg

                Kris "You bet, neighbor. We're here to look out for each other and make this place feel like home."

            if myrandom == 2:
                $ position = "krisshy"
                call sceneimg
                player "You know, Kris, I've shared a lot about my new life here, but I haven't really talked about where I'm coming from. My story's a bit of a winding road."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I'd love to hear it. We've got time."
                $ position = "krisshy"
                call sceneimg
                player "Well, I grew up in a quiet suburban neighborhood, quite different from this lively city life. I always had a passion for cooking, right from my mom's kitchen. That's where I learned the magic of flavors and the joy of creating something delicious."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Cooking, huh? That's fascinating. Do you have any special dishes you love to make?"
                $ position = "krisshy"
                call sceneimg
                player "Oh, absolutely. I've spent years perfecting my lasagna recipe. It's a labor of love, layering pasta, rich meat sauce, and creamy béchamel. But I'm always up for trying something new, too."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Lasagna sounds divine! You'll have to invite me over for dinner sometime."
                $ position = "krisshy"
                call sceneimg
                player "Consider it a date. Anyway, I decided to move here for a fresh start, hoping to bring some of that homey comfort to this bustling city. So far, it's been an exciting journey of new beginnings."
                $ position = "krisexplaining"
                call sceneimg

                Kris "That's fantastic! Your passion for cooking will surely make an impact here. And, hey, you're not alone on this journey. You've got neighbors like me to share it with."
                $ position = "krisshy"
                call sceneimg
                player "Thanks, Kris. It's reassuring to know there are friendly faces like yours around. And who knows, maybe one day, I'll whip up a lasagna that'll make this neighborhood famous."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I can't wait for that day, neighbor. Until then, we'll enjoy every moment and every meal this city has to offer."
                $ position = "krisshy"
                call sceneimg
                player "Cheers to that, Kris."

            if myrandom == 3:
                $ position = "krisshy"
                call sceneimg
                player "You know, Kris, I've been meaning to share my story with you. It's not particularly dramatic, but I think it's worth telling."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I'd love to hear it. We're neighbors, after all. It's nice to get to know each other."
                $ position = "krisshy"
                call sceneimg
                player "I grew up in a small town, far from the city life. It was a close-knit community, and I had a pretty ordinary childhood. But as I got older, I started to feel this pull, this desire to explore beyond the familiar."
                $ position = "krisexplaining"
                call sceneimg

                Kris "That's fascinating. So, what made you decide to move here, to our city?"
                $ position = "krisshy"
                call sceneimg
                player "Well, it was a mix of things. I wanted a change of scenery, new experiences, and the city seemed like the perfect place for that. Plus, I've always been a food enthusiast, and I'm hoping to make a career in the culinary world."
                $ position = "krisexplaining"
                call sceneimg

                Kris "A culinary enthusiast? That's incredible! Have you worked in any restaurants or kitchens before?"
                $ position = "krisshy"
                call sceneimg
                player "Yeah, I have some experience, and I'm really passionate about it. Cooking has been a big part of my life. I'm eager to see where this culinary journey takes me in this city."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I have no doubt you'll do great, especially with your dedication. The city's culinary scene can be quite exciting."
                $ position = "krisshy"
                call sceneimg
                player "Thanks for the vote of confidence, Kris. It means a lot. And who knows, maybe one day, I'll whip up something special for you and our other neighbors."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I'm looking forward to that day! And if you ever need any ingredients or cooking tips, you know where to find me."
                $ position = "krisshy"
                call sceneimg
                player "I'll keep that in mind, Kris. It's been great sharing a bit of my story with you."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Likewise, neighbor. We've got a friendly bunch here, and I'm sure you'll find your place in no time."
            

        "Ask Kris about her personal life" if krisstory == 2:
            $ krisstory = 3
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "krisshy"
                call sceneimg
                player "Kris, you've been so friendly since I moved here. Tell me a bit about your personal life. Do you live here with family?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Oh, yes! I'm married to a wonderful man named Mark. We've been together for about five years now."
                $ position = "krisshy"
                call sceneimg
                player "That's great to hear. How did you two meet?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "It's a bit of a funny story, actually. We were neighbors just like you and I are now. We'd bump into each other while taking out the trash or checking the mail, and eventually, we started chatting more. One thing led to another, and here we are."
                $ position = "krisshy"
                call sceneimg
                player "Sometimes, love finds you in the most unexpected places, huh?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Exactly! And we've been happy ever since. Mark's a kind and supportive guy. He's also a great cook, so we share a love for good food."
                $ position = "krisshy"
                call sceneimg
                player "That sounds like a perfect match. And I'm guessing your cooking skills are pretty impressive too, considering your husband."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I do enjoy cooking, but I'm no culinary expert like you seem to be. It's more of a hobby for me. We complement each other in the kitchen."
                $ position = "krisshy"
                call sceneimg
                player "Well, it's clear you two have a strong connection, and that's what matters most. It's great to know a bit more about your life here, Kris."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Likewise, neighbor. If you ever want to hear more stories or need any advice, you know where to find me."
                $ position = "krisshy"
                call sceneimg
                player "I'll definitely keep that in mind. Thanks for sharing, Kris."

            if myrandom == 2:
                $ position = "krisshy"
                call sceneimg
                player "Kris, I've noticed you're married. How did you and your husband meet?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Oh, our story is a bit of a whirlwind, really. We met in college, both of us studying completely different subjects. It was at this quirky little café near the campus. We struck up a conversation about the coffee there, of all things."
                $ position = "krisshy"
                call sceneimg
                player "A café chat that turned into something more, huh?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "Exactly! We started meeting there regularly, and our conversations grew deeper. Eventually, we realized there was something special between us."
                $ position = "krisshy"
                call sceneimg
                player "That sounds like a lovely beginning. And how did he propose?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "He proposed in the most unexpected way. We used to visit this park, just a short walk from here, almost every weekend. One day, he surprised me with a picnic. We were sitting under a big oak tree when he pulled out a tiny velvet box."
                $ position = "krisshy"
                call sceneimg
                player "A picnic proposal! That's incredibly romantic."
                $ position = "krisexplaining"
                call sceneimg

                Kris "It was. He said he wanted our love to grow like the branches of that oak tree, strong and everlasting. It was impossible to say no after that."
                $ position = "krisshy"
                call sceneimg
                player "It sounds like a beautiful moment. You two must be really happy together."
                $ position = "krisexplaining"
                call sceneimg

                Kris "We are. He's been my rock through thick and thin, and I couldn't ask for a better partner."
                $ position = "krisshy"
                call sceneimg
                player "I'm glad to hear that, Kris. It's wonderful to have someone who stands by your side."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Indeed, and I hope you find happiness and support in this city too. If you ever want advice or just someone to talk to, I'm here for you."
                $ position = "krisshy"
                call sceneimg
                player "I appreciate that, Kris. Your kindness means a lot to me."

            if myrandom == 3:
                $ position = "krisshy"
                call sceneimg
                player "Kris, you've been so kind in sharing with me about the neighborhood and all. But what about you? Tell me more about your personal life."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Oh, you want to know about me, huh? Well, there's not much to tell, really. I'm happily married to my husband, Mark. We've been together for a few years now."
                $ position = "krisshy"
                call sceneimg
                player "That's wonderful to hear. How did you two meet?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "We actually met through mutual friends at a gathering, and it just clicked. Mark's a software engineer, so he's often busy with work, but when we do have time together, we make the most of it."
                $ position = "krisshy"
                call sceneimg
                player "It sounds like you have a great connection. How does he feel about the neighborhood?"
                $ position = "krisexplaining"
                call sceneimg

                Kris "He likes it here too, though he's not as outgoing as I am. Mark enjoys the tranquility of our neighborhood, and he's a big fan of the nearby park and ocean views."
                $ position = "krisshy"
                call sceneimg
                player "It's lovely to hear that you two are happy here. And if you ever need anything or want to chat, remember I'm just a stone's throw away."
                $ position = "krisexplaining"
                call sceneimg

                Kris "Thank you, neighbor. I appreciate that. It's nice to have friendly faces around, especially when Mark's at work."
                $ position = "krisshy"
                call sceneimg
                player "Anytime, Kris. I'm sure our neighborhood will continue to bring good experiences for both of us."
                $ position = "krisexplaining"
                call sceneimg

                Kris "I'm looking forward to it, and maybe one day, you'll get to meet Mark too."
        "Sorry, I have no time to talk, see you later":
            $ position = "krishi"
            call sceneimg
            Kris "Ok, see you, bye!"
            $ krisnottoday = 1
            jump culinarychoices

        

    jump krisfirstmeet