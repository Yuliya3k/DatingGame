label promcafe:

    if lin_cafetoday == 1 and calendar.Hours >= 18:
        
        # $ position = "parkpromlincafesittingfar"
        # call sceneimg
        "As I approach the beach cafe, my eyes immediately lock onto Lin. She's sitting there, bathed in the warm, golden glow of the setting sun. Lin is wearing a stunning golden metallic dress that shimmers and reflects the fading daylight. The dress drapes gracefully over her toned figure, catching the hues of the evening sky and blending seamlessly with the colors of the sunset."
        # $ position = "parkpromlincafesittingapproaching"
        # call sceneimg
        "Her hair, styled effortlessly, cascades down her shoulders, catching the last rays of daylight and creating an ethereal aura around her. The gentle breeze tousles her hair slightly, adding to the natural elegance of the moment."
        if (calendar.Hours == 19 and calendar.minutes == 0) or (calendar.Hours == 18 and calendar.minutes >= 00):
            # $ position = "parkpromlincafesittingapproachinghappy"
            # call sceneimg
            Lin "Hey there! Right on time, I see. I appreciate punctuality."
            $ position = "parkpromlincafesittinglistening"
            call sceneimg
            player "Wouldn't dream of keeping you waiting. You look absolutely stunning, by the way. That dress suits you perfectly."
            $ position = "parkpromlincafesittingtalking"
            call sceneimg
            Lin "Thank you! You're not looking too shabby yourself. Shall we grab a table with a view?"
            $ position = "parkpromlincafesittinglistening"
            call sceneimg
            player "Absolutely. A view like this deserves our full attention."
            jump linpromcafetalk
            $ lin_cafetoday = 0
        if (calendar.Hours == 19 and calendar.minutes > 14):
            $ lin_cafetoday = 0
            
            $ reputationchange = -15
            $ nigirlimage = "nilin"
            call reputationchange
                
            if lintoolate == 0:
                
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                Lin "You're late. I specifically mentioned 19:00, and I don't appreciate waiting."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg
                player "I'm really sorry, Lin. I got held up at work, and I lost track of time. It won't happen again."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg
                Lin "Well, alright. Just this once, then. Let's not dwell on it. Grab a seat, and let's enjoy our dinner."
                jump linpromcafetalk
            if lintoolate == 1:
                
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                Lin "Seriously? You're late again? I can't believe this."
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                player "I know, I know, Lin. I'm really sorry. It's just been a crazy day."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg
                Lin "This is the second time you've kept me waiting. It's disrespectful, you know."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg
                player "I understand, Lin. I messed up, and I'm genuinely sorry. I'll make it up to you, I promise."
                $ position = "parkpromlincafesittingtalking"
                call sceneimg
                Lin "Fine, but you owe me big time. Let's just have dinner now and try to salvage what's left of the evening."
                jump linpromcafetalk
            if lintoolate == 2:
                
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                Lin " (exasperated) [name], you're late again? This is becoming a pattern, and I can't tolerate it any longer."
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                player "Lin, I'm really sorry. I got caught up with work, and I lost track of time."
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                Lin "That's no excuse. I've been patient, but this is the third time. It's disrespectful and shows a lack of consideration."
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                player "I understand, Lin. I messed up, and I should have been more responsible. I'm really sorry."
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                Lin "I think it's best if we end this here. I can't keep waiting for someone who doesn't value my time."
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                player "Lin, please give me another chance. I promise it won't happen again."
                $ position = "linpromcafesittingtalkangry"
                call sceneimg
                Lin "I'm sorry, but I need someone who respects my time and commitments. Goodbye, [name]."
            $ lintoolate += 1
            

    else:
        if promcafe < 5:
            
            $ position = "parkpromcafeempty"
            call sceneimg
            "It is not working yet"
            $ promcafe += 1
        if promcafe >= 5:
            $ promcafetoday = 1
            $ myrandom = renpy.random.randint(1,2)
            if myrandom == 1:
                $ mindy_fullness = renpy.random.randint(1,4000)
                $ position = "parkmindycafeenterance"
                call sceneimg
                "Looks like it is opened now"
            if myrandom == 2 and lin_cafetoday == 0 and calendar.Hours >= 18:
                $ position = "parkpromcafelincomingin"
                call sceneimg
                "Looks like Lin enters the cafe. She does not notice you"
                
            else:
                $ mindy_fullness = renpy.random.randint(1,4000)
                $ position = "parkmindycafeenterance"
                call sceneimg
                "Looks like it is opened now"
            jump park

    return