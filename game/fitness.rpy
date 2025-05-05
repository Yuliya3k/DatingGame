label fitness:
    play music "audio/gym.mp3" 
    $ calendar.AddMinutes(20)
    call closescreens
    

    if linfirsttime == 0:
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            $ position = "linlistening"
            call sceneimg
            player "Hi, I'm new in town and thought I'd check out the fitness club. Is this where I sign up?"
            $ position = "linhi"
            call sceneimg
            Lin "Absolutely! Welcome to FitZone. I'm Lin, one of the trainers here. What's your name?"
            $ position = "linlistening"
            call sceneimg
            player "I'm [name]. Nice to meet you, Lin. What kind of training programs do you offer here?"

            Lin "Nice to meet you too, [name]. We have a range of programs, from cardio and strength training to group classes like yoga and spin. It depends on your goals. What are you looking to achieve?"
            $ calendar.AddMinutes(5)
            $ linfirsttime = 1
        
        if myrandom == 2:
            $ position = "linlistening"
            call sceneimg
            player "Hey, I heard good things about this place. I'm thinking about joining. What can you tell me about it?"
            $ position = "linhi"
            call sceneimg
            Lin "Well, you're in luck! I'm Lin, one of the trainers here. FitZone offers a variety of programs to help you achieve your fitness goals. What's your name?"
            $ position = "linlistening"
            call sceneimg
            player "I'm [name]. Nice to meet you, Lin. Do you offer personal training sessions here?"

            Lin "Nice to meet you too, [name]. Yes, we do have personal training if myrandom ==s. We can tailor a program to your specific needs and goals."
            $ calendar.AddMinutes(5)
            $ linfirsttime = 1

        if myrandom == 3:
            $ position = "linlistening"
            call sceneimg
            player "I've been looking for a gym in the area. What's your fitness club all about?"
            $ position = "linhi"
            call sceneimg
            Lin "Great to have you interested! I'm Lin, a trainer here at FitZone. We focus on providing a welcoming and supportive environment for all fitness levels. What's your name?"
            $ position = "linlistening"
            call sceneimg
            player "I'm [name]. It's good to meet you, Lin. Are there any group classes or special events coming up?"

            Lin "Likewise, [name]. Yes, we have a schedule of group classes, and we often organize fitness challenges and events. I can give you a rundown if you'd like."
            $ calendar.AddMinutes(5)
            $ linfirsttime = 1        
        
        $ myrandom = renpy.random.randint(1,3)
        $ position = "linhmm"
        call sceneimg
        menu:
            "I'm excited to get started. What program would you recommend for someone looking to build strength?" if myrandom == 1:
                Lin "For building strength, I'd recommend our Strength & Conditioning program. It focuses on weightlifting and resistance training. We'll help you set specific goals and track your progress."
                $ training = 1
                jump trainingbye
            "I'm interested in improving my flexibility and reducing stress. What program would you suggest for that?" if myrandom == 2: 
                $ position = "linletsdoit"
                call sceneimg
                Lin "If flexibility and stress reduction are your goals, our Yoga & Mindfulness program would be perfect for you. It combines yoga sessions with relaxation techniques to help you find balance."
                $ training = 1
                jump trainingbye
            "I want to improve my overall fitness and endurance. What program should I sign up for?" if myrandom == 3:
                $ position = "linletsdoit"
                call sceneimg
                Lin "For overall fitness and endurance, I'd recommend our Total Body Fitness program. It offers a mix of cardio workouts, strength training, and core exercises to boost your stamina and tone your body."
                $ position = "linlistening"
                call sceneimg
                player "Great, the Total Body Fitness program sounds like what I need. When can I start?"
                $ position = "linexplaining"
                call sceneimg
                Lin "Fantastic choice! We have sessions starting next week. I'll get you signed up for the program, and we can schedule your first session. Welcome to FitZone, [name]!"
                $ position = "linlistening"
                call sceneimg
                player "Thank you, Lin. I'm looking forward to it!"  
                $ training = 1
                jump trainingthanks
            "I appreciate your offer, Lin, but I'm not really into fitness training right now." if myrandom == 1:
                $ position = "linexplaining"
                call sceneimg
                Lin "No problem at all, [name]. If you ever change your mind or want some advice, just let me know. I'm here to help."
                $ training = 0
                jump trainingbye
            "I've had a bad experience with fitness training before, Lin, and I'm not ready to give it another shot." if myrandom == 2:
                $ position = "linexplaining"
                call sceneimg
                Lin "I completely understand. Sometimes it's important to take things at your own pace. If you ever reconsider, we'll be here."
                $ training = 0
                jump trainingbye
            "Thanks for the offer, Lin, but I have a pretty busy schedule right now, and I don't think I can commit to training." if myrandom == 3:
                $ position = "linexplaining"
                call sceneimg
                Lin "I get it, [name]. Life can get hectic. If things change or you find some free time, feel free to drop by. We'll be here to help you meet your fitness goals."
                $ training = 0
                jump trainingbye

    if linfirsttime == 1 and training == 1:
        $ myrandom = renpy.random.randint(1,3)

        if myrandom == 1:
            $ position = "linexplaining"
            call sceneimg
            Lin "Hey [name], ready for another training session today?"
            $ position = "linlistening"
            call sceneimg
            player "Absolutely, Lin. Let's get to work!"
            $ position = "linletsdoit"
            call sceneimg
            Lin "That's the spirit! Remember, every drop of sweat you shed here takes you closer to your fitness goals. We'll start with some warm-up stretches to get those muscles ready. Then, we'll dive into a high-intensity circuit that'll leave you feeling stronger and more energetic. And always keep in mind, consistency is the key to success. You've been doing great!"
            jump trainingthanks

        if myrandom == 2:
            $ position = "linhi"
            call sceneimg
            Lin "Good to see you, [name]. How are you feeling today? Ready to train?"
            $ position = "linlistening"
            call sceneimg
            player "Feeling great, Lin. Let's push it to the limit!"
            $ position = "linletsdoit"
            call sceneimg
            Lin "Fantastic! You know, every day you show up here, you're investing in your health and well-being. That's something to be proud of. Today, we'll focus on your core strength and endurance. I've designed a challenging routine that'll help you achieve your fitness milestones. Remember, it's not just about the workout; it's about the journey and the progress you make along the way."
            jump trainingthanks
        if myrandom == 3:
            $ position = "linhi"
            call sceneimg
            Lin "Hey there, [name]. Training day is here again. Ready to hit those goals?"
            $ position = "linlistening"
            call sceneimg
            player "You bet, Lin. I'm all in for this."
            $ position = "linletsdoit"
            call sceneimg
            Lin "Great to hear your determination! Keep in mind that progress might not always be linear, but as long as you're putting in the effort, you're moving forward. Today, we're concentrating on your flexibility and balance. We'll work on exercises that not only challenge your body but also your mind. And always remember, setbacks are just setups for comebacks. Let's do this!"
            jump trainingthanks

    if linfirsttime == 1 and training == 0:   
        $ myrandom = renpy.random.randint(1,3)
        $ position = "linhmm"
        call sceneimg
        if myrandom == 1:
            $ position = "linhi"
            call sceneimg
            Lin "Hey [name], I didn't expect to see you back here today. What brings you back to the gym?"
            menu:
                "Well, Lin, I've been thinking, and maybe you were right. I want to give training another shot and see where it takes me.":
                    $ position = "linletsdoit"
                    call sceneimg
                    Lin "That's the spirit! It's never too late to start, and I'm here to support you all the way. Let's work together to achieve your fitness goals."
                    $ training = 1
                    jump trainingbye
                "Honestly, Lin, I can't explain it. I guess I just felt like I needed to be here, even though I'm not sure I'm ready to start training yet.":
                    $ position = "linexplaining"
                    call sceneimg
                    Lin "That's okay. Sometimes, you might not know exactly what you need until you're here. If you ever change your mind, I'll be here to help you get started."
                    jump trainingbye

        if myrandom == 2:
            $ position = "linhi"
            call sceneimg
            Lin "Hello again, [name]. You're back! What made you change your mind about training?"
            menu:

                "I realized that I can't ignore the importance of fitness anymore. I want to improve myself, and I think your guidance will be valuable.":
                    $ position = "linletsdoit"
                    call sceneimg
                    Lin "I appreciate your honesty, and I'm here to help you reach your potential. Remember, it's not about where you start; it's about the journey and the progress you make."
                    $ training = 1
                    jump trainingbye
                "I wish I could give you a clear answer, Lin, but I'm not sure why. I guess I just wanted to be in this environment and see where it leads.":
                    $ position = "linexplaining"
                    call sceneimg
                    Lin "Well, that's a start. No pressure, [name]. If and when you're ready, we can discuss a training plan. Until then, feel free to hang around."
                    jump trainingbye
            

        if myrandom == 3:
            $ position = "linhi"
            call sceneimg
            Lin "Oh, look who's back! [name], what made you decide to return to the gym?"
            menu:
                "Well, Lin, I've been feeling a bit sluggish lately, and I figured it's time for a change. Your encouragement stayed with me, and I want to give training a shot.":
                    $ position = "linletsdoit"
                    call sceneimg
                    Lin "I'm glad to hear that. It takes courage to make a choice like this. We'll start slow and work our way up, one step at a time. You've got this!"
                    $ training = 1
                    jump trainingbye
                "Honestly, Lin, I'm not sure why I'm here. It's a bit confusing even for me. I can't seem to find the motivation to start training.":
                    $ position = "linexplaining"
                    call sceneimg
                    Lin "I appreciate your honesty. Sometimes, these things take time. If you ever want to talk or need guidance, just let me know. I'm here to support you whenever you're ready."
                    jump trainingbye


"something went wrong"
jump culinarychoices