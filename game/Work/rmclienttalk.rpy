label rmclienttalk:
    
    $ myrandom = renpy.random.randint(1,5)
    

    if myrandom == 1:
        Margo "Hey, could you do me a favor? One of our regulars, Mrs. Anderson, is here tonight, and she's been asking for a word with you."

        player "Mrs. Anderson? What does she want with me?"

        Margo "I'm not entirely sure, but she's been coming here for years. She might have some feedback or just want to chat. You know how particular she is about her meals."

        player "Alright, I'll go talk to her. Is she at her usual table?"

        Margo "Yes, she's in her favorite spot by the window. Thanks, I appreciate it."
        
        call mrsanderson

    if myrandom == 2:
        Margo "Hey, could you do me a favor? One of our regulars, Mrs. Anderson, is here tonight, and she's been asking for a word with you."

        player "Mrs. Anderson? Sure, I'll go see what she needs."

        Margo "Thanks, I knew I could count on you. She's at her usual table by the window."

        call mrsanderson

    if myrandom == 3:
        Margo "Hey, could you do me a favor? One of our regulars, Mrs. Anderson, is here tonight, and she's been asking for a word with you."

        player "Mrs. Anderson again? What's it this time?"

        Margo "You know her, always particular about her meals. She might have some suggestions or feedback. Please, it would mean a lot if you could chat with her."

        player "Fine, I'll go over there. Is she at her usual table?"

        Margo "Yes, she's sitting by the window."

        call mrsanderson

    if myrandom == 4:
        Margo "Hey, could you do me a favor? One of our regulars, Mrs. Anderson, is here tonight, and she's been asking for a word with you."

        player "Mrs. Anderson? That's interesting. I'll go see what she wants."

        Margo "Great! She's sitting at her usual table near the window."

        call mrsanderson

    if myrandom == 5:
        Margo "Hey,  could you do me a favor? One of our regulars, Mrs. Anderson, is here tonight, and she's been asking for a word with you."

        player "Mrs. Anderson? What does she want with me?"

        Margo "I'm not entirely sure, but she's been coming here for years. She might have some feedback or just want to chat. You know how particular she is about her meals."

        player "Alright, I'll go talk to her. Is she at her usual table?"

        Margo "Yes, she's in her favorite spot by the window. Thanks,  I appreciate it."

        call mrsanderson

    return



label mrsanderson:
    play music "audio/rmrestaurant.mp3" 
    $ myrandom = renpy.random.randint(1,5)
    $ julia_fullness = renpy.random.randint(800,4000)
    $ position = "rmjuliasit"
    call sceneimg

        

    if myrandom == 1:

        player "Mrs. Anderson, I heard you wanted to talk to me. How can I assist you today?"

        Julia "Oh,  it's such a delight to see you! I just had to let you know how absolutely splendid my meal was tonight."

        player "Thank you, Mrs. Anderson! I'm thrilled to hear that you enjoyed it. What specifically did you like about your meal?"

        Julia "Well, first of all, the presentation was impeccable. That dish you recommended, the Grilled Salmon with Lemon Herb Sauce, was a masterpiece. It looked as good as it tasted."

        player "I'm glad to hear that the presentation met your expectations. And how was the taste?"

        Julia "Oh, the taste,  it was divine! The salmon was cooked to perfection, so tender and flavorful. And that lemon herb sauce, my goodness, it was like a burst of sunshine on my plate."

        player "I'm so happy you enjoyed it. We take great care in preparing our dishes to ensure they're perfect for our valued guests like you."

        Julia "It certainly shows, dear. Your attention to detail and commitment to excellence shine through. This is why I keep coming back to this restaurant."

        player "Thank you for your kind words, Mrs. Anderson. We truly appreciate your patronage and feedback. If there's anything else I can assist you with, please don't hesitate to let me know."

        Julia "No, everything was simply perfect tonight. You've made my evening. Please convey my compliments to the chef."

        player "Of course, Mrs. Anderson. I'll be sure to pass along your compliments. It was a pleasure serving you tonight."

        Julia "Keep up the exceptional work. Good night, dear!"

        player "Thank you, Mrs. Anderson. Have a wonderful night!"

    if myrandom == 2:

        player "Mrs. Anderson, Margo said you wanted to talk to me. What can I do for you?"

        Julia "Oh,  it's you. I must say, the meal was quite satisfactory tonight."

        player "Thank you, Mrs. Anderson. We're glad you enjoyed it. Is there anything specific that stood out to you?"

        Julia "Well, the portion size was adequate, and the flavors were decent. Not exceptional, but decent."

        player "I see. We appreciate your feedback. We're always working to improve."

        Julia "That's good to hear. Just a bit more attention to detail next time, dear."

        player "Certainly, Mrs. Anderson. We'll strive to do better. Thank you for dining with us."

    if myrandom == 3:

        player "Mrs. Anderson, Margo said you wanted to talk. What's on your mind?"

        Julia "Oh,  I must say, tonight's meal left much to be desired."

        player "I'm sorry to hear that, Mrs. Anderson. Can you please share what you didn't like about it?"

        Julia "Firstly, the portion size was far too small. I left here hungry. And the flavors were quite bland, nothing memorable."

        player "I apologize for the disappointment, Mrs. Anderson. Your feedback is valuable, and we'll work on improving."

        Julia "Well, I hope so. I've had better meals elsewhere. Don't let this happen again."

        player "We'll do our best to make your next visit a better one. Thank you for bringing this to our attention."

    if myrandom == 4:

        player "Mrs. Anderson, Margo mentioned you wanted to talk to me. How can I assist you tonight?"

        Julia "Oh,  it's you. The meal was neither exceptional nor terrible tonight."

        player "Thank you for your honest feedback, Mrs. Anderson. We appreciate your patronage. Is there anything specific you'd like to mention?"

        Julia "Not really. It was just an average dining experience. Nothing more, nothing less."

        player "Understood, Mrs. Anderson. We aim to provide memorable experiences, and we'll strive to do better next time."

        Julia "Sure, whatever. Have a good evening."

        player "You too, Mrs. Anderson. Thank you for dining with us."

    if myrandom == 5:

        player "Mrs. Anderson, I heard you wanted to talk to me. How can I assist you today?"

        Julia "Oh,  I'm afraid I can't say I enjoyed my meal tonight."

        player "I'm truly sorry to hear that, Mrs. Anderson. What was the issue with your meal?"

        Julia "The dish I ordered, the Pasta Primavera, was overcooked, and the sauce lacked flavor. It was quite disappointing."

        player "I apologize for the culinary mishap, Mrs. Anderson. We aim to provide a better experience. Your feedback will help us improve."

        Julia "Well, I hope so. I've had better Pasta Primavera at other places. Please, ensure it's better next time."

        player "We'll make sure to address this, Mrs. Anderson. Thank you for bringing it to our attention."


jump cook


