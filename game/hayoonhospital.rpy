label hayoonhospital:



    if hospitalhi == 0:
        $ myrandom = renpy.random.randint(1,3)
        if myrandom > 1:
            $ myrandom = renpy.random.randint(1,2)
            if myrandom == 1:
                $ position = "hayoonhospitalleaning1"
                call sceneimg
                "You see Ha-Yoon is waiting for a patient, it may be a good opportunity to talk"
                menu:
                    "Talk to Ha-Yoon":
                        pass
                    "Do not talk, go home":
                        jump culinarychoices
            if myrandom == 2: 
                $ position = "hayoonhospitalleaning2"
                call sceneimg
                "You see Ha-Yoon is waiting for a patient, it may be a good opportunity to talk"
        else:
            $ position = "hospitalempty"
            call sceneimg
            "There is nobody here"
            jump culinarychoices
            
    else:
        $ myrandom = renpy.random.randint(1,2)
        if myrandom == 1:
            $ position = "hayoonhospitalleaning1"
            call sceneimg
            
        if myrandom == 2: 
            $ position = "hayoonhospitalleaning2"
            call sceneimg
                

    menu:
        "Say hi" if hospitalhi == 0:
            $ hayoonmettoday = True
            $ hospitalhi = 1    
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                $ position = "hayoonhospitaltalkhello"
                call sceneimg
                player "Hey, Ha-Yoon! It's good to see you here. How's your day been at the hospital?"
                $ position = "hayoonhospitaltalktalk"
                call sceneimg
                HaYoon "Hello! It's been quite a day – started off with some challenging cases, but we managed well. The hospital environment is always unpredictable. I had a patient with a rare condition, and coordinating with specialists kept me on my toes. It's fulfilling, though, seeing patients respond positively to treatments."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg
                player "That sounds intense but rewarding. It must take a lot of resilience and skill to handle such situations."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Definitely. Each day is a new learning experience. Sometimes it's about medical knowledge, other times it's about understanding patient psychology. For instance, today I spent a good amount of time just talking to a patient, easing their concerns. It's not just about the physical treatment, but also offering emotional support."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "That's a very holistic approach. I admire how you balance the technical and human aspects of your job."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Thank you. It's not always easy, but it's worth it. Seeing a patient smile and knowing I contributed to their healing is the best part of my job."

            if myrandom == 2:
                $ position = "hayoonhospitaltalkhello"
                call sceneimg

                player "Hi, Ha-Yoon! How's everything at the hospital today? Anything interesting?"
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Hey there! It's been a mixed bag, really. We had a couple of emergency cases in the morning which were quite demanding. But the team's coordination was exceptional, and we managed to stabilize the patients effectively."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "That's intense. It must be quite a rush to work in such high-pressure situations."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "It is. There's this adrenaline rush, but it's also balanced with a sense of responsibility. Like today, I had to perform a minor procedure under unexpected circumstances. It was challenging, but thankfully, it went well."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "Sounds like you really have to be prepared for anything. It's impressive how you handle it all."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "It's part of the job. I always say being a doctor is about lifelong learning – not just in medicine but in adapting and problem-solving. Every day brings its own set of challenges and triumphs."

            if myrandom == 3:
                $ position = "hayoonhospitaltalkhello"
                call sceneimg

                player "Hello, Ha-Yoon! Busy day at the hospital?"
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Hi! Yes, it's been quite eventful. We had a series of consultations and surgeries lined up. I was involved in a particularly complicated surgery this morning, which required a lot of precision and focus."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "That sounds incredibly demanding. How do you manage such stress?"
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Well, it's about staying calm and collected. Having a great team helps a lot. Post-surgery, I had consultations. I enjoy this part because it allows me to connect with patients on a personal level, understand their concerns, and offer guidance."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "Your job really encompasses a wide range of skills. It's not just medical expertise but also empathy and communication."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Absolutely. Being a doctor isn't just about diagnosing and treating; it's about caring for the person as a whole. Balancing the technical and emotional aspects is key to providing effective healthcare."

        "I want to ask you a question, but I'm unsure":
            

            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1: 
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "Actually, Ha-Yoon, there's something I've been wanting to ask you, but I'm not sure how you'll take it."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Oh? Don't hesitate. Just go ahead and ask. I believe in open communication, and I'm here to help in any way I can."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "Well, it's a bit out of the blue. I've been reading up on some health topics, and I came across this particular condition. It's not something I've heard much about before, and it got me thinking. I know you're a doctor, and I value your opinion, but I wasn't sure if it was appropriate to bring it up out of a professional setting."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "I understand your concern, but please feel free to ask. It's always good to seek information, especially about health. I'll try my best to provide a helpful response, or at least guide you to the right resources."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "Thanks, Ha-Yoon. That's really reassuring to hear. I guess what I'm trying to say is that I appreciate your openness and willingness to assist, even outside of your professional responsibilities. It's not just about the question itself but also about understanding and navigating these health-related topics."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Absolutely, and I'm glad you feel comfortable reaching out. Health is a broad and sometimes complex subject, and it's normal to have questions or concerns. Whether it's clarifying a medical condition, discussing wellness strategies, or simply satisfying curiosity, I'm here to support and guide."

            if myrandom == 2: 
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "Ha-Yoon, there's something I've been meaning to ask you. It's a bit personal, and I'm not sure if it's something I should be discussing with you. I hope it's okay."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Please, don't worry about it. It's okay to ask questions, even personal ones. I'm here to listen and help if I can. What's on your mind?"
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "It's about a health issue that I came across recently. I've been doing some research, but there's a lot of conflicting information out there. I thought of asking you, given your expertise, but I wasn't sure if it was crossing a line. I don't want to impose on your time or make you feel uncomfortable."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "I appreciate your consideration, but as a doctor, I'm more than happy to discuss health issues. It's important to have accurate information, and I'm glad you thought of me. Feel free to ask your question, and I'll do my best to provide a clear and accurate answer."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "Thank you, Ha-Yoon. That means a lot. I've always respected your knowledge and judgment, and having this conversation is really helpful. It's not just about getting an answer but also about understanding the broader context of health and wellness."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Of course, and you're right. Understanding the bigger picture of health is crucial. I'm here to help clarify any doubts and guide you towards better health choices. Always feel free to reach out with any questions."

            if myrandom == 3:

                $ position = "hayoonhospitaltalklisten"
                call sceneimg
                player "Ha-Yoon, there's been a question on my mind for a while, but I've been hesitant to ask. It's a bit personal, and I'm not sure how to approach it with you."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "I'm here to help, so please don't hesitate to ask. I understand that health-related questions can be personal, but it's important to seek answers. What's your question?"
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "It's about a specific health concern that I've been curious about. I've looked into it a bit, but the information I found was overwhelming and sometimes contradictory. I know you're a doctor, and I respect your expertise, but I didn't want to overstep by asking something outside of a professional consultation."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "You're not overstepping at all. It's great that you're taking an interest in your health, and I'm more than willing to offer my perspective. It's better to have a conversation and get reliable information than to be left wondering or misled by unreliable sources."
                $ position = "hayoonhospitaltalklisten"
                call sceneimg

                player "That's very kind of you, Ha-Yoon. Your willingness to engage in this conversation and offer your insights is truly valuable. It's not just about finding an answer but also about learning to navigate the complex world of health information."
                $ position = "hayoonhospitaltalktalk"
                call sceneimg

                HaYoon "Exactly, and I'm happy to assist. Understanding health issues can be challenging, and I'm here to make it more accessible and understandable. Feel free to ask me anything, anytime."

            menu:
                "Tell her about your belly fetish":
                    
                    $ myrandom = renpy.random.randint(1,3)
                    if myrandom == 1: 
                        $ position = "hayoonhospitaltalktalk"
                        call sceneimg

                        HaYoon "I see. Thank you for sharing that with me. As a doctor, I've learned that human sexuality and preferences are diverse and complex. It's important to recognize and understand our own desires, as long as they are expressed in a healthy, consensual, and respectful manner. Fetishes and preferences like yours, focused on a specific body part or attribute, are more common than you might think. It's a part of human diversity in sexual expression. If this aspect of your sexuality causes you any distress or if you have concerns about how it impacts your relationships, it might be helpful to speak with a therapist who specializes in sexual health. They can provide more personalized guidance and support."
                        $ position = "hayoonhospitaltalklisten"
                        call sceneimg

                        player "Thank you, Ha-Yoon. I appreciate your understanding and professional advice. It's a relief to talk about this openly."
                        $ position = "hayoonhospitaltalktalk"
                        call sceneimg

                        HaYoon "Of course. It's important to have a safe space to discuss these things. Remember, sexual preferences are a part of who you are, and seeking understanding and support is a positive step."

                    if myrandom == 2:
                        $ position = "hayoonhospitaltalktalk"
                        call sceneimg

                        HaYoon "Thank you for trusting me with this information. In the field of medicine, we acknowledge that individuals have varied sexual preferences and fetishes. What you've described is a type of fetish, and it's essential to approach it with self-awareness and mutual respect in any relationship. As long as your preferences are expressed in a healthy way that respects both your own and your partner's boundaries and consent, there's a space for open and honest communication. If you ever find that this aspect of your sexuality is causing you confusion or concern, consulting a mental health professional who understands sexual health could be beneficial. They can help you navigate any complexities or questions you might have."
                        $ position = "hayoonhospitaltalklisten"
                        call sceneimg

                        player "I appreciate your open-mindedness and advice, Ha-Yoon. It's been something I've been unsure about discussing."
                        $ position = "hayoonhospitaltalktalk"
                        call sceneimg

                        HaYoon "I'm glad you felt you could talk to me. Understanding and accepting your sexual preferences is an important part of your overall well-being."

                    if myrandom == 3: 
                        $ position = "hayoonhospitaltalktalk"
                        call sceneimg

                        HaYoon "Firstly, I want to thank you for feeling comfortable enough to share that with me. As a doctor, my role is to provide nonjudgmental support and advice. Sexual preferences, including fetishes, are a natural part of human sexuality for many people. What's important is how these preferences are integrated into your life – ensuring that they contribute to healthy, consensual, and respectful relationships. If your preference for a specific physical attribute like a belly brings you any feelings of distress or if you're seeking ways to understand it better within the context of your relationships, it might be helpful to speak with a therapist who can offer more personalized insight and guidance in the realm of sexual health."
                        $ position = "hayoonhospitaltalklisten"
                        call sceneimg

                        player "Thanks, Ha-Yoon, for your understanding and guidance. It's something I've been hesitant to talk about."
                        $ position = "hayoonhospitaltalktalk"
                        call sceneimg

                        HaYoon "You're welcome. Remember, seeking to understand and accept your preferences is a healthy approach, and professional guidance can be very helpful in this journey."
                    menu:
                        "Do you want to know why I asked you?":
                            $ myrandom = renpy.random.randint(1,3)
                            if myrandom == 1: 
                                $ position = "hayoonhospitaltalktalk"
                                call sceneimg

                                HaYoon "Yes, I'm actually quite interested to know why you brought this up. It's not often that someone shares such personal aspects of their sexuality with me outside a clinical setting. Understanding your reasoning could provide me with more context, and as a medical professional, I value understanding the whole picture when it comes to matters of health and well-being. So, please feel free to share your thoughts and reasons."
                                $ position = "hayoonhospitaltalklisten"
                                call sceneimg

                                player "I appreciate your willingness to listen. I guess I've been looking for a perspective from someone in the medical field, someone who could offer an objective viewpoint without judgment."
                                $ position = "hayoonhospitaltalktalk"
                                call sceneimg

                                HaYoon "That makes sense. I'm here to offer any insights I can, within my professional capacity. Your trust in sharing this with me is something I take seriously."

                            if myrandom == 2: 
                                $ position = "hayoonhospitaltalktalk"
                                call sceneimg

                                HaYoon "Certainly, I would like to know why you decided to ask me about this. It's important for me as a doctor to understand the context behind such discussions. Your openness is commendable, and if there's more you wish to share or explore about this topic, I'm here to listen and provide any professional guidance that might help you."
                                $ position = "hayoonhospitaltalklisten"
                                call sceneimg

                                player "Thank you for being so open and nonjudgmental. I've been contemplating this aspect of myself and thought a medical perspective might help me make sense of it."
                                $ position = "hayoonhospitaltalktalk"
                                call sceneimg

                                HaYoon "I'm glad you chose to discuss it with me. Understanding oneself is a key part of personal health, and I'm here to support that journey in any way I can."

                            if myrandom == 3:
                                $ position = "hayoonhospitaltalktalk"
                                call sceneimg

                                HaYoon "Yes, I'm definitely interested in understanding why you chose to share this with me. It's not every day that I have conversations like this, especially in a non-clinical context. But as a healthcare professional, I believe in providing a safe space for all kinds of health-related discussions, including those pertaining to sexual health and preferences. So please, feel free to explain your reasons."
                                $ position = "hayoonhospitaltalklisten"
                                call sceneimg

                                player "I value your opinion highly, Ha-Yoon, not just as a doctor but as someone I trust. I was hoping for some insight from someone knowledgeable and approachable."
                                $ position = "hayoonhospitaltalktalk"
                                call sceneimg

                                HaYoon "I'm honored that you trust me with this. It's important to have open channels of communication about these topics, and I'm here to offer any assistance or advice you might need."
                            menu:
                                "Explain that you asked because she is a doctor":
                                    $ myrandom = renpy.random.randint(1,3)
                                    if myrandom == 1: 
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "The reason I brought this up with you, Ha-Yoon, is precisely because of your professional background. I've been grappling with understanding this part of myself, and I knew you, as a medical professional, would offer an objective and informed opinion. It's not easy to discuss such matters, and I needed someone who could approach it with a clinical perspective, free from personal biases."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "I appreciate your trust in my professionalism. Discussing sexual preferences and fetishes can indeed be sensitive, and it's important to approach them with an open mind and a medical understanding. I'm glad you felt comfortable coming to me, and I hope my response has been helpful. If there are more aspects you wish to explore or questions you have, remember, my door is always open."
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "Thank you, Ha-Yoon. It means a lot to have someone with your expertise to talk to about this."

                                    if myrandom == 2: 
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "I asked you, Ha-Yoon, because I value the professional insight you bring as a doctor. I've been trying to make sense of my preferences, and I thought who better to discuss this with than someone who understands the complexities of human behavior and health. Your medical perspective provides a clarity that I can't get from just talking to friends or searching online."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "It's good to hear that you consider my professional opinion valuable in understanding yourself better. Sexual health and preferences are an integral part of overall well-being, and it's important to have open and honest conversations about them. If my insights can provide you with a clearer understanding or guide you to further resources, then I'm more than happy to assist."

                                        player "That's exactly what I was looking for. Thanks for being so approachable and understanding about this."

                                    if myrandom == 3:
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "I chose to ask you, Ha-Yoon, because I respect your expertise as a doctor. When it comes to something as personal as sexual preferences, I wanted a perspective grounded in medical knowledge. You have a way of explaining things that demystifies and normalizes these topics, and that is what I was looking for – a professional viewpoint to help me navigate my thoughts and feelings."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "I am honored that you consider my professional viewpoint valuable. Understanding and accepting one's sexual preferences are crucial for mental and emotional health. As a doctor, it's my role to provide guidance and support in all aspects of health, including sexual health. If there's anything more you need clarity on or if you're looking for further discussions, I'm here to help."
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "Thanks, Ha-Yoon. Your understanding and professional guidance have been incredibly reassuring."
                                    jump hayoonghospitalgoodbye
                                "Explain her that you asked because you've seen her belly bloated":
                                    $ myrandom = renpy.random.randint(1,3)
                                    if myrandom == 1:
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg 

                                        player "Actually, Ha-Yoon, part of the reason I asked is because I've noticed a few times that your belly appeared quite bloated, almost like you were pregnant. I thought maybe you shared the same interest or had a similar fetish."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "Oh, I see where you're coming from. In reality, that bloating is simply a result of my eating habits. As a doctor, especially in a hospital setting, we often don't get much time for proper meals. So, I tend to eat quickly and sometimes in larger quantities than usual, which can lead to bloating. It's not something I've ever sexualized or considered in that light. It's just a practical aspect of my busy schedule and the demands of my job."
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "I understand now. I hope I didn't offend you by bringing it up."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "Not at all. It's a valid observation, but in my case, it's purely circumstantial and not related to any particular fetish or sexual preference."

                                    if myrandom == 2: 
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "I was curious, Ha-Yoon, and I hope this doesn't come across wrong, but I've seen you sometimes with what looked like a very full belly. It made me wonder if you might share my interest in that kind of physical appearance."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "I appreciate your honesty, but what you observed is just a result of my eating patterns. As doctors, especially in a hectic environment like a hospital, we often have to eat quickly between rounds or procedures. This can lead to me eating more rapidly than I should, which causes bloating. It's not something I associate with any sexual context—it's purely a functional aspect of my lifestyle in a demanding profession."
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "Thanks for clarifying that, Ha-Yoon. I hope I haven't made you uncomfortable."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "No, you haven't. It's good to have open discussions, and I understand why you might have thought that. But in my case, it's completely unrelated to any fetish."

                                    if myrandom == 3: 
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "Ha-Yoon, I was wondering, and please tell me if this is too forward, but I've noticed sometimes your belly looks quite full, almost pregnant. I thought maybe you had a similar interest in belly expansion."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "Oh, that's an interesting observation. To be honest, what you've noticed is a consequence of how I often eat. In the medical field, especially in a busy hospital environment, meal times can be irregular and rushed. I tend to eat quickly, which can lead to noticeable bloating. However, this isn't something of a sexual nature for me. It's simply a practical aspect of my day-to-day life as a doctor, where time for meals is often scarce."
                                        $ position = "hayoonhospitaltalklisten"
                                        call sceneimg

                                        player "I see. I'm sorry if my question was out of line."
                                        $ position = "hayoonhospitaltalktalk"
                                        call sceneimg

                                        HaYoon "It's okay. I understand the curiosity, but in my situation, it's purely a matter of practicality and the nature of my work."
                                    menu:
                                        "Is it ok to eat like you?":
                                            $ myrandom = renpy.random.randint(1,3)
                                            if myrandom == 1: 
                                                $ position = "hayoonhospitaltalklisten"
                                                call sceneimg

                                                player "Ha-Yoon, I've had this question for a long time. Is it actually safe or healthy to eat to the point where you feel like you're ready to explode?"
                                                $ position = "hayoonhospitaltalktalk"
                                                call sceneimg

                                                HaYoon "That's an important question. Eating to such an extent can be harmful in several ways. Firstly, overeating, especially regularly, can lead to weight gain and associated health issues like obesity, heart disease, and diabetes. It puts excessive strain on your digestive system, leading to discomfort, bloating, and potentially more serious conditions like gastric rupture in extreme cases. Secondly, it can affect your metabolism and even lead to nutritional imbalances. Eating large amounts in a short period can also impact mental well-being, as it's often linked with feelings of guilt or shame. Moderation is key in eating habits, and it's crucial to listen to your body's signals of hunger and fullness."
                                                $ position = "hayoonhospitaltalklisten"
                                                call sceneimg

                                                player "That's quite insightful. I didn't realize the extent of the potential issues."
                                                $ position = "hayoonhospitaltalktalk"
                                                call sceneimg

                                                HaYoon "Yes, it's important to be mindful of our eating habits for our overall health. It's always better to eat in moderation and focus on a balanced diet."

                                            if myrandom == 2:
                                                $ position = "hayoonhospitaltalklisten"
                                                call sceneimg

                                                player "I've been wondering, Ha-Yoon, from a medical standpoint, is it safe or healthy to eat so much that you feel extremely full?"
                                                $ position = "hayoonhospitaltalktalk"
                                                call sceneimg

                                                HaYoon "From a medical perspective, consistently eating to that extent isn't advisable. Overeating can lead to various health issues. It can cause immediate discomfort like indigestion, acid reflux, and bloating. Long-term, it can lead to more serious health concerns such as gastrointestinal disorders, increased risk of cardiovascular diseases, and metabolic syndrome. It's also important to consider the psychological aspects. Compulsive overeating or eating in response to emotional cues rather than hunger can lead to an unhealthy relationship with food. A balanced diet and understanding your body's needs are crucial for maintaining good health."
                                                $ position = "hayoonhospitaltalklisten"
                                                call sceneimg

                                                player "I see. It sounds like it's about balance and understanding your body."
                                                $ position = "hayoonhospitaltalktalk"
                                                call sceneimg

                                                HaYoon "Exactly. It's important to nurture a healthy relationship with food, which includes understanding portion sizes and your body's cues."

                                            if myrandom == 3:
                                                $ position = "hayoonhospitaltalklisten"
                                                call sceneimg

                                                player "Ha-Yoon, I've always been curious. Is it really safe or healthy to eat until you're excessively full?"
                                                $ position = "hayoonhospitaltalktalk"
                                                call sceneimg

                                                HaYoon "Eating until you're excessively full, especially on a regular basis, can be detrimental to your health. It puts unnecessary stress on your digestive system, leading to discomfort and potential long-term issues like gastritis or GERD (Gastroesophageal Reflux Disease). Overeating can also contribute to weight-related problems and imbalances in blood sugar levels, which can be particularly risky for people with or prone to diabetes. Additionally, it's not just about physical health. Overeating can be linked to psychological factors such as stress or emotional eating, which can be addressed more effectively through understanding and managing the underlying emotional triggers."
                                                $ position = "hayoonhospitaltalklisten"
                                                call sceneimg

                                                player "Thanks for explaining that. It sounds like moderation is essential."
                                                $ position = "hayoonhospitaltalktalk"
                                                call sceneimg

                                                HaYoon "Absolutely. A balanced approach to eating, attentive to both physical and emotional signals, is key to maintaining good health." 
                                          
                                            menu:

                                                "Why do you do this?":
                                                    $ hayoonfasteater = 1
                                                    $ myrandom = renpy.random.randint(1,3)
                                                    if myrandom == 1: 
                                                        $ position = "hayoonhospitaltalklisten"
                                                        call sceneimg

                                                        player "If eating like that can be harmful, why do you choose to eat this way? I'm just curious about your perspective."
                                                        $ position = "hayoonhospitaltalktalk"
                                                        call sceneimg

                                                        HaYoon "That's a fair question. As a doctor, I'm certainly aware of the potential consequences of such eating habits. However, we doctors are also human and have our own personal preferences and coping mechanisms. My eating pattern, especially in the demanding hospital environment, is a personal decision. It's a way of managing the limited time I have, and admittedly, it's not always ideal. I'm fully informed about the possible health implications, and I do take steps to mitigate the risks as much as possible, such as being mindful of my diet outside of work and maintaining a regular exercise routine. It's about balancing my professional responsibilities with my personal choices, while being aware of the health risks involved."
                                                        $ position = "hayoonhospitaltalklisten"
                                                        call sceneimg

                                                        player "That makes sense. It's about finding a balance that works for you, even in a challenging environment."
                                                        $ position = "hayoonhospitaltalktalk"
                                                        call sceneimg

                                                        HaYoon "Exactly. It's important to be aware and make informed choices, even if they're not perfect."

                                                    if myrandom == 2:
                                                        $ position = "hayoonhospitaltalklisten"
                                                        call sceneimg

                                                        player "Considering the risks associated with overeating, why do you still choose to eat in such a way?"
                                                        $ position = "hayoonhospitaltalktalk"
                                                        call sceneimg

                                                        HaYoon "It's a valid question, and I understand where you're coming from. In the medical profession, particularly in a hospital setting, the nature of our work often dictates our lifestyle choices, including eating habits. My choice to eat quickly and in larger quantities at times is more a reflection of the constraints of my job rather than a disregard for the health implications. I'm fully aware of the consequences, and I ensure to counterbalance this with other healthy habits and regular health check-ups. It's a compromise I make given the nature of my work, but it's an informed decision."
                                                        $ position = "hayoonhospitaltalklisten"
                                                        call sceneimg

                                                        player "I can see how the demanding nature of your job impacts your eating habits."
                                                        $ position = "hayoonhospitaltalktalk"
                                                        call sceneimg

                                                        HaYoon "Yes, it's one of the challenges we face in this profession. But being aware and proactive about our health is key."

                                                    if myrandom == 3:
                                                        $ position = "hayoonhospitaltalklisten"
                                                        call sceneimg

                                                        player "I'm curious, knowing the potential harm, why do you still eat in such a way that can cause bloating?"
                                                        $ position = "hayoonhospitaltalktalk"
                                                        call sceneimg

                                                        HaYoon "That's an insightful question. As a medical professional, I'm fully aware of the health risks associated with such eating habits. However, the reality of working in a hospital often involves irregular and rushed meal times. My way of eating is a pragmatic decision in response to the time constraints I face daily. It's not ideal, and I'm fully cognizant of that. I make this choice with a full understanding of its implications and try to maintain a balanced approach to my overall health to mitigate any adverse effects. It's about making informed choices within the constraints of my professional life."
                                                        $ position = "hayoonhospitaltalklisten"
                                                        call sceneimg

                                                        player "It sounds like a challenging but necessary adjustment to your work life."
                                                        $ position = "hayoonhospitaltalktalk"
                                                        call sceneimg

                                                        HaYoon "It is. It's about adapting to the circumstances while staying informed about our health choices."
                                                    menu:
                                                        "Do you want to go to lunch with me from time to time? The food is on me!":
                                                            $ myrandom = renpy.random.randint(1,3)
                                                            if myrandom == 1: 
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "Knowing all this, and considering my personal interests, would you mind if I asked you out for lunch? I’d be happy to treat you."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "I appreciate your offer, and I'm flattered. However, I think it's important to maintain a professional boundary in this context. While I'm open to discussing health-related topics and providing guidance, I feel it would be more appropriate to keep our interactions within the realm of professional advice and support. I value our conversations and the trust you've placed in me by sharing your personal interests, but I believe it's crucial to keep those aspects of our relationship separate from social engagements."
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "I understand and respect your perspective. Thanks for being honest about it."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "Thank you for understanding. I'm always here if you need medical advice or support."

                                                            if myrandom == 2: 
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "Given what I've shared with you about my interests, would it be okay if I asked you out for lunch? My treat."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "Thank you for the invitation, and for being upfront about your interests. However, considering the professional nature of our relationship and the information you've shared, I think it would be best to maintain a clear distinction between our professional interactions and personal life. It's important for me, as a doctor, to ensure that boundaries are respected for the comfort and well-being of both parties. I hope you understand that this decision is made with mutual respect in mind."
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "Absolutely, I respect your decision and appreciate your clarity."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "Thank you for your understanding. If you have any health-related questions in the future, feel free to reach out."

                                                            if myrandom == 3: 
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "Considering what I've told you about my fetish, would you still be open to going out for lunch with me? I’d like to invite you."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "I'm glad you felt comfortable enough to share that with me, and I'm grateful for your offer. However, I think it’s important for me to maintain a certain level of professionalism in our interactions. Given the personal nature of what you've shared, it might be better to keep our relationship focused on professional advice and health-related discussions. I hope this doesn't cause any discomfort, and please know that my decision is based on maintaining professional integrity and respect."
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "I understand where you're coming from, Ha-Yoon. Thanks for your honesty."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "Thank you for being understanding. And remember, my door is always open for any health advice or concerns you may have."
                                                                jump hayoonghospitalgoodbye
                                                        "You can come to my restaurant to have lunch any time as a gift":
                                                            $ myrandom = renpy.random.randint(1,3)
                                                            if myrandom == 1:
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "How about this - would you consider coming to my restaurant for a lunch on me? You don’t have to dine with me; just enjoy a free lunch as a token of my appreciation."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "That's a very kind offer, and I do appreciate it. As a doctor, I usually have to be cautious about accepting gifts or offers, but a meal at your restaurant sounds lovely. Given that it's a public place and a professional setting, I think it would be acceptable. I can certainly stop by for a meal. It would also give me a chance to support your culinary endeavors, which I've always found intriguing."

                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg
                                                                player "Fantastic! Let me know when you plan to come, and I'll make sure everything is set up for a great dining experience."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "I will, thank you. It's a generous gesture, and I look forward to trying your creations."

                                                            if myrandom == 2:
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "I understand and respect your boundaries. Maybe you could come to my restaurant for a lunch? You won't have to dine with me; just enjoy a meal on the house as a way of expressing my gratitude."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "Thank you for being so considerate and for the invitation. While I am usually careful about accepting personal offers, a meal at your restaurant, under professional circumstances, seems appropriate. I'd be happy to visit your restaurant. It's a good opportunity to experience your culinary skills, which I've heard so much about."
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "Great! Just let me know when you're coming, and I'll ensure that you have a wonderful meal."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "I'll definitely take you up on that. Thank you for the offer, and I'll let you know when I can make it."

                                                            if myrandom == 3:
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "I completely understand your need for professional boundaries. How about just coming over to my restaurant for a complimentary lunch? There's no need for us to dine together; consider it a gesture of my appreciation for your advice."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "That's very generous of you. While I usually have to be careful about accepting gifts, a lunch at your restaurant seems like a nice gesture that falls within professional limits. I'd be happy to visit and experience your cooking. It's always wonderful to see the passion of a skilled chef in their element."
                                                                $ position = "hayoonhospitaltalklisten"
                                                                call sceneimg

                                                                player "I'm glad to hear that. Just give me a heads up when you decide to come, and I'll make sure you're well taken care of."
                                                                $ position = "hayoonhospitaltalktalk"
                                                                call sceneimg

                                                                HaYoon "Thank you, I appreciate it. I'm looking forward to it and will let you know."
                                                                jump hayoonghospitalgoodbye
                                                            
                                                        "Nevermind, next time":
                                                            jump hayoonghospitalgoodbye
                                                "Nevermind, next time":
                                                    jump hayoonghospitalgoodbye
                                        "Nevermind, next time":
                                            jump hayoonghospitalgoodbye     
                                "Nevermind, next time":
                                    jump hayoonghospitalgoodbye
                        "Nevermind, next time":
                            jump hayoonghospitalgoodbye
                "Nevermind, next time":
                    jump hayoonghospitalgoodbye
        "Make her a compliment" if hayoonfasteater == 1:
            $ myrandom = renpy.random.randint(1,2)
            if myrandom == 1:
                $ hayoon_attitude += 1
                $ reputationchange = 1
                $ nigirlimage = "nihayoon"
                call reputationchange
                $ myrandom = renpy.random.randint(1,10)
                if myrandom == 1:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Ha-Yoon, I couldn't help but notice you seem a bit uncomfortable. Is everything okay?"
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Oh, it's just a bit of bloating. It happens sometimes after a quick meal during my short breaks at the hospital. Nothing to worry about, but thanks for your concern."

                if myrandom == 2:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Looks like the hospital canteen food is treating you well, Ha-Yoon!"
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Ha! More like treating me to a bloated belly. The perils of eating in a rush, I guess."

                if myrandom == 3:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Ha-Yoon, as a doctor, what's your take on occasional bloating like yours?"
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Well, it's common among medical professionals given our hectic schedules. It's not ideal, but I try to manage it with proper hydration and healthier meal choices when I can."

                if myrandom == 4:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "I see your belly looks a bit bloated, Ha-Yoon. Does that bother you?"
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "It's a bit uncomfortable, but it comes with the territory of hospital work. I try to not let it bother me too much."

                if myrandom == 5:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Heading for a quick lunch again, Ha-Yoon? Hopefully, it won’t leave you feeling too bloated this time."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "One can only hope, right? It's the downside of eating on the run, but I've gotten used to it."

                if myrandom == 6:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Do you ever find that your eating habits at the hospital affect your digestion, Ha-Yoon?"
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Definitely. Rapid eating often leads to this bloating. It’s a reminder to slow down, but finding the time is another story."

                if myrandom == 7:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "I notice you're a bit bloated. Maybe trying some digestive tea might help?"
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "That's a good suggestion. I do try to incorporate herbal teas into my routine. They can be quite soothing."

                if myrandom == 8:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Your schedule must be really packed, Ha-Yoon. I can tell by your bloated belly."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Yes, it's a telltale sign of my grab-and-go lunches. Not the best for digestion, but it’s often all the time I have."

                if myrandom == 9:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Seeing your bloated belly, Ha-Yoon, makes me think about the health implications of rushed eating."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "You're right. It’s not ideal for health. I try to mitigate it with other healthier habits and mindful eating when possible."

                if myrandom == 10:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Ha-Yoon, maybe some yoga or stretching might help with the bloating?"
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "That's a great idea. I do try to incorporate some yoga into my weekly routine. It helps quite a bit with digestion and stress."
            if myrandom == 2:
                $ hayoon_attitude += 1
                $ reputationchange = 1
                $ nigirlimage = "nihayoon"
                call reputationchange
                $ myrandom = renpy.random.randint(1,10)
                if myrandom == 1:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "I can only imagine the tight schedule you must have, Ha-Yoon. It's impressive how you manage, even if it means eating quickly and feeling full."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Yes, it can get quite hectic, and sometimes I do feel very full. But it's part of the job, and I try to handle it as best as I can."

                if myrandom == 2:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "The way you cope with the demands of your job, even when it leaves you feeling uncomfortably full, really shows your strength."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Thank you. It's not always comfortable, but I've learned to adapt and stay focused on my work."

                if myrandom == 3:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Despite the challenges, like sometimes feeling overly full from quick meals, your dedication to your work is truly admirable, Ha-Yoon."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "That's very kind of you. Yes, the quick meals can be a challenge, but I'm committed to my work."

                if myrandom == 4:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "I see how hard you work, Ha-Yoon, even if it means occasionally dealing with the discomfort of feeling too full. Your commitment is commendable."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Thanks, I appreciate that. It can be a bit uncomfortable at times, but it's part of the job."

                if myrandom == 5:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Your effort in managing everything, even when it leads to feeling tight and full, doesn't go unnoticed, Ha-Yoon."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "I'm glad to hear that. It's not always easy, but I do my best to balance everything."

                if myrandom == 6:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "It must be tough sometimes, feeling so full because of the rushed meals. Yet, you handle it with such grace, Ha-Yoon."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "It can be tough, yes. But I try to stay positive and deal with it as best as I can."

                if myrandom == 7:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Even when you're feeling overly full from your busy schedule, your strength and resilience shine through, Ha-Yoon."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Thank you for saying that. It's a challenge, but one that I've learned to manage."

                if myrandom == 8:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "I understand the challenges of your job, like occasionally feeling tight after a quick meal. Your ability to keep going is inspiring."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "That's very kind of you. Yes, it's challenging, but I keep pushing forward."

                if myrandom == 9:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "Your adaptability in managing your work and meals, even when it leads to a feeling of tightness, is impressive, Ha-Yoon."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "Adaptability is key in my profession. Thank you for noticing and for your understanding."

                if myrandom == 10:
                    $ position = "hayoonhospitaltalklisten"
                    call sceneimg
                    player "The professionalism you maintain, even under circumstances like feeling uncomfortably full, is remarkable, Ha-Yoon."
                    $ position = "hayoonhospitalstretching"
                    call sceneimg
                    HaYoon "I try to maintain professionalism at all times. Thank you for recognizing that."
        "Nevermind, next time":
            jump hayoonghospitalgoodbye




    

    # he asked because she is a doctor
    


    # he asked because he saw her with huge belly and thought she might like it
    #player about her belly fetish
    

    


    


    


        #will she mind if he will ask her out for lunch, lunch will be on him? Knowing he has the fetish? NO
    



    #how about coming to his restaurant and lunch will be on him, but no company, she can just have free lunch. YES
    

    

    # bloated
    


    


