label linfedcomments:
    
    $ myrandom = renpy.random.randint(1,20)
    if myrandom == 1:

        Lin "Oh wow, this is so delicious, but I'm incredibly full. My belly feels like a balloon ready to pop!"
        player "I'm glad you like it, Lin. It's great to see someone appreciate my cooking, even with a belly as round and full as yours."
    if myrandom == 2:

        Lin "Every bite is amazing, but I think I'm reaching my limit. I feel like I'm going to burst!"
        player "Your enjoyment means a lot to me. But let's not push you too far. Your belly looks quite firm and stretched already."
    if myrandom == 3:

        Lin "This is so tasty, but I'm so stuffed. My stomach is so round, I might roll down the hill!"
        player "I appreciate your kind words about my food. And yes, your belly does look pleasantly full and round. Just like a well-satisfied diner."
    if myrandom == 4:

        Lin "I can't believe how much I've eaten. I'm so bloated, my stomach is tight as a drum!"
        player "It's a compliment to any chef to see someone enjoy their food to the max. But let's be careful; your belly looks incredibly taut."
    if myrandom == 5:

        Lin "Each bite is better than the last, but I think one more might make me explode!"
        player "I'm thrilled you enjoy the flavors so much. Your belly does look like it's at its limit, though. We should take a break."
    if myrandom == 6:

        Lin "Your cooking is irresistible, but I'm so full, it feels like my belly could pop any second."
        player "I love seeing someone relish my dishes, but your comfort is important too. Your belly looks like it's had quite the feast!"
    if myrandom == 7:

        Lin "Seriously, how do you make everything taste so good? But I’m so bloated, it’s like I'm pregnant!"
        player "Thank you, Lin. Cooking is my passion. And well, your belly does have that satisfied, pregnant-like roundness to it."
    if myrandom == 8:
        Lin "I can't get enough of this, but I'm so stuffed, my stomach feels like it's stretching to the max."
        player "Your words are music to a chef's ears. But I can see your belly is really stretched out. Let's not overdo it."
    if myrandom == 9:

        Lin "This is heavenly, but I'm beyond full. My belly is so swollen, I feel like a balloon!"
        player "It's always a joy to feed an enthusiastic eater like you, even with a belly as swollen and bloated as yours right now."
    if myrandom == 10:

        Lin "Everything is so flavorful, but I'm about to burst. My stomach is so distended!"
        player "I'm glad you're enjoying the meal. But we should be mindful; your belly is looking incredibly distended and full."
    if myrandom == 11:

        Lin "I can't say no to your cooking, but my stomach is so tight and round, like I've swallowed a beach ball!"
        player "Your enjoyment of the food is clear, but let's be cautious. Your belly looks as round and tight as you describe."
    if myrandom == 12:


        Lin "How do you do it? Every bite is a delight, but my belly's so stuffed, it's hard as a rock!"
        player "It's all about passion for the ingredients. And your belly does look impressively firm and stuffed."
    if myrandom == 13:

        Lin "I've never felt so full. My stomach is like a tight, overstuffed pillow!"
        player "That's quite the image, Lin! Your belly does seem exceptionally full. We should take it easy now."
    if myrandom == 14:

        Lin "Your dishes are irresistible, but I'm so bloated, I feel like I'm carrying twins!"
        player "It's great to hear you love my cooking so much. Your belly certainly looks as though it's carrying a hefty, satisfying load."
    if myrandom == 15:

        Lin "Each mouthful is amazing, but my belly's stretched to its limit. It’s so round and protruding!"
        player "I'm flattered by your praise. Your belly's roundness is a testament to your appreciation, but let's not push you too far."
    if myrandom == 16:

        Lin "This is the best, but I'm so overfull. My stomach is sticking out so much!"
        player "Your love for the food is clear, but your comfort matters too. Your belly does look quite prominently full."
    if myrandom == 17:


        Lin "You're an incredible cook, but I'm at my breaking point. My belly is bulging out!"
        player "Thank you, Lin. I can see you're quite full, with your belly bulging like that. Let's pause for now."
    if myrandom == 18:

        Lin "I don’t know how you do it, but every bite is a delight. However, my belly's so swollen, it feels like it's going to pop!"
        player "I'm honored you enjoy the food, but let's be mindful of your fullness. Your belly does look quite swollen and tight."
    if myrandom == 19:

        Lin "Your cooking is too good, but I'm stuffed to the brim. My stomach's so bloated, I feel huge!"
        player "It's a joy to cook for someone who appreciates good food. But I can see your belly's bloatedness; we should take a break."
    if myrandom == 20:

        Lin "Everything tastes incredible, but I've never felt so full. My stomach's so tight and bloated!"
        player "I'm glad you like it, but let's not overdo it. Your belly is visibly tight and full. Time to rest and digest."

    return

