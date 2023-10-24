label aurorafirstmeet:

    #firsttalk
    if aurorafirstmeet == 1:
        $ position = "auroraexplain"
        call sceneimg
        $ aurorafirstmeet = 2
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            $ position = "aurorahey"
            call sceneimg
            player "Hello there! Lovely day for gardening, isn't it?"
            $ position = "aurorahello"
            call sceneimg
            Aurora "Oh, it is, indeed. Gardening is my little slice of heaven. Helps keep things in order, you know?"
            $ position = "auroragardening"
            call sceneimg
            player "I can see that. Your garden looks amazing. I'm [name], by the way, just moved into the neighborhood."
            $ position = "auroraexplain"
            call sceneimg
            Aurora "Nice to meet you. I'm Aurora. My husband, Mark, usually helps with the gardening, but he's off running errands today."
            $ position = "auroragardening"
            call sceneimg
            player "Thank you, Aurora. I might take you up on that offer. Your garden really is impressive. Did you do all of this yourself?"
            $ position = "auroraexplain"
            call sceneimg
            Aurora "Mostly, yes. Mark helps with the heavy lifting sometimes, and our son, Ethan, well, he's more of a supervisor, making sure everything's to his liking."
            $ position = "auroragardening"
            call sceneimg
            player "Sounds like a team effort. I'm looking forward to getting to know the neighborhood better."
            $ position = "auroraexplain"
            call sceneimg
            Aurora "It's a wonderful place with some lovely folks around. And if you ever want some gardening tips or need help with anything else, don't hesitate to ask."

            player " I'll keep that in mind. Thanks again, Aurora. Enjoy your gardening!"
            $ position = "auroragardening"
            call sceneimg
            Aurora "You too. Have a great day!"

        if myrandom == 2:
            $ position = "aurorahey"
            call sceneimg
            player "Hello there! Lovely day for gardening, isn't it?"
            $ position = "aurorahello"
            call sceneimg
            Aurora "Oh, it is, indeed. Gardening is my little slice of heaven. Helps keep things in order, you know?"
            $ position = "auroragardening"
            call sceneimg
            player "I can see that. Your garden looks amazing. I'm [name], by the way, just moved into the neighborhood."
            $ position = "auroraexplain"
            call sceneimg
            Aurora "Nice to meet you. I'm Aurora. If you ever need any help settling in, just let us know."
            $ position = "auroragardening"
            call sceneimg
            player "Thank you, Aurora. Your garden is impressive. Did you do all of this yourself?"
            $ position = "auroraexplain"
            call sceneimg
            Aurora "Mostly, yes. I have some occasional helpers around."
            $ position = "auroragardening"
            call sceneimg
            player "Sounds like a community effort. I'm looking forward to getting to know the neighborhood better."
            $ position = "auroraiwish"
            call sceneimg
            Aurora "It's a wonderful place with some lovely folks around. And if you ever want some gardening tips or need help with anything else, don't hesitate to ask."
            $ position = "auroragardening"
            call sceneimg
            player " I'll keep that in mind. Thanks again, Aurora. Enjoy your gardening!"
            $ position = "auroragardening"
            call sceneimg
            Aurora "You too. Have a great day!"

        if myrandom == 3:
            $ position = "aurorahey"
            call sceneimg
            player "Hello there! Lovely day for gardening, isn't it?"
            $ position = "aurorahello"
            call sceneimg
            Aurora "Oh, it is, indeed. Gardening is my little slice of heaven. Helps keep things in order, you know?"
            $ position = "auroragardening"
            call sceneimg
            player "I can see that. Your garden looks amazing. I'm [name], by the way, just moved into the neighborhood."
            $ position = "auroraexplain"
            call sceneimg
            Aurora "Nice to meet you. I'm Aurora. Mark's inside, and our son, Ethan, is probably playing in the yard. We've been here for a while now. If you ever need any help settling in, just let us know."
            $ position = "auroragardening"
            call sceneimg
            player "Thank you, Aurora. I might take you up on that offer. Your garden really is impressive. Did you do all of this yourself?"
            $ position = "auroraexplain"
            call sceneimg
            Aurora "Mostly, yes. Mark helps with the heavy lifting sometimes, and Ethan... well, he's more of a supervisor, making sure everything's to his liking."
            $ position = "auroragardening"
            call sceneimg
            player "Sounds like a team effort. I'm looking forward to getting to know the neighborhood better."
            $ position = "auroraexplain"
            call sceneimg
            Aurora "It's a wonderful place with some lovely folks around. And if you ever want some gardening tips or need help with anything else, don't hesitate to ask."
            $ position = "auroragardening"
            call sceneimg
            player " I'll keep that in mind. Thanks again, Aurora. Enjoy your gardening!"
            $ position = "auroragardening"
            call sceneimg
            Aurora "You too. Have a great day!"
        jump culinarychoices

    if aurorafirstmeet == 2:
        $ position = "auroragardening"
        call sceneimg
        label auroratalk1:
            if aurorahi == 0:
                $ position = "auroraexplain"
                call sceneimg
                $ aurorahi = 1
                player "Hey, Aurora! How's it going?"
                $ position = "aurorahello"
                call sceneimg
                Aurora "Oh, hi there! I'm just tending to my garden, as you can see."
            menu:
                "Ask about Ethan" if ethan == 0:
                    $ ethan = 1
                    $ myrandom = renpy.random.randint(1,3)
                    if myrandom == 1:
                        $ position = "auroragardening"
                        call sceneimg
                        player "How old is Ethan?"
                        $ position = "auroraexplain"
                        call sceneimg
                        Aurora "Ethan just turned seven last month. He's growing up so fast, it's hard to believe."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Time does have a way of flying by. What's Ethan like? Is he into gardening and eco-activism like you?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Well, he's still figuring out his interests, but he does enjoy helping me in the garden sometimes. He's more into exploring the park and playing by the ocean. And he's got a heart of gold, always curious and kind."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Sounds like you've got an amazing family. It must be nice living in such a close-knit community with them."
                        $ position = "auroraexplain"
                        call sceneimg
                        Aurora "It truly is. We all value what this town has to offer, from the ocean to the park and the sense of belonging. If you ever want to meet Ethan or Mark, just let me know. We'd love to have you over for a visit."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Thanks, Aurora. I'll definitely take you up on that offer one day. Family and community are what make a place feel like home."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "I couldn't agree more. Enjoy your day, and if you have any more questions or just want to chat, you know where to find me."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Will do, Aurora. Have a wonderful day too!"

                    if myrandom == 2:
                        $ position = "auroragardening"
                        call sceneimg
                        player "I'm still getting used to the town, but it's starting to feel like home. By the way, you mentioned your son Ethan the other day. How old is he?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Ethan just turned seven last month. He's growing up so fast."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's a great age! What does he like to do for fun?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Oh, he's quite the explorer. He loves spending time at the park by the ocean, and he's got a knack for finding the most interesting seashells. He's also a budding artist. His drawings of the ocean and the creatures in it are something to behold."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Sounds like you have a little marine biologist and artist in the making."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "You might be right! I encourage his curiosity and creativity as much as I can. It's important to foster his love for the environment too, given my work."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's wonderful. It must be fulfilling to see him take an interest in the same things you're passionate about."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "It really is. And it's a joy to watch him grow and learn every day. If you ever want to meet him or join us for one of our beachcombing adventures, you're more than welcome."
                        $ position = "auroragardening"
                        call sceneimg
                        player "I'd love to meet Ethan someday. And exploring the beach with you both sounds like a fantastic way to spend a day. Thanks for the invite, Aurora."
                        $ position = "auroragardening"
                        call sceneimg
                        Aurora "Anytime. Just let me know when you're up for it. Enjoy your day!"

                    if myrandom == 3:
                        $ position = "auroragardening"
                        call sceneimg
                        player "You mentioned your son, Ethan, earlier. How old is he?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Ethan just turned seven last month. He's growing up so fast."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's a wonderful age. Is he as passionate about the environment as you are?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Well, he's getting there. He loves spending time outdoors, and he's really curious about nature. We do little eco-friendly activities together, like planting flowers and learning about local wildlife."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That sounds like a great way to teach him about the environment from a young age."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "I believe it's important to instill a love for nature and a sense of responsibility towards it from a young age. It's our world, after all, and future generations need to take care of it."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Absolutely, you're doing a fantastic job as a parent, Aurora."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Thank you. It's not always easy, but it's incredibly rewarding. Parenthood has a way of making you see the world through fresh eyes."
                        $ position = "auroragardening"
                        call sceneimg
                        player "I can only imagine. Well, if you ever need a hand with anything or someone to watch over Ethan while you're working on your eco-projects, don't hesitate to ask."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "That's very kind of you. I might take you up on that offer sometime. We're lucky to have such a supportive community here."
                        $ position = "auroragardening"
                        call sceneimg
                        player "We certainly are. It's been great chatting with you, Aurora. I'll let you get back to your gardening."
                        $ position = "auroragardening"
                        call sceneimg
                        Aurora "Likewise. Enjoy the rest of your day!"

                "Ask about Mark" if mark == 0:
                    $ mark = 1
                    if myrandom == 1:
                        player "Aurora, you mentioned your husband, Mark, earlier. What does he do for a living?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Mark works as an environmental engineer. He's just as passionate about the environment as I am, if not more."
                        $ position = "auroragardening"
                        call sceneimg
                        player "An environmental engineer? That sounds like important work."
                        $ position = "auroraiwish"
                        call sceneimg
                        
                        Aurora "It is. He's involved in projects that focus on sustainable infrastructure and green technologies. It's his way of contributing to a greener, more sustainable future."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's fascinating. Do you both often find yourselves discussing environmental topics at home?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Oh, all the time. Our dinner table conversations usually revolve around the latest developments in eco-friendly technologies or ways to reduce our carbon footprint."
                        $ position = "auroragardening"
                        call sceneimg
                        player "It sounds like a household committed to making a difference."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "We believe in practicing what we preach. It's not always easy, but we do our best to lead by example."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's admirable. You and Mark are doing fantastic work for the environment."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Thank you. We're just doing our part, like so many others in our community. Every small action counts."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Well, it's been great getting to know you, Aurora. If there's ever an opportunity for me to join in or help out with your environmental initiatives, count me in."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "That means a lot. We're always happy to have more hands on deck. Let's work together for a healthier planet."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Absolutely. Have a wonderful day, Aurora."
                        $ position = "auroragardening"
                        call sceneimg
                        Aurora "You too. Enjoy the beauty of nature around us."

                    if myrandom == 2:
                        $ position = "auroragardening"
                        call sceneimg
                        player "Aurora, you've told me about Ethan, but what about your husband, Mark? What does he do?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Ah, Mark is quite the character. He's an architect, you know, and he's been working on some fascinating projects lately."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That sounds intriguing. What kind of projects is he involved in?"
                        $ position = "auroraiwish"
                        call sceneimg

                        Aurora "Well, his latest project is designing eco-friendly, energy-efficient homes. He's passionate about sustainable architecture, just like I am about the environment."
                        $ position = "auroragardening"
                        call sceneimg
                        player "It seems like you two make a dynamic duo with your shared passions for eco-friendliness."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "We do try. It's important to us that our work aligns with our values. And it's great because we inspire each other to make a positive impact."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's wonderful to hear. You and Mark must have some interesting conversations."
                        $ position = "auroraiwish"
                        call sceneimg

                        Aurora "Oh, we definitely do. Our dinner table discussions are often about innovative building materials, green technologies, and, of course, how we can make our own home more eco-friendly."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Have you made any eco-friendly changes to your home recently?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora " (thoughtful) Yes, we've installed solar panels, improved insulation, and even started composting. Small steps, but they add up."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Those are significant steps towards sustainability. You two are an inspiration."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Thank you. We believe that leading by example is the best way to inspire change. If you ever want tips on making your own home more eco-friendly, feel free to ask."
                        $ position = "auroragardening"
                        call sceneimg
                        player "I'll keep that in mind. It's been great learning more about your family, Aurora."
                        $ position = "auroragardening"
                        call sceneimg
                        Aurora "Likewise. It's nice to have friendly neighbors who care about what's important."

                    if myrandom == 3:
                        $ position = "auroragardening"
                        call sceneimg
                        player "Aurora, you mentioned your husband, Mark, earlier. What does he do?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Mark works as an environmental engineer. He's just as passionate about the environment as I am, maybe even more so."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's fantastic! It must be great having a partner who shares your values and interests."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "It really is. We met at a sustainability conference a few years ago, and it was like finding my other half. We make a good team, both at home and in our eco-projects."
                        $ position = "auroragardening"
                        call sceneimg
                        player "It sounds like a match made in environmental heaven. Do you two often collaborate on projects together?"
                        $ position = "auroraiwish"
                        call sceneimg

                        Aurora "Absolutely. We've worked on various initiatives, from community clean-up events to designing eco-friendly systems for local businesses. It's wonderful to have a partner who not only understands but actively supports your goals."
                        $ position = "auroragardening"
                        call sceneimg
                        player "I can see why you both are so dedicated to your work. It's inspiring."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Thank you. We believe that change begins at home, and our family is committed to living as sustainably as possible."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Do you have any eco-friendly tips for someone like me who's new to town and wants to make a positive impact?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Of course! Start with simple changes like reducing single-use plastics, composting your kitchen scraps, and supporting local farmers' markets for fresh produce. And, if you're interested, you can always join one of our eco-workshops or events. We'd love to have you."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Those are great suggestions, Aurora. I'll definitely keep them in mind. Thanks for sharing, and it's been a pleasure getting to know you better."
                        $ position = "auroragardening"
                        call sceneimg
                        Aurora "Likewise. Feel free to reach out if you ever want to chat more about eco-friendly living or anything else. Have a wonderful day!"


                "Ask what is Aurora doing for life" if auroraforliving == 0:
                    $ auroraforliving = 1
                    if myrandom == 1:
                        $ position = "auroragardening"
                        call sceneimg
                        player "I'm still getting used to the town, but it's starting to feel like home. By the way, I've been meaning to ask, what do you do for a living, Aurora?"
                        $ position = "auroraexplain"
                        call sceneimg
                        Aurora "Well, I'm an eco-activist and PR manager by profession. I work for a local environmental organization here in town."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That sounds fascinating. What kind of work does your organization do?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "We focus on promoting sustainable and eco-friendly practices in our community. We organize events, workshops, and awareness campaigns on topics like recycling, reducing plastic waste, and conserving energy."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's important work. It's great to see people dedicated to making a positive impact on the environment."
                        $ position = "auroraiwish"
                        call sceneimg

                        Aurora "Thank you. Every little bit counts, and I believe that collectively, we can make a significant difference. If you ever want to get involved or learn more, just let me know. We're always looking for volunteers."
                        $ position = "auroragardening"
                        call sceneimg
                        player "I'll keep that in mind. It's fantastic to have someone like you in the community, Aurora, working towards a greener future."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "I appreciate that. And it's always nice to have neighbors who care about the environment too. If you ever need gardening tips or just want to chat, feel free to drop by."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Thanks, Aurora. I'll definitely take you up on that offer. Have a great day!"
                        $ position = "auroragardening"
                        call sceneimg
                        Aurora "You too. Enjoy your day!"

                    if myrandom == 2:
                        $ position = "auroragardening"
                        call sceneimg
                        player "I'm still getting used to the town, but it's starting to feel like home. By the way, I've been meaning to ask, what do you do for a living, Aurora?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Well, I'm an eco-activist and PR manager by profession. I work for a local environmental organization here in town."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That sounds fascinating. What kind of work does your organization do?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "We focus on promoting sustainable and eco-friendly practices in our community. We organize events, workshops, and awareness campaigns on topics like recycling, reducing plastic waste, and conserving energy."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's important work. It's great to see people dedicated to making a positive impact on the environment."
                        $ position = "auroraiwish"
                        call sceneimg

                        Aurora "Thank you. Every little bit counts, and I believe that collectively, we can make a significant difference. If you ever want to get involved or learn more, just let me know. We're always looking for volunteers."
                        $ position = "auroragardening"
                        call sceneimg
                        player "I'll keep that in mind. It's fantastic to have someone like you in the community, Aurora, working towards a greener future."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "I appreciate that. And it's always nice to have neighbors who care about the environment too. If you ever need gardening tips or just want to chat, feel free to drop by."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Thanks, Aurora. I'll definitely take you up on that offer. Have a great day!"
                        $ position = "auroragardening"
                        call sceneimg
                        Aurora "You too. Enjoy your day!"

                    if myrandom == 3:
                        $ position = "auroragardening"
                        call sceneimg
                        player "I'm still getting used to the town, but it's starting to feel like home. By the way, I've been meaning to ask, what do you do for a living, Aurora?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Well, I'm an eco-activist and PR manager by profession. I work for a local environmental organization here in town."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That sounds fascinating. What kind of work does your organization do?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "We focus on promoting sustainable and eco-friendly practices in our community. We organize events, workshops, and awareness campaigns on topics like recycling, reducing plastic waste, and conserving energy."
                        $ position = "auroragardening"
                        call sceneimg
                        player "That's important work. It's great to see people dedicated to making a positive impact on the environment."
                        $ position = "auroraiwish"
                        call sceneimg

                        Aurora "Thank you. Every little bit counts, and I believe that collectively, we can make a significant difference. If you ever want to get involved or learn more, just let me know. We're always looking for volunteers."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Is there a particular project or initiative you're working on right now that you're excited about?"
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Actually, yes! We're planning a community tree-planting event in the park by the ocean. It's going to be a wonderful day of environmental action and camaraderie. You should join us!"
                        $ position = "auroragardening"
                        call sceneimg
                        player "That sounds like a fantastic idea. Count me in! Let me know when it's happening."
                        $ position = "auroraexplain"
                        call sceneimg

                        Aurora "Will do. It'll be great to have you there. If you have any questions about gardening or anything else in the meantime, just swing by."
                        $ position = "auroragardening"
                        call sceneimg
                        player "Thanks, Aurora. I'm looking forward to getting more involved in the community and making a positive impact."
                        $ position = "auroragardening"
                        call sceneimg
                        Aurora "I have no doubt you will. Enjoy your day!"
                "Nothing for now, see you!":
                    $ position = "aurorahello"
                    call sceneimg
                    Aurora "See you!"
                    jump culinarychoices
            jump auroratalk1

    

    return