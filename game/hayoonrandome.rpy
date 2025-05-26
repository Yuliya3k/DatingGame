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


            menu:
                "Ask if she usually reads here?":

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

                "What's your books of choice?":
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
        "Just go":
            
            return

    

    return