label linistoofull:
       
    $ myrandom = renpy.random.randint(1,18)
    if myrandom == 1:
        Lin "This is so delicious, but I'm seriously full. Another bite and I might just burst!"
        player "I'm glad you enjoy it, Lin. It's great to see someone appreciate my cooking, though I can see your belly's quite round and full. Let's take a break."
    if myrandom == 2:

        Lin "Your food is amazing, but I'm at my limit. My belly feels like it's going to explode!"
        player "Your enjoyment means a lot, Lin. But let's not push it. Your belly does look incredibly firm and stretched."
    if myrandom == 3:

        Lin "I can't believe how full I am. My stomach is so round, I feel like I'm pregnant!"
        player "I appreciate your kind words, Lin. But we should listen to your body. Your belly looks comfortably full, almost pregnant-like."
    if myrandom == 4:

        Lin "Every bite is delicious, but I think I need to stop now. I'm so bloated!"
        player "It's a compliment to a chef to see such appreciation. But I agree, it's time to stop. Your belly looks really bloated."
    if myrandom == 5:

        Lin "I love your cooking, but I'm too full. I feel like my belly is going to pop!"
        player "Thanks, Lin. It's good to know when to pause. Your belly does look like it's had quite the feast!"
    if myrandom == 6:

        Lin "This is wonderful, but I'm overstuffed. My stomach is tight as a drum!"
        player "I'm thrilled you like the flavors, but let's take it easy. Your belly looks incredibly taut and full."
    if myrandom == 7:

        Lin "I can't get enough of this, but I really should stop. I'm about to burst!"
        player "I'm glad you enjoy the meal, Lin. But we should respect your fullness. Your belly does look like it's at its limit."
    if myrandom == 8:

        Lin "Your cooking is irresistible, but I'm so full I might explode. Time to stop, I think."
        player "I love seeing someone relish my dishes. But it's important not to overdo it. Your belly looks extremely stretched."
    if myrandom == 9:

        Lin "I've never felt so full. My stomach is like a tight, overstuffed pillow!"
        player "That's quite the image, Lin. Your belly does seem exceptionally full. Let's give it a rest."
    if myrandom == 10:

        Lin "Your dishes are amazing, but I've reached my limit. My belly is so swollen!"
        player "It's great to hear you love my cooking so much. But let's take care of your comfort. Your belly is impressively swollen."
    if myrandom == 11:

        Lin "I can't say no to your cooking, but my stomach is so tight and round now. No more for me."
        player "Your enjoyment of the food is clear, Lin. But let's be cautious. Your belly looks as round and tight as you describe."
    if myrandom == 12:

        Lin "How do you make everything so tasty? But I'm full to the brim. My belly's so stuffed!"
        player "Thanks, Lin. Cooking is my passion. But we shouldn't push your limits. Your belly looks very full and firm."
    if myrandom == 13:

        Lin "I've never been this full. My stomach is sticking out so much, I have to stop!"
        player "Your words are music to a chef's ears. But we don't want to make you uncomfortable. Your belly does look quite protruding."
    if myrandom == 14:

        Lin "Everything's so good, but I'm overstuffed. My stomach feels like it's going to pop!"
        player "I'm honored you enjoy the food, but let's not overdo it. Your belly looks like it's stretched to its maximum."
    if myrandom == 15:

        Lin "Your cooking is too good, but I'm so stuffed. I feel huge, like I'm carrying twins!"
        player "It's a joy to cook for someone who appreciates good food. But your belly looks like it's carrying quite a load!"
    if myrandom == 16:

        Lin "Each mouthful is amazing, but my belly's stretched to its limit. No more for me."
        player "I'm flattered by your praise, Lin. But let's respect your fullness. Your belly is indeed very round and tight."
    if myrandom == 17:

        Lin "This is heavenly, but I've reached my limit. My stomach is bulging out!"
        player "Thank you, Lin. It's good to know when to stop. Your belly looks really full and bulging."
    if myrandom == 18:

        Lin "I don’t know how you do it, but I'm so full. My belly's swollen, I need"
    
    
    return



