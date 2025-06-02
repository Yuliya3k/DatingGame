label rm:
    $ myrandom = renpy.random.randint(1,10)
    if myrandom > 5 and hayoonfirstmeet == 1:
        call hayoonrandome


    call closescreens
    play music "audio/rmkitchen.mp3" volume 0.3
    

    

    $ myrandom = renpy.random.randint(1,3)
    if margofirsttime == 0:
        $ position = "kitchen"
        call sceneimg
        "As I pushed open the swinging door that led from the restaurant's dining area into the bustling kitchen, a sense of anticipation and responsibility washed over me. I couldn't help but marvel at the gleaming stainless steel equipment that surrounded me."
        "The kitchen was alive with the hum of machinery and the smell of culinary wonders in the making. It was a chef's paradise, and for the first time, it was all mine to command."

        "The thought hit me like a tidal wave. This was it. My dream job. The culmination of years of hard work, culinary school, and countless hours spent perfecting my craft. The bustling kitchen was my canvas, and the dishes I prepared would be my masterpieces."

        "For a moment, I stood there, taking it all in, feeling the weight of responsibility and opportunity on my shoulders. I knew that the orders would start pouring in soon, and I had to be ready to orchestrate this culinary symphony."

        "Just as I was lost in my thoughts, I heard the unmistakable sound of footsteps approaching from behind. I turned around instinctively, stepping back to ensure I wasn't blocking the path. And there she was, Margo, our manager, a no-nonsense woman with an air of authority that demanded respect."      

        "She looked at me, her eyes sizing me up for a moment, and then she offered a small but encouraging smile."
        $ position = "margohismile"
        call sceneimg
        Margo "Hello there, you must be the new face in our kitchen. I'm Margo, the manager of this fine establishment. And you are?"
        $ position = "margormlistening"
        call sceneimg 
        player "I'm  nice to meet you, Margo."
        $ position = "margormexplaining"
        call sceneimg
        Margo "Likewise. I'm thrilled to have you on board. You'll find we take our work seriously here, but we also value teamwork and a positive attitude. Our restaurant prides itself on providing impeccable service to our guests. Remember, they're not just customers; they're our patrons, and their satisfaction is our top priority."
        $ position = "margormlistening"
        $ margofirsttime = 1
        call sceneimg 
        menu:
            "I understand, Margo. I've always believed in putting the customer first.":
                $ position = "margormtalking"
                call sceneimg
                Margo "Excellent. That's the spirit. Our clients are the most important people in this restaurant, and their demands are the law. We're here to cater to their tastes and preferences, so always be attentive and responsive to their needs."
                $ position = "margormlistening"
                call sceneimg 
                player "Got it, Margo. I'll do my best to ensure they have a memorable dining experience."
                $ position = "margormgoodluck"
                call sceneimg
                Margo "That's what I like to hear. We have a fantastic team here, and I'm sure you'll fit right in. If you ever have questions or need guidance, feel free to reach out. We're here to support each other and provide exceptional service."
                $ position = "margormlistening"
                call sceneimg 
                player "Thank you, Margo. I'm eager to contribute to the team and help uphold the high standards of this restaurant."
                $ position = "margormtalking"
                call sceneimg
                Margo "I have no doubt you will. Welcome to the team, and good luck."
                $ position = "margormlistening"
                call sceneimg 
                player "Thank you, Margo. I'm looking forward to it."
                $ rmclients = 1


        
            "I appreciate that, Margo, but I've always believed in focusing on the culinary aspect of things more than the customer service side.":
                $ position = "margormtalking"
                call sceneimg
                Margo "I see. While our cuisine is undoubtedly important, the overall dining experience, including service, plays a crucial role in keeping our patrons coming back. It's the synergy of both that makes us exceptional."
                $ position = "margormlistening"
                call sceneimg 
                player "I understand, Margo, but I was hoping to primarily focus on honing my skills in the kitchen."
                $ position = "margormtalking"
                call sceneimg
                Margo "I respect your dedication to your craft. However, as a member of this team, it's essential to be well-rounded. We work closely together to create memorable experiences for our guests. Perhaps over time, you'll see the value in the balance we strike here."
                $ position = "margormlistening"
                call sceneimg 
                player "Alright, Margo, I'll do my best to adapt and contribute in every way I can."
                $ position = "margormgoodluck"
                call sceneimg
                Margo "That's the spirit. We have a fantastic team here, and I'm sure you'll fit right in. If you ever have questions or need guidance, feel free to reach out. We're here to support each other and provide exceptional service."
                $ position = "margormlistening"
                call sceneimg 
                player "Thank you, Margo. I'll give it my best shot."
                $ position = "margormtalking"
                call sceneimg
                Margo "Welcome to the team. I appreciate your willingness to try new things."
                $ position = "margormlistening"
                call sceneimg 
                player "Thank you, Margo. I hope I can meet your expectations."
                $ rmclients = 1


        
            "I appreciate that, Margo, but I've always believed that my primary role is in the kitchen, creating exceptional dishes. Service and customer interactions are best left to those who excel in that area.":
                $ position = "margormexplaining"
                call sceneimg
                Margo "I understand your perspective, but here, we expect all team members to contribute to the overall guest experience. We believe that both the culinary and service aspects are essential for our success."
                $ position = "margormlistening"
                call sceneimg 
                player "I'm sorry, Margo, but I won't be engaging with the customers directly. My focus will be on delivering the best dishes from the kitchen."
                $ position = "margormexplaining"
                call sceneimg
                Margo "I respect your dedication to your craft, but I must emphasize that working here means embracing our service-oriented approach. It's a fundamental part of our restaurant's philosophy."
                $ position = "margormlistening"
                call sceneimg 
                player "I understand, Margo, but I won't be deviating from my culinary role."
                $ position = "margormexplaining"
                call sceneimg
                Margo "I appreciate your honesty. We'll work around this for now. However, I hope you'll eventually see the value in providing a complete dining experience. If you ever change your mind or have any questions, don't hesitate to reach out."
                $ position = "margormlistening"
                call sceneimg 
                player "Thank you, Margo. I'll keep that in mind."
                $ position = "margormtalking"
                call sceneimg
                Margo "Welcome to the team. Let's hope for a successful collaboration."
                $ position = "margormlistening"
                call sceneimg 
                player "Thank you, Margo. I'll do my best in the kitchen."
                $ rmclients = 0



    if margofirsttime == 1 and rmclients == 1:
    
        if myrandom == 1:

            $ position = "margohismile"
            call sceneimg
            Margo "Ah, good to see you. How are you settling in so far?"
            $ position = "margormlistening"
            call sceneimg 
            player "I'm doing well, thank you, Margo. It's been quite the experience."
            $ position = "margormexplaining"
            call sceneimg
            Margo "I'm glad to hear that. Listen, I appreciate your willingness to give the customer interactions a shot. It really does make a difference. Remember, the patrons love to see the face behind the delicious dishes they enjoy."
            $ position = "margormlistening"
            call sceneimg 
            player "I've been trying to be more open to it, and you're right, it's not as bad as I thought."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "That's the spirit! You'll find that our customers can be quite delightful. They appreciate good food and good company."
            $ position = "margormlistening"
            call sceneimg 
            player "I've noticed that, too. It's rewarding to see them enjoy the meals."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "Excellent. Keep up the good work. Your culinary skills are a huge asset to us, and when combined with your newfound customer interaction skills, I have no doubt you'll become a true star in our restaurant."
            $ position = "margormlistening"
            call sceneimg 
            player "Thanks, Margo. I'll do my best to contribute to the team and make the customers' dining experience memorable."
            $ position = "margormexplaining"
            call sceneimg
            Margo "I have no doubt you will. Now, get ready for a busy shift. And remember, if you ever need assistance or have any questions, don't hesitate to ask."
            $ position = "margormlistening"
            call sceneimg 
            player "I will, Margo. Thanks for your support."
            $ position = "margohismile"
            call sceneimg
            Margo "Good luck out there. I'm looking forward to hearing more about your culinary adventures."
            
        if myrandom == 2:
            $ position = "margohismile"
            call sceneimg
            Margo " I'm glad to see you again. How are you feeling about working directly with our customers today?"
            $ position = "margormlistening"
            call sceneimg 
            player "I've had some time to think about it, Margo. I'm willing to give it a try and help out where I can."
            $ position = "margormgoodluck"
            call sceneimg
            Margo "That's the spirit. I think you'll find it to be a rewarding experience. Remember, our patrons appreciate a personal touch, and it can make their dining experience truly special."
            $ position = "margormlistening"
            call sceneimg 
            player "I'll do my best to provide that personal touch, Margo. I'm here to contribute to the team and make our guests happy."
            $ position = "margormexplaining"
            call sceneimg
            Margo "That's the attitude we love to see. If you have any questions or need guidance while interacting with customers, feel free to ask. We're here to support you."
            $ position = "margormlistening"
            call sceneimg 
            player "Thanks, Margo. I appreciate your support. Let's make it a great day for our customers."
            $ position = "margormexplaining"
            call sceneimg
            Margo "Absolutely. Let's go out there and show them what our restaurant is all about."

        


        if myrandom == 3:
            $ position = "margohismile"
            call sceneimg
            Margo "Hello. It's nice to see you back."
            $ position = "margormlistening"
            call sceneimg 
            player "Hello, Margo. I've decided to give this customer interaction thing a try, like you suggested."
            $ position = "margormtalking"
            call sceneimg
            Margo "That's great to hear. I'm confident you'll do well. Just remember, the key is to be attentive, friendly, and make our guests feel special. It's all about creating memorable experiences."
            $ position = "margormlistening"
            call sceneimg 
            player "I'll keep that in mind. Any specific tasks for me tonight?"
            $ position = "margormexplaining"
            call sceneimg
            Margo "Tonight, you'll be assisting the servers, delivering dishes to the tables, and checking in on our guests to ensure everything's to their satisfaction. It's a fantastic way to get to know our regulars and newcomers alike."
            $ position = "margormlistening"
            call sceneimg 
            player "Sounds good, Margo. I'm up for it."
            $ position = "margormtalking"
            call sceneimg
            Margo "I knew you would be. And remember, if you ever have questions or need assistance, our seasoned staff will be happy to help. Now, let's get to work and show our guests why this place is so special."
            $ position = "margormlistening"
            call sceneimg 
            player "Absolutely, Margo. Let's make it a great night."
            $ position = "margormtalking"
            call sceneimg
            Margo "That's the spirit. I have no doubt you'll make a positive impression on our guests tonight. Good luck!"
            $ position = "margormlistening"
            call sceneimg 
            player "Thank you, Margo. I'll do my best."

        # jump cook 


    # next day no communication
    if margofirsttime == 1 and rmclients == 0:
        if myrandom == 1:
            $ position = "margohismile"
            call sceneimg
            Margo "Good morning. I hope you're ready for your first day here at the restaurant. We have a wonderful team, and I think you'll enjoy working with us."
            $ position = "margormlistening"
            call sceneimg 
            player "Morning, Margo. I'm looking forward to the cooking part, but I won't be interacting with customers. I'm not comfortable with that."
            $ position = "margormexplaining"
            call sceneimg
            Margo "Oh, I see. Well, here at our restaurant, we believe in providing a complete dining experience, and that includes connecting with our customers. It's part of the job for all team members."
            $ position = "margormlistening"
            call sceneimg 
            player "I understand, but I won't be doing that. My expertise is in the kitchen, not at the front of the house."
            $ position = "margormexplaining"
            call sceneimg
            Margo "I appreciate your skills, but we all have to pitch in. How about we start with you taking a few orders and see how it goes? You might find it's not as bad as you think."
            $ position = "margormlistening"
            call sceneimg 
            player "Margo, I won't change my mind on this. Cooking is what I'm here for, not serving tables."
            $ position = "margormexplaining"
            call sceneimg
            Margo "Alright, if that's your stance, we'll find a way to work around it. But do remember, customer satisfaction is crucial for us."
            $ position = "margormlistening"
            call sceneimg 
            player "I won't forget, Margo. I'll focus on the kitchen, and you can handle the front."
            $ position = "margormtalking"
            call sceneimg
            Margo "Fair enough. Let's make sure we excel in our respective roles. Welcome to the team."


        if myrandom == 2:
            $ position = "margohismile"
            call sceneimg
            Margo "Good morning, welcome to our restaurant. I hope you're ready for your first day."
            $ position = "margormlistening"
            call sceneimg 
            player "Morning, Margo. I am, but I want to clarify something from our last conversation. I won't be comfortable communicating with customers."
            $ position = "margormexplaining"
            call sceneimg
            Margo "I see. Well, that's an essential part of our service here. We believe in a complete dining experience."
            $ position = "margormlistening"
            call sceneimg 
            player "I understand that, but my expertise is in cooking. I'll give my best in the kitchen, but I won't be mingling with customers."
            $ position = "margormexplaining"
            call sceneimg
            Margo "We value your cooking skills, but we also expect every team member to assist in customer service. Perhaps we can arrange some training to help you get comfortable?"
            $ position = "margormlistening"
            call sceneimg 
            player "I appreciate the offer, Margo, but it's not something I want to do. I'd rather focus on my role in the kitchen."
            $ position = "margormexplaining"
            call sceneimg
            Margo "I understand your position, but this is a part of our culture here. I hope you'll reconsider in the future."
            $ position = "margormlistening"
            call sceneimg 
            player "I won't, Margo. Cooking is my passion, and that's where I can contribute best."

            $ position = "margormexplaining"
            call sceneimg
            Margo "Very well. We'll work with your decision, but keep in mind that our goal is to provide the best dining experience for our customers."
            $ position = "margormlistening"
            call sceneimg 
            player "I appreciate your understanding, Margo. I'll give my all in the kitchen."
            $ position = "margormexplaining"
            call sceneimg
            Margo "Let's focus on that, then. Welcome to the team."

        if myrandom == 3:
            $ position = "margormtalking"
            call sceneimg
            Margo " I want to reiterate the importance of customer service in our restaurant. Our clients are our lifeblood, and we need everyone on the team to engage with them."
            $ position = "margormlistening"
            call sceneimg 
            player "Margo, I appreciate your perspective, but I'm a cook. My strength lies in the kitchen, not in chatting with customers."
            $ position = "margormexplaining"
            call sceneimg
            Margo "I get that, but we're a tight-knit team here. It's not just about your role; it's about the overall experience we provide. I need you to be flexible."
            $ position = "margormlistening"
            call sceneimg 
            player "I'm sorry, Margo, but I can't commit to that. I'll give my best in the kitchen, but I won't be mingling with customers."
            $ position = "margormexplaining"
            call sceneimg
            Margo "Well, I was hoping for more cooperation. Customer satisfaction is crucial to us, and your refusal to engage directly might affect our ratings."
            $ position = "margormlistening"
            call sceneimg 
            player "I understand the stakes, Margo, but I can't step out of my comfort zone like that. Cooking is what I do best."
            $ position = "margormtalking"
            call sceneimg
            Margo "I see we're at an impasse here. I'll have to consider how this impacts our team dynamics moving forward."
            $ position = "margormlistening"
            call sceneimg 
            player "I hope you understand my perspective, Margo. I'm here to cook, not to be a server."
            $ position = "margormexplaining"
            call sceneimg
            Margo "Let's focus on your kitchen duties, then. Just remember, we're a team, and teamwork is crucial to our success."
        
    if ava_attitude >= 50 and workreputation >= 50:
        call restaurantbeachdaytalk

    jump cook 

jump rm
    # worked a shift
    # + money
    # + time
    # + reputation