jump hayoonhospital


label hayoonghospitalgoodbye:

    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        $ position = "hayoonhospitaltalklisten"
        call sceneimg
        player "Ha-Yoon, I really appreciate the time you've taken today to talk with me, especially considering your busy schedule. It means a lot that you're so open and understanding. I hope I haven't kept you too long. Have a great rest of your day, and take care of yourself. I look forward to our next chat, maybe under less rushed circumstances."
        $ position = "hayoonhospitaltalkhello"
        call sceneimg
        HaYoon "Thank you for your kind words. I'm glad we had this conversation, and it's always a pleasure to talk with someone who understands the demands of my job. Don't worry, you haven't kept me. Take care as well, and I'm sure we'll have another opportunity to catch up soon."

    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 2:
        $ position = "hayoonhospitaltalklisten"
        call sceneimg

        player "Today's conversation has been enlightening, Ha-Yoon. Your insights and understanding have been incredibly valuable. I'm grateful for the time you've shared with me, given how hectic your days can be. I'll let you get back to your responsibilities. Have a wonderful rest of the day, and hopefully, we can continue our discussions another time."
        $ position = "hayoonhospitaltalkhello"
        call sceneimg
        HaYoon "It was my pleasure to share this time with you. I'm always happy to provide insights where I can. Thank you for being so understanding and respectful of my time. Have a great day too, and I look forward to our future conversations."

    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 3:   
        $ position = "hayoonhospitaltalklisten"
        call sceneimg 

        player "Ha-Yoon, thank you for taking the time to discuss everything today, especially considering the little free time you have. Your perspective and advice have been invaluable. I hope you have a relaxing rest of your day, and let's definitely plan to reconnect when both our schedules allow."
        $ position = "hayoonhospitaltalkhello"
        call sceneimg
        HaYoon "You're very welcome. I'm glad I could offer some perspective and help in any way. Thank you for being considerate of my schedule. Enjoy the rest of your day as well, and I'm looking forward to our next meeting."


jump culinarychoices