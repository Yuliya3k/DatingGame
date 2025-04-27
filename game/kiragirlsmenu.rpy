label kiragirlsmenu:

    menu:
        "Kira, you must meet all sorts of people here. Tell me about Ha-Yoon" if hayoonintro == 0:
        

            Kira "Oh, absolutely! Well, there's Ha-Yoon, the town's brilliant doctor."
            $ position = "hayoonintro"
            call sceneimg
            Kira " Dr. Ha-Yoon is a dedicated and compassionate doctor who works tirelessly to heal and care for the residents of Urbana. With a gentle demeanor and a wealth of medical knowledge, she stands as a pillar of support for those in need. Beyond her professional skills, Ha-Yoon also has a deep love for traditional herbal remedies, and she often finds herself experimenting with unique concoctions to soothe ailments. Her kind-hearted nature and dedication to her work make her a beloved figure in the city."
            $ hayoonintro = 1

        "Kira, I'm new in town, and I'd love to know about some intriguing people around here. Tell me about Lin" if linintro == 0:

            Kira "Welcome to the city! Let me tell you about Lin. "
            $ position = "linintro"
            call sceneimg
            Kira "Lin is a fitness enthusiast and a highly motivated personal trainer who believes in the power of physical and mental strength. With her chiseled physique and unwavering determination, she inspires countless individuals to push their limits and embrace a healthy lifestyle. Lin's training sessions are known for their intensity, but also for the camaraderie she fosters among her clients. Beyond the gym, she loves spending time outdoors, hiking, and participating in athletic events."
            $ linintro = 1

        "Kira, I've heard this town has its fair share of characters. Can you introduce me Ava?" if avaintro == 0:

            Kira "Absolutely! You should meet Ava, the lifeguard at the local beach." 
            $ position = "avaintro"
            call sceneimg
            Kira "Ava is a lifeguard who takes her duty of ensuring safety at the city's beaches and pools very seriously. With her strong swimmer's build and sharp attention to detail, she is always on the lookout for potential hazards. Despite her serious demeanor while on duty, Ava has a playful side that emerges when she's off the clock. She's an avid surfer and enjoys teaching newcomers the joys of riding the waves. Ava's dedication to her job and her love for the water make her a respected figure along the coastline."
            $ avaintro = 1

        "Hey, Kira. I'm curious about the locals. Tell me about Sally" if sallyintro == 0:

            Kira "Well, Sally, the maid at the luxurious mansion down the road, is quite the mystery. "
            $ position = "sallyintro"
            call sceneimg
            Kira " Sally is a cheerful and enthusiastic maid who takes pride in her work of maintaining the city's elegant homes and establishments. Her attention to detail is unparalleled, and she's known for transforming even the messiest spaces into showcases of cleanliness and order. Beyond her professional responsibilities, Sally harbors a love for gardening and spends her free time cultivating colorful blooms that add beauty to the city. Her positive outlook and commitment to her craft make her a cherished member of the Urbana community."
            $ sallyintro = 1

return