label lineatingcomments:
    $ reputationchange = 1
    $ nigirlimage = "nilin"
    call reputationchange
    
    $ myrandom = renpy.random.randint(1,18)
    if myrandom == 1:
        Lin "This dish is incredible! The flavors are so rich and well-balanced."
        player "I'm glad you like it, Lin. I put a lot of thought into getting the flavors just right."
    if myrandom == 2:

        Lin "I can't get enough of this. Every bite is a delight!"
        player "That's what I love to hear! Enjoy every bite. It’s made with care."
    if myrandom == 3:

        Lin "You've really outdone yourself. This is one of the best meals I've had."
        player "Thank you, Lin. It's always a pleasure to cook for someone who appreciates good food."
    if myrandom == 4:

        Lin "The texture here is perfect. How did you get it so tender?"
        player "A little culinary secret and patience. I’m glad it paid off."
    if myrandom == 5:

        Lin "I'm in love with this dish. It's just bursting with flavors!"
        player "I aimed to please the palate. It's great to see you enjoying it so much."
    if myrandom == 6:

        Lin "Wow, this is so good. You really are an amazing cook."
        player "Thanks, Lin. Cooking is my passion, and I’m happy to share it with you."
    if myrandom == 7:

        Lin "I could eat this all day. It's absolutely delicious."
        player "Feel free to have as much as you like. It’s all yours!"
    if myrandom == 8:

        Lin "This is so comforting. It’s like a hug in a bowl."
        player "That’s exactly the vibe I was going for. Comfort food at its best."
    if myrandom == 9:

        Lin "Your culinary skills never cease to amaze me. This is superb."
        player "I appreciate that, Lin. I always strive to bring something special to the table."
    if myrandom == 10:

        Lin "The combination of flavors here is genius. I wouldn’t change a thing."
        player "I’m thrilled you think so. Finding the right balance is key."
    if myrandom == 11:

        Lin "This meal is just perfect. You've really outdone yourself."
        player "Thank you! It’s rewarding to see my dishes enjoyed like this."
    if myrandom == 12:

        Lin "Every time I eat your cooking, it's a new experience. This is fantastic."
        player "I love keeping it fresh and exciting. Glad you’re enjoying the experience."
    if myrandom == 13:

        Lin "You could open a restaurant with dishes like this. It's that good."
        player "That’s quite the compliment! Maybe one day, Lin."
    if myrandom == 14:

        Lin "I feel so spoiled eating this. It's like a gourmet meal."
        player "You deserve it, Lin. It’s my way of showing appreciation."
    if myrandom == 15:

        Lin "I'm savoring every bite. It’s just so tasty!"
        player "That’s the best way to enjoy a meal. Take your time and relish it."
    if myrandom == 16:

        Lin "You’ve got a gift for cooking. This is simply amazing."
        player "Thanks, Lin. Cooking is an art, and I love sharing it with friends."
    if myrandom == 17:

        Lin "This is so fulfilling. I can't believe how good this is."
        player "I’m glad to hear that. There’s nothing like a fulfilling meal."
    if myrandom == 18:

        Lin "Your cooking never disappoints. It’s always a treat."
        player "I’m happy to hear you think so. It's always fun to cook for you."
    if myrandom == 19:

        Lin "I can’t help but smile with every bite. It’s just that delicious."
        player "Seeing you smile makes the effort all worth it."
    if myrandom == 20:

        Lin "This is exactly what I needed. You're an incredible chef."
        player "I’m just happy to provide a meal that hits the spot for you."

    return




