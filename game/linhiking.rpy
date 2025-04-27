label linhiking:
    $ linhike = 0
    hide screen linhikefeeding
    if linhikejustrest == 1 or linhikejustrest == 1 or linhikejustrest == 2 or linhikebreakeat == 1 or linhikingbreak == 1:
        $ position = "linhikingcampfiretalklisten"
        call sceneimg
    else:
        $ position = "linhikingwalking"
        call sceneimg

    if lin_attitude >= 90 and lin_dayfullness == 0 and lin_fullness < 1200:
        $ lin_fullness += 1200
        $ lin_dayfullness = 1

    # $ position = "linhikingtalklisten"
    # call sceneimg
    # pause
    # $ position = "linhikingno"
    # call sceneimg
    # pause
    # $ position = "linhikingtalk"
    # call sceneimg
    # pause
    # $ position = "linhikingyes" 
    # call sceneimg
    # pause
    # $ position = "linhikingwalking"
    # call sceneimg
    # pause
    # $ position = "linhikingcampfirelookingatthebellytalk"
    # call sceneimg
    # pause
    # $ position = "linhikingcampfirelookingatthebellytalk"
    # call sceneimg
    # pause
    # $ position = "linhikingcampfiretalkmouthopen"
    # call sceneimg
    # pause
    # $ position = "linsittingcampfiremouthopenedfromabove"
    # call sceneimg
    # pause
    
    # pause
    # $ position = "linhikingcampfiretalklisten"
    # call sceneimg
    # pause
    
    # pause


    if linhikinghi == 0:
        $ linhikinghi = 1

        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            $ position = "linhikinghi"
            call sceneimg

            Lin "Hey! Great to see you geared up for our hike. You look as excited as I am. Ready to explore the wilderness?"
            
            $ position = "linhikingtalklisten"
            call sceneimg

            player "Absolutely, Lin! I've been looking forward to this all week. I've got energy bars, water, and my camera. Can't wait to capture some nature shots!"
            $ position = "linhikingtalk"
            call sceneimg

            Lin "Perfect! You're well-prepared. We'll tackle some interesting trails today. The views are breathtaking, especially near the peak. Just follow my lead, and we'll make a great team."
            
            $ position = "linhikingtalklisten"
            call sceneimg

            player "Lead the way! I'm ready to hit those trails and see the world from the top. Let's make this an adventure to remember!"
            $ position = "linhikingtalk"
            call sceneimg

            Lin "That's the spirit! Remember, it's not just about the destination, but also enjoying the journey. Let’s get going and enjoy every step of the way!"
        if myrandom == 2:
            
            $ position = "linhikinghi"
            call sceneimg
            Lin "Good morning! Ready to start our hiking journey? It's a bit challenging, but I know we can do it."
            
            $ position = "linhikingtalklisten"
            call sceneimg

            player "Morning, Lin! Yes, I'm ready, though I'll admit I'm a bit nervous. It's been a while since I last hiked. I've got water and snacks, so I should be good."
            $ position = "linhikingtalk"
            call sceneimg

            Lin "No worries, we'll take it at a pace you're comfortable with. The trail has some steep parts, but we'll tackle them together. And the view at the end is worth it!"
            
            $ position = "linhikingtalklisten"
            call sceneimg

            player "Thanks for being understanding. I'll try to keep up. Let's make the most of this day and enjoy the hike at our own pace."   
            $ position = "linhikingtalk"
            call sceneimg         
        

            Lin "Absolutely, it's all about enjoying the experience. We'll take breaks as needed and keep it fun. Ready to start this beautiful journey?"
            
            $ position = "linhikingtalklisten"
            call sceneimg

            player "Yes, let's do this. I'm glad to have you as my guide and motivator. Here's to a day full of nature and new experiences!"
        if myrandom == 3:
            
            $ position = "linhikinghi"
            call sceneimg

            Lin "Hey there! I'm glad you could make it. This trail is one of my favorites for clearing the mind. Are you all set for today's hike?"
            
            $ position = "linhikingtalklisten"
            call sceneimg

            player "Hi Lin, yes, I'm ready. I brought some water and a light lunch. I'm looking forward to disconnecting and immersing myself in nature. I hope to find some peace along the way."
            $ position = "linhikingtalk"
            call sceneimg

            Lin "That's a wonderful approach. This trail has a way of soothing the soul. We'll pass through some serene spots where you can really feel at one with nature."
            
            $ position = "linhikingtalklisten"
            call sceneimg

            player "That sounds exactly like what I need. Let's embark on this journey with an open mind and heart. I'm ready to embrace the tranquility of the trail."
            $ position = "linhikingtalk"
            call sceneimg

            Lin "Then let's get going. Remember, it's about the journey as much as the destination. Let nature's beauty inspire us today."



    menu:
        "Talk about your impressions about the hike so far" if linhikingimpression == 0:
            $ linhikingimpression = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                

                player "Lin, this trail is incredible! The way the sunlight filters through the leaves, it's like something out of a fairy tale."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "I'm glad you're enjoying it. Nature has a way of surprising us with its beauty, especially on trails like this."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Absolutely! Every turn brings something new. I love how the landscape changes as we climb higher. What's your favorite part about hiking these trails?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "For me, it’s the sense of adventure and discovery. Every hike is a new experience, even on familiar trails. Plus, the physical challenge is invigorating."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I can see why. The fresh air, the sound of the birds, it’s all so revitalizing. And these views are worth every step. It's like the world opens up before you."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Exactly! That's why I love bringing people here. It’s rewarding to see others appreciate the beauty of the outdoors. Keep going; the view from the top is even more breathtaking."
            if myrandom == 2:
                

                player "This hike is quite the workout, Lin. I can feel every muscle in my legs. How do you keep up your energy on such intense hikes?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "It's all about pacing and knowing your limits. Regular breaks, staying hydrated, and good nutrition play a big part. It's important to listen to your body."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That makes sense. I'm learning to pace myself better. The beauty around here is a great distraction from the exertion, though. Do you find that being out here impacts your mindset?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Definitely. Hiking is not just physical for me; it's a mental release too. It helps me clear my head and refocus. Nature has a way of putting things in perspective."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I’m starting to feel that. There’s something about the simplicity of walking through nature that feels grounding. It’s a break from the chaos of everyday life."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Yes, exactly. The further we get from the start, the closer we get to finding a bit of peace. Just wait until we reach the summit. It's like standing on the edge of the world."
            if myrandom == 3:
                

                player "Lin, how did you get into hiking? Was it always a passion of yours?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "It started as a way to stay fit, but it quickly grew into something more. I fell in love with the peace and solitude of the trails."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I can see the appeal. There's something special about being out here, away from it all. Do you have any memorable hiking experiences you’d like to share?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "There are so many. Once, I got caught in a surprise rainstorm. I found shelter under a large tree and just watched the rain cascade through the forest. It was magical and humbling."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That sounds amazing. Nature's unpredictability is part of the adventure, isn't it? It must be incredible to witness all its moods up close."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Absolutely. Every hike, every weather change, brings a new perspective. You learn to appreciate the little things, like the sound of a stream or the rustle of leaves."


        "Do you think I can find any ingredients here?" if linhikingingredients == 0:
            $ linhikingingredients = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                

                player "Lin, this hike is amazing. I've been thinking about how these natural surroundings could inspire some new recipes. Ever come across any wild herbs or berries on these trails?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Actually, yes. There are patches of wild mint and sometimes wild strawberries around here. You could use them to add a fresh twist to your dishes."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That's perfect! Imagining the flavors of the forest in my cooking is thrilling. I'm always looking for fresh, natural ingredients. It adds authenticity to my culinary creations."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "I bet your dishes are as vibrant as the scenery we're seeing. Hiking can be a great way to get inspired. The wilderness has a lot to offer."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Definitely. The colors, the scents, it all blends like a perfect recipe. It's like nature is a master chef, presenting its best work. I can’t wait to translate this experience into my cooking."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "It's great to see your passion for cooking merge with your love for nature. Let's keep an eye out for more edible plants. You might find your next signature ingredient!"
            if myrandom == 2:
                

                player "Lin, hiking like this makes me think about the importance of a balanced lifestyle. As a cook, I’m surrounded by food all day, and it can be challenging to maintain that balance."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "I can imagine. It's all about finding harmony. Hiking is a great way to offset the sedentary aspects of cooking. Plus, it can be a source of inspiration."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Exactly. Being out here, away from the heat of the kitchen, it refreshes me. It's a different kind of heat, the warmth of the sun. It rejuvenates my creativity."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Nature has a way of doing that. And as a cook, you have the unique ability to bring these elements into your dishes. The energy, the freshness."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I try to. My goal is to capture these natural essences in my cooking. It's not just about taste; it's about the experience, the story behind each ingredient."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "That's a beautiful approach to cooking. The meals you create must be a true adventure for the palate. Just like this hike is for our senses."
            if myrandom == 3:
                

                player "This hike is giving me so many ideas, Lin. The variety of textures and colors in nature... I'm imagining how I could translate that into a plate."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "That's an interesting way to look at it. I bet your dishes are as vibrant and full of life as the landscape we're walking through."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I strive for that. There’s something about the simplicity of nature that I want to reflect in my cooking. Pure, unadulterated flavors that speak for themselves."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Sounds like your cooking is an art form. It's great to see how your passion for food intertwines with your love for the outdoors."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "For me, cooking is like painting a canvas, but with flavors. Each dish tells a story, much like each trail we hike has its own narrative."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "I love that analogy. It's clear that you're not just a cook, but a true artist. Your dishes must be a journey in themselves."


        "Is there edible plants in the forest?" if linhikingedible == 0:
            $ linhikingedible = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                
                

                player "Lin, as we're hiking through this beautiful mixed forest, I realize I don't know much about the local plants. As a cook, I'm always curious about natural ingredients. Do you know anything about the edible plants around here?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Well, I'm no botanist, but I do know a bit. For instance, see those berries over there? Those are wild raspberries, perfectly safe to eat and delicious. And over there, that’s wild garlic. You can use the leaves in your cooking for a mild garlic flavor."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That's fascinating! I can already imagine how I could incorporate them into my dishes. I always prefer using local, natural ingredients. They bring a unique touch to the culinary experience."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Absolutely, and it’s a great way to connect with the local environment. Just be sure to double-check any plants you're not sure about. It’s important to be certain they’re safe to consume."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Definitely, I'll be cautious. Thanks for the heads-up, Lin. This hike is turning out to be not just a physical journey, but a culinary exploration too!"
            if myrandom == 2:
                

                player "Lin, this forest is amazing, but I have to admit, I'm a bit out of my element. Back in the kitchen, I know my ingredients, but out here, I'm clueless. Do you know about any edible plants in these woods?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Sure, there are a few I can point out. See those leaves? That's a type of wild mint. It's really aromatic and would be great in teas or as a garnish. And over there, that’s a patch of fiddlehead ferns. They're great when sautéed."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Wow, I'm learning so much already! I always try to bring a touch of the natural world into my cooking. It's about creating a dish that's not just tasty but also tells a story."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "That’s a great approach to cooking. Just remember, when foraging, always be sure what you pick is safe to eat. There’s a lot out here, but not everything is edible."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I’ll keep that in mind. Maybe I should carry a guidebook for edible plants on my next hike. Thanks for sharing your knowledge, Lin!"
            if myrandom == 3:
                

                player "Lin, being relatively new to this area, I’m not familiar with the local flora. In the kitchen, I love experimenting with different herbs and plants. Do you know any edible plants we might find here?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "I do know a bit. For example, those small white flowers over there are wild chives. They have a mild onion flavor. And that plant with the small blue flowers is borage, which is edible and has a taste similar to cucumber."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "This is exactly the kind of knowledge I was hoping to gain on our hike. Using ingredients straight from nature can really elevate a dish and give it a unique character."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "I agree, and it’s a sustainable way to source ingredients. Just be careful and make sure to identify plants correctly before using them in your cooking."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Absolutely, safety first. I might start bringing a plant identification guide on hikes. Thanks for the insights, Lin. This is turning into an educational adventure!"


        "Tell me about this place ecology" if linhikingecology == 0:
            $ linhikingecology = 1
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                
                $ position = "linhikingtalk"
                call sceneimg

                Lin "This area has a rich natural history. Being close to the sea, the saline air influences the flora around here. The vegetation has adapted to these unique conditions."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That’s fascinating! The saline influence must give the plants here a unique character. As a cook, it's exciting to think about how these flavors could enhance a dish."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Exactly. And geologically, this area has transformed dramatically over millions of years. It used to be under the sea, and the rocky terrain we see now is the result of tectonic movements."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Incredible! Walking on what was once the seabed... It makes you appreciate the dynamic nature of our planet. The mineral-rich soil here must be a factor in the unique plant life."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "You're right. The soil composition definitely contributes to the diversity of plants. It’s like a natural pantry, full of unique ingredients for you to explore."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I'm inspired already. I can't wait to experiment with these local flavors. This hike is turning into a treasure hunt for new ingredients!"
            if myrandom == 2:
                $ position = "linhikingtalk"
                call sceneimg

                Lin "This forest is quite unique due to its proximity to the sea. The salty air here has a significant impact on the types of plants that thrive in this region."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That’s an interesting point. The sea’s influence extends beyond the shore, shaping the ecosystem. It's a reminder of how interconnected our environment is."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Absolutely. And geologically, this place has a rich history. Once submerged under the ocean, the rocks we see today are ancient, filled with stories of the past."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "It's like we're walking through time. The thought that these rocks were part of the seabed adds a layer of mystery to our hike."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Indeed. And these rocks contribute to the soil's mineral content, creating a unique habitat for various plants, some of which are quite rare."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "As a cook, that piques my curiosity. The idea of using rare, locally-grown herbs and plants in my recipes is quite appealing. Nature's pantry is full of surprises."
            if myrandom == 3:
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Did you know that the sea's proximity plays a big role in the biodiversity of this forest? The saline air impacts the vegetation here, giving rise to unique plant species."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That’s a chef’s delight! The sea's influence could add a subtle twist to the flavors of these plants. I’m already thinking about how to use them in my cooking."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "And there’s more to it. The rocky landscape is a result of ancient geological shifts. This whole area was once under the sea, which is quite mind-boggling."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That’s amazing. To think that the ground we're walking on has such a deep history. It must have a profound effect on the ecosystem here."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "Definitely. The soil, enriched by these ancient rocks, supports a variety of plants. It’s a perfect example of how geology influences ecology."
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I see a new menu in the making! Using ingredients that have grown in this unique environment could be my next big culinary project. Thanks for the inspiration, Lin!"


        "Do you want to take a break?" if lin_fullstage < 4:
            $ linhikingbreak = 1
            $ myrandom = renpy.random.randint(1,3)
            $ position = "linhikingtalksmiling"
            call sceneimg
            if myrandom == 1:
                

                

                player "I brought some food with me, Lin. How about we find a nice spot to sit and enjoy a meal? I've prepared something special."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "That sounds wonderful! I'm actually starving. What did you bring?"
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I made a quinoa salad with fresh herbs and roasted vegetables, and for protein, I've got grilled chicken with a hint of lemon and thyme. Thought it'd be perfect for a hike."
                $ position = "linhikingtalk"
                call sceneimg
                

                Lin "That sounds delicious and just what I need after all this walking. Lead the way to our dining spot!"
                call linhikefeeding
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

               

                Lin "This is incredible! You really know how to make a meal that's both healthy and flavorful. It's the perfect fuel for our hike."
                
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "I'm glad you like it! As a cook, I love creating dishes that are not only tasty but also nourishing, especially for outdoor activities like this."
            if myrandom == 2:
                

                player "Hey Lin, I've brought some food along. How about we stop for a quick bite? I’m sure you must be hungry."

                Lin "That sounds great. I could use a good meal right now. What do you have?"
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I prepared some hearty sandwiches – roasted vegetables and hummus on whole grain bread, and some fresh fruit on the side."
                $ position = "linhikingtalk"
                call sceneimg
                call linhikefeeding
                Lin "Perfect! I love a good sandwich. And fresh fruit is always refreshing after a hike."
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                

                Lin "These sandwiches are fantastic! You really have a knack for combining flavors."
                
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Thanks, Lin! I try to pack meals that are both fulfilling and good for energy. It’s important to keep up the stamina when hiking."
            if myrandom == 3:
                

                player "Lin, let's take a break for a bit. I've got some snacks with me. What do you say we sit down and refuel?"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "That sounds like a plan. I’m pretty hungry. What snacks did you bring?"
                
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I've got some homemade granola bars, packed with nuts and seeds, and some apple slices with almond butter. Thought they'd be a good energy boost."
                $ position = "linhikingcampfiretalklisten"
                call sceneimg
                call linhikefeeding

                Lin "Yum, that sounds exactly like what I need right now. Let's find a nice place to relax and eat."

                

                Lin "These granola bars are amazing! And the apple slices are so refreshing. You really know how to make hiking snacks exciting."
                
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Thanks! I believe good food makes the great outdoors even better. It's all about balancing taste and energy."
            $ linhikingbreak = 0


        "Do you want to take a break?" if lin_fullstage > 3 and linhikebreak == 0 and linhikebreakeat == 0 and linhikejustrest == 0:
            $ linhikebreak = 1
            $ myrandom = renpy.random.randint(1,2)
            if myrandom == 1:
                $ linhikebreakeat = 1
                $ myrandom = renpy.random.randint(1,3)

                $ position = "linhikingtalksurprised"                
                call sceneimg

                if myrandom == 1:
                    

                    player "Lin, I've brought along some food I prepared. Would you like to sit and have a little more? I promise it's light and should be easy on your stomach."
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "I did eat earlier and I'm quite full, but I can't resist trying your cooking. What have you got?"
                
                    $ position = "linhikingtalklisten"
                    call sceneimg


                    player "I've made a simple, refreshing fruit salad with a mix of berries, mint, and a hint of lime. It's light and should be perfect after your earlier meal."
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "That sounds lovely and not too heavy. Let's find a nice spot to sit and enjoy it. Your cooking is always worth making room for!"
                    call linhikefeeding
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg
                  

                    Lin "This is just perfect – light and flavorful. It’s exactly what I needed. You always know how to make food that's appealing yet considerate of how one feels."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "I'm glad you like it. I believe in creating dishes that are not only tasty but also suit the moment, especially when out in nature like this."
                if myrandom == 2:
                    

                    player "Lin, I brought some of my homemade cooking. I understand you've already eaten, but maybe you'd like to try just a little? It's quite light."
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "I am a bit full, but I never pass up a chance to sample your dishes. What did you bring?"
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "I made a small batch of vegetable spring rolls, they're fresh and not too filling. And I have some herbal tea that should be soothing after a big meal."
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "That sounds like it won't be too much for me. Let's sit down and have a taste. Your culinary skills always amaze me."
                    call linhikefeeding
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg
                    

                    Lin "These spring rolls are fantastic, and the tea is just what I needed. You always manage to strike the right balance with your food."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "Thank you, Lin. I try to prepare food that's enjoyable but also considerate of our needs. Good food should always feel good."
                if myrandom == 3:
                    

                    player "Lin, I've got some snacks with me. They're homemade and quite light. Would you like to try some, even though you're a bit full?"

                    Lin "Well, your cooking is always a treat. What snacks did you bring?"
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "I prepared some cucumber and carrot sticks with a light yogurt dip. It's refreshing and shouldn't be too heavy after your meal."
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "That sounds just about right for my current state. Let’s find a spot to relax and snack. Your thoughtful cooking is one of a kind."
                    call linhikefeeding
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg
                    

                    Lin "This is lovely – light, healthy, and tasty. Even though I was full, I'm enjoying every bite. You really have a gift for this."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "Thanks, Lin! I like to make food that’s adaptable to how we feel. It’s all about enhancing the experience without overwhelming."
                $ linhikebreakeat = 0
            if myrandom == 2:        
                $ myrandom = renpy.random.randint(1,3)
                $ position = "linhikingtalksurprised"
                call sceneimg
                if myrandom == 1:
                    

                    player "Lin, I brought some food I made. Would you like to join me for a bite? It's nothing heavy, just a light snack."
                    $ position = "linhikingno"
                    call sceneimg

                    Lin "Thanks for the offer, but I actually ate quite a bit earlier and I'm feeling pretty full right now. I'll have to pass, but I appreciate it."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "No worries at all, Lin. I totally understand. It’s important to listen to your body. We can just find a nice spot to rest and enjoy the view."
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "That sounds perfect, actually. A little break to enjoy the scenery would be great. Thanks for being so understanding."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "If you feel like having a nibble later, just let me know. I’ve got enough to share. For now, let’s just enjoy the tranquility of the forest."
                if myrandom == 2:
                    

                    player "Hey Lin, I’ve packed some of my special homemade snacks. Would you like to have some with me?"
                    $ position = "linhikingno"
                    call sceneimg

                    Lin "I would normally jump at the chance to try your cooking, but I'm actually still quite full from earlier. I think I'll have to pass this time."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "That's completely fine, Lin. We don't have to eat. Maybe we can just find a nice spot to sit and chat instead?"
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "That would be lovely. A nice, relaxing chat sounds just right. Thank you for being so considerate."    
                
                    $ position = "linhikingtalklisten"
                    call sceneimg                

                    player "Whenever you’re ready for a snack, just let me know. No pressure at all. It’s nice just to sit and talk like this."
                if myrandom == 3:
                    

                    player "Lin, I’ve prepared some snacks for our hike. Feel free to join me if you're up for it."
                    $ position = "linhikingno"
                    call sceneimg

                    Lin "I appreciate that, but I actually had a big meal earlier and I'm still feeling the effects. I’ll have to decline this time."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "I understand, no problem at all. Let’s just find a comfortable place to rest for a bit. We can enjoy the surroundings without the snacks."
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "That sounds good to me. A little rest would be great right now. Thanks for being so accommodating."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    

                    player "If you change your mind or feel like a light snack later, just say the word. For now, let’s just relax and enjoy the peace of the forest."
            if myrandom == 3: 
                $ linhikejustrest = 1
                $ myrandom = renpy.random.randint(1,3)

                $ position = "linhikingtalksurprised"                
                call sceneimg

                if myrandom == 1:
                    

               

                    player "Lin, I brought some of my homemade cooking. Would you like to sit and eat with me? It's light and nutritious."
                    $ position = "linhikingno"
                    call sceneimg

                    Lin "I wish I could, but I'm so full right now I could pass for pregnant! I've had two big meals already today and I'm just bloated. I really can't eat another bite."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "I totally understand, Lin. Overeating can be uncomfortable. Let's just find a spot to relax and enjoy the view instead. No pressure to eat."
                    $ position = "linhikingtalk"
                    call sceneimg

                    Lin "That sounds perfect, thank you. I'd hate to decline your cooking otherwise. A quiet sit-down is just what I need right now."

                
                if myrandom == 2:
                    

                    player "Hey Lin, I've got some food here, but it sounds like you're really full. I don't want to make you uncomfortable. How about we just take a break?"
                    $ position = "linhikingno"
                    call sceneimg

                    Lin "Yeah, that's a good idea. I feel so bloated after my earlier meals, I don't think I could fit anything else. I appreciate your understanding."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "Of course, your comfort is important. Let's find a nice place to sit and relax. The food can wait."

                    Lin "Thanks for being so considerate. It's nice just to sit and unwind after eating so much."

                
                if myrandom == 3:
                    

                    player "Lin, I've got some snacks, but it sounds like you're already full to the brim! We don't have to eat; how about we just chill out instead?"
                    $ position = "linhikingno"
                    call sceneimg

                    Lin "That would be great. I'm so stuffed, I feel like I've eaten for two! I definitely need a break from food right now."
                
                    $ position = "linhikingtalklisten"
                    call sceneimg

                    player "No worries, let's find a nice place to take it easy. The food can always be saved for later."

                    Lin "Thanks, that's just what I need. A little rest and relaxation after all that food."


        "But why? Insist on eating" if linhikebreak == 1 and linhikebreakeat == 0:
            $ myrandom = renpy.random.randint(1,3)
            $ position = "linhikingtalksurprised"                
            call sceneimg
            if myrandom == 1:
                

                player "Oh, come on, Lin. You've got a small belly, but there's always room for a little more, especially for something homemade. Give it a try!"
                $ position = "linhikingno"
                call sceneimg

                Lin "Honestly, I'm really full, and I wouldn't want to overdo it. Thanks, but I'll have to pass. I think I might call it a day and head home."

                player "I apologize if I came off too insistent. I didn't mean to make you uncomfortable. Let me know if you need company on the way back."
                $ position = "linhikingwalking"
                call sceneimg

                Lin "No, it's okay. I think I just need to rest up. Thanks for the offer, though. Let's plan another hike soon, maybe on a less full stomach!"
            if myrandom == 2:
                

                player "Are you sure, Lin? There's always a little extra room for something delicious. I made it myself, and it's very light. You won't regret it!"
                $ position = "linhikingno"
                call sceneimg

                Lin "I appreciate your enthusiasm, but I really can't eat any more. Actually, I think I should head back now. I need some time to digest."

                player "Oh, I'm sorry if I overstepped. I just wanted to share something I made. Safe travels back, and let’s catch up another time."
                $ position = "linhikingwalking"
                call sceneimg

                Lin "That sounds good. Thanks for understanding, and sorry to cut our hike short. Let's definitely catch up again soon."

                
            if myrandom == 3:
                

                player "Just a small bite, Lin? I assure you it's very light and won't make you feel overstuffed. I’d love for you to try it."
                $ position = "linhikingno"
                call sceneimg

                Lin "Really, I can't. I'm too full, and I don’t want to feel uncomfortable. I think it's best if I head home now."

                player "I apologize if I was being pushy. It wasn't my intention. Please let me know if you need any assistance getting back."
                $ position = "linhikingwalking"
                call sceneimg

                Lin "No worries, I'll be fine. Thanks for the offer, though. We'll plan another hike soon, maybe on an emptier stomach next time!"
            $ linhikesun = 0
            jump culinarychoices


        
            

        "Suggest Lin to eat just a little" if linhikejustrest == 1 and lin_fullstage < 8:
            $ linhikejustrest = 2
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:                
                $ position = "linhikingcampfiretalklisten"
                call sceneimg
                player "Lin, I've brought some food I made. You seem quite full, but if you're up for it, I can help make it easier for you. How about I serve you a small portion?"
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg
                pause 1.0
                $ position = "linhikingcampfirebellyview"
                call sceneimg
                
                
                Lin "That would be nice, actually. I do feel incredibly bloated – like I'm pregnant! A little bit more wouldn't hurt, especially if you're offering to help."
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg

                player "Sure thing. Let's find a comfortable spot where you can relax. I'll prepare a small, easy-to-digest serving. Just sit back and enjoy."

                Lin "Thank you. I appreciate your help. This way, I can still enjoy your cooking without overdoing it."
                
                call linhikefeeding
            if myrandom == 2:              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Lin, I see you're pretty full, but I'm happy to help you out. Would you like to try just a little of what I've prepared? I can assist so you don't have to strain yourself."
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg
                pause 1.0
                $ position = "linhikingcampfirebellyview"
                call sceneimg

                Lin "That's very kind of you. I am pretty bloated – might as well look the part of being pregnant! A small taste of your cooking would be lovely, especially with your help."              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Alright, let's get settled then. I'll take care of everything. You just sit back and tell me if you want more or if it's enough."
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg

                Lin "Thanks, I really appreciate it. Your care makes this offer hard to refuse."
                call linhikefeeding
                
            if myrandom == 3:              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Lin, I understand you're feeling quite full. How about I help you with a very small portion? It should be manageable, and I'll make sure you're comfortable."
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg
                pause 1.0
                $ position = "linhikingcampfirebellyview"
                call sceneimg

                Lin "That sounds good. I'm so full I could pass for pregnant, but I don't want to miss out on your cooking. A little help would be great."              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Let's find a nice spot then. You can relax, and I’ll serve you a bit of food. We'll take it slow and easy."
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg

                Lin "Thank you for being so considerate. A bit of your delicious cooking, with your help, sounds perfect right now."
                call linhikefeeding

        "Talk to Lin" if linhikejustrest == 1 and lin_attitude <= 400:
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg
                

                Lin "Sitting here, resting in the forest, it's the perfect time to tell you how much I enjoy your cooking. It's always so flavorful and hearty."
                $ position = "linhikingcampfirebellyview"
                call sceneimg
                player "Thank you, Lin. It means a lot coming from you. I'm glad you can still enjoy it, even though you're a bit full right now."
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg
                Lin "Oh, this slight bloat is nothing! Your dishes are worth a little extra fullness. They have this homely yet sophisticated touch that's hard to find."              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "That's exactly what I aim for in my cooking – a balance between comfort and a culinary adventure. I'm happy to hear it resonates with you."
            if myrandom == 2:              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                Lin "This is such a peaceful spot to relax. And, you know, every time you cook, it's a treat. Your meals are so well thought out and delicious."
                $ position = "linhikingcampfirebellyview"
                call sceneimg
                player "Thanks, Lin. I'm glad you enjoy them, even if you're feeling a bit bloated right now. I always hope my dishes bring joy."
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg

                Lin "Absolutely, they do! A little bloat is a small price to pay for such delightful flavors. You have a real talent for combining ingredients."              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "I appreciate that. Cooking is my way of expressing creativity, and it's wonderful to share that with friends who appreciate it."
            if myrandom == 3:              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                Lin "Resting here, with nature all around us, it's a perfect moment to tell you how much I enjoy your culinary creations. They’re always so inviting and tasty."
                $ position = "linhikingcampfirebellyview"
                call sceneimg
                player "That's so kind of you to say, Lin. I'm glad you can enjoy them, even with a bit of bloat. Good food is meant to be shared and savored."
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg

                Lin "Your cooking is always worth a little extra fullness. There's something about your dishes that's comforting yet exciting at the same time."              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Thank you, Lin. I try to put a piece of my heart into every dish. Knowing that it brings happiness to others is the best reward."


        "Talk to Lin about her belly" if linhikejustrest == 1 and lin_attitude > 90:
            $ myrandom = renpy.random.randint(1,3)
            
            if myrandom == 1:
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg

                Lin "I can't believe how bloated I am right now. It's surprising, especially since I usually watch what I eat. But I just can't help myself with your cooking. It's always so good."              
                $ position = "linhikingcampfirebellyview"
                call sceneimg

                player "I'm really flattered you enjoy my dishes so much, Lin. But I hope you're not feeling too uncomfortable. It's important to listen to your body."

                Lin "Oh, it's a bit uncomfortable, but worth it. I'm just not used to feeling this full. Your cooking has a way of tempting me beyond my usual limits!"              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Well, I'm glad you like it, but I wouldn't want you to overdo it on my account. Next time, I'll make sure to prepare something light and easy."
            if myrandom == 2:
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg

                Lin "This is unusual for me. I'm so bloated! I always keep an eye on my diet, but your food is just irresistible. Look at my belly! It's like I'm carrying a food baby!"              
                $ position = "linhikingcampfirebellyview"
                call sceneimg

                player "I take it as a compliment that you enjoy my cooking so much, Lin. But I hope you're not too uncomfortable. We can always adjust the menu next time."

                Lin "It's a bit of a shock to see my belly this full, but your meals are always a culinary adventure. Maybe I just need to indulge once in a while."              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "Absolutely, Lin. It's all about balance. Enjoying good food is one of life's pleasures. Next time, we can go for something lighter."
            if myrandom == 3:
                $ position = "linhikingcampfirelookingatthebellytalk"
                call sceneimg

                Lin "I'm genuinely surprised at myself. Look at how bloated I am! I'm usually so careful with my diet, but your cooking is something else. It's hard to resist."              
                $ position = "linhikingcampfirebellyview"
                call sceneimg

                player "Your enjoyment of my cooking means a lot, Lin. But your comfort is important too. It's okay to indulge, but we don't want to overdo it."

                Lin "True, I guess I got a bit carried away. Your food just brings out a different side of me. It's worth a little bloating now and then!"              
                $ position = "linhikingcampfiretalklisten"
                call sceneimg

                player "I'm glad to hear you like it so much. But let's make sure you're comfortable next time. We can find the perfect balance between taste and health."


        "Suggest Lin to eat just a little" if linhikejustrest == 1 and lin_fullstage > 7:
            $ myrandom = renpy.random.randint(1,2)
            $ position = "linhikingtalksurprised"                
            call sceneimg
            pause 1
            if myrandom == 1:
                
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:              
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "Since you find my cooking so irresistible, would you like to try just a little more? I have some left."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "Oh, as much as I'm tempted by your amazing cooking, I think I'll have to pass this time. I honestly feel like I'm going to explode already!"             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "I completely understand, Lin. It's important not to push ourselves too much. Let's just relax and enjoy the nature around us."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "That sounds perfect. Thanks for being so understanding. Your cooking is always a treat, but right now, just sitting and resting feels great."

                    
                if myrandom == 2:             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "Are you sure you don't want just a tiny bit more of my cooking? It's hard to resist, I know!"
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "Your food is fantastic, but no more for me today. I feel like I'm on the brink of bursting! I've reached my limit."             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "Alright, I won't tempt you further. Let's give your stomach a well-deserved break and just relax here."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "Thank you! Some rest is exactly what I need right now. This is what I get for not being able to resist your culinary magic!"

                    
                if myrandom == 3:             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "If you're up for it, I still have some food left. Maybe a little more to tantalize your taste buds?"
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "I’d normally never say no to your cooking, but I really feel like I'm at my limit. Any more and I might just pop!"             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "I respect that, Lin. We'll save it for another time. For now, let's just relax and enjoy this peaceful moment."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "That sounds like a plan. Sitting here, taking in the peace of the forest – it's the perfect way to digest such a great meal."

            if myrandom == 2:
                $ linhikeexplodingeat = 1
                $ myrandom = renpy.random.randint(1,3)
                if myrandom == 1:             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "It's great to hear you love my cooking that much. How about just a small bite then? Something light that won’t make you feel too full."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "Well, when it comes to your cooking, I really feel like I have no limits. I'm almost at the point of exploding, but I can't resist a small taste of your delicious food."             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "Alright, I’ll prepare just a little for you, something very light. We don't want to push your limits too much."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "That sounds perfect. A tiny bit more of your culinary magic won’t hurt, I guess. I just can’t say no to it!"
                    call linhikefeeding
                if myrandom == 2:             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "If you're sure a small bite won't be too much, I'd be happy to serve you a little. I always want my food to be a pleasure, never a burden."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "I might be on the edge, but I can't help myself. Your cooking is just too good. A tiny bit more should be fine. I trust your judgment."             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "Okay, I'll make sure it's just a small amount. Something to savor without overdoing it."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "Thanks, I appreciate it. It’s hard to resist your dishes, even when I’m this full!"
                    call linhikefeeding
                if myrandom == 3:             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "Well, if a small bite is what you'd like, I’m happy to oblige. But let’s keep it really small. I don’t want you to be uncomfortable."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "Yeah, just a tiny bit more should be okay. Your dishes are irresistible, and I guess I do have quite an appetite for them!"             
                    $ position = "linhikingcampfiretalklisten"
                    call sceneimg

                    player "I’ll get something very light then. It’s always a pleasure to share my cooking, especially with someone who enjoys it so much."
                    $ position = "linhikingcampfirelookingatthebellytalk"
                    call sceneimg

                    Lin "Thanks, I really can’t turn down an offer to taste your food, even with a belly this full!"
                    call linhikefeeding


        



        # "Set up a fire" if linhikejustrest == 1 and linhikefire == 0: 
        #     $ linhikefire = 1
        #     $ myrandom = renpy.random.randint(1,3)
        #     if myrandom == 1:
        #         $ position = "linsittingnofirefromtheback"
        #         call sceneimg
                

        #         player "Let's make this a bit more special. I'll set up a fire for us. It'll create a cozy atmosphere for our meal."

        #         Lin "That sounds lovely, but are you sure it's not too much work?"

        #         player "Not at all. I love making a fire. It adds a certain charm to outdoor dining. Just relax and I'll have it ready in no time."

        #         $ position = "linsittingcampfirefromtheback"
        #         call sceneimg

        #         Lin "You really know how to create a perfect setting. A fire makes everything more magical."

        #         player "Exactly! It’s about the whole experience, not just the food. There’s nothing like a meal cooked over an open fire."

                

        #         Lin "I'm already loving this. The warmth and the light from the fire, it's so comforting."

        #         player "I’m glad you think so. Now, let's get cooking. This fire will give a wonderful flavor to our meal."

                
        #     if myrandom == 2:
        #         $ position = "linsittingnofirefromtheback"
        #         call sceneimg

        #         player "I think a fire would be perfect for us right now. It'll add a rustic touch to our meal. Let me set one up."

        #         Lin "That sounds incredible. But only if it's not too much trouble for you."

        #         player "I enjoy doing it. A fire in the great outdoors is the best kitchen a cook could ask for. Just sit back and watch the magic happen."

        #         $ position = "linsittingcampfirefromtheback"
        #         call sceneimg

        #         Lin "You're full of surprises! A fire really elevates the whole experience."

        #         player "I believe the setting is as important as the meal itself. Cooking over a fire brings out unique flavors you just can't get any other way."

                

        #         Lin "This is amazing. The fire, the forest around us, and your cooking – it's an unbeatable combination."

        #         player "That's the spirit! Let's enjoy this to the fullest. A good meal is all about the ambiance as well."

                
        #     if myrandom == 3:
        #         $ position = "linsittingnofirefromtheback"
        #         call sceneimg

        #         player "How about we add a little more adventure to our meal? I'll set up a fire. It should make our dining experience even more enjoyable."

        #         Lin "That sounds exciting, but don't go to any extra effort on my account."

        #         player "It's no effort at all. In fact, it's a pleasure. There's something special about cooking and eating by a fire."

        #         $ position = "linsittingcampfirefromtheback"
        #         call sceneimg

        #         Lin "You really are a master of all trades. A fire makes it feel like a real outdoor adventure."

        #         player "Well, I believe in the full culinary experience. A fire not only cooks the food but also adds a unique ambiance."

                

        #         Lin "This is so nice. The crackling fire and the open air – it's like a mini-vacation."

        #         player "Exactly my thoughts. Now, let's cook something amazing with this fire. It's going to be a meal to remember."

        


        "Time to go home":
            $ linhikesun = 0
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:

                $ position = "linhikingtalklisten"
                call sceneimg
                

                player "Lin, this hike was just what I needed. Thanks for suggesting it and keeping such great company."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "I'm really glad you enjoyed it. It's always more fun with a friend. Let’s do this again soon!"
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Definitely, count me in. It's always a pleasure hiking with you. Have a great rest of your day!"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "You too! Make sure to rest up after today's trek. Take care, and I'll see you soon."
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Thanks, Lin. See you around!"
            if myrandom == 2:
                $ position = "linhikingtalklisten"
                call sceneimg

                player "That was an amazing hike, Lin! I had a great time exploring the trails with you."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "It was a blast, wasn't it? Good company makes all the difference. We should plan another hike like this."
                $ position = "linhikingtalklisten"
                call sceneimg

                player "I'm already looking forward to it. Thanks for a wonderful day out. Rest well tonight!"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "You too! Thanks for joining me today. See you next time!"
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Definitely, take care, Lin!"
            if myrandom == 3:
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Lin, today's hike was fantastic. I really appreciate you showing me these trails."
                $ position = "linhikingtalk"
                call sceneimg

                Lin "I’m happy to share them with you. Hiking is always more enjoyable with company. Let's hit another trail soon."

                player "I'd love that. Thanks for today, it was a great experience. Have a good evening!"
                $ position = "linhikingtalk"
                call sceneimg

                Lin "You too! Take care of yourself, and let's catch up again for another hike."
                $ position = "linhikingtalklisten"
                call sceneimg

                player "Sounds perfect. See you soon, Lin!"
            jump culinarychoices




    jump linhiking
        