label linvomitcomments:
    $ myrandom = renpy.random.randint(1,20)

    if myrandom == 1:
        Lin "Ugh... I feel like I'm going to be sick. My belly is way too full..."
        player "Easy, Lin... Let's get you some fresh air. You don't want to push yourself any further."

    elif myrandom == 2:
        Lin "I can taste the food coming back up... I’m really nauseous."
        player "Take deep breaths, Lin. I’m sorry if I overdid it with the portions."

    elif myrandom == 3:
        Lin "Oh no... My stomach is churning. I feel like I could throw up any second."
        player "Try to relax. We can stop right now and let you recover. It’s okay."

    elif myrandom == 4:
        Lin "This pressure in my stomach... I’m worried I might lose it all."
        player "Let’s slow down, Lin. No need to force yourself. Your comfort comes first."

    elif myrandom == 5:
        Lin "I’m so stuffed… I’m afraid one more bite will make me hurl."
        player "Alright, no more food. Let me help you lie down or sit up straighter."

    elif myrandom == 6:
        Lin "I feel so sick. I really might vomit if I don’t stop eating."
        player "You’ve already had enough. Let's get you settled so you don’t feel worse."

    elif myrandom == 7:
        Lin "Oh gosh... My stomach keeps lurching. I can’t hold everything down much longer."
        player "Breathe, Lin. We’ll pause here. I'll get you some water and a cool towel."

    elif myrandom == 8:
        Lin "I’m so nauseous, everything I’ve eaten feels like it’s stuck in my throat."
        player "Just relax, Lin. We’ll take a break until the nausea passes."

    elif myrandom == 9:
        Lin "My stomach’s so tight, I'm sure I'll end up throwing up if this keeps up."
        player "No more pushing your limits. Let’s help you feel better instead."

    elif myrandom == 10:
        Lin "I can’t believe I overate this much… I’m seriously going to throw up."
        player "It’s okay, Lin. Mistakes happen. Just focus on calming your stomach now."

    elif myrandom == 11:
        Lin "My belly hurts, and I feel like I'm going to be sick any moment."
        player "Let’s get you somewhere comfortable. I’ll stay with you until it passes."

    elif myrandom == 12:
        Lin "I’m trying not to gag… This was way too much for me."
        player "I’m sorry, Lin. I should’ve watched your limits more carefully. Let’s stop right now."

    elif myrandom == 13:
        Lin "Oh no… I feel a wave of nausea. I think it’s too late to keep this down."
        player "Deep breaths. Let’s see if we can keep you from actually vomiting. I’ve got you."

    elif myrandom == 14:
        Lin "Everything is spinning… I’m so full, I'm certain I'll throw up."
        player "Hang on, Lin. I’ll get you some water and a cool cloth. We’ll make sure you’re okay."

    elif myrandom == 15:
        Lin "I can’t hold it in much longer… My belly is rebelling."
        player "It’s alright, Lin. Let’s get you up slowly, maybe walk a bit for some relief."

    elif myrandom == 16:
        Lin "Ugh… I shouldn’t have forced that last bite. I’m about to puke."
        player "Let’s not worry about politeness. If you need to let it out, do it. I'll help clean up."

    elif myrandom == 17:
        Lin "My stomach is cramping... I'm moments away from losing it all."
        player "No more food, no more pressure. Let’s help you recover. It’ll pass, I promise."

    elif myrandom == 18:
        Lin "I feel so bloated and nauseous… I hate to say it, but I think I’m going to vomit."
        player "I’m sorry, Lin. Let’s find a place to sit or lie down until the feeling subsides."

    elif myrandom == 19:
        Lin "I can't stop gagging. My belly is way beyond full."
        player "We’ll stop everything right now. Let’s get you somewhere calm before it gets worse."

    else:  # myrandom == 20
        Lin "I regret having that extra helping... I can feel it all trying to come back up."
        player "Don’t blame yourself. Let's take care of you, step by step."

    return