label girl:
    label g1girl:
        $ g1_fullnessoz = int(g1_fullness*0.034)



        $ g1_totalfullness = g1_fullness + g1_intfullness
        #if girl == "g1":
        if g1_totalfullness <= 400:
            $ g1_fullstage = 1
            if g1_near == 1 and g1_stage1 == 0:
                $ g1_stage1 = 1
                g1 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
        else:
            if g1_totalfullness <=800 and g1_totalfullness > 400:
                $ g1_fullstage =2
                if g1_near == 1 and g1_stage2 == 0:
                    $ g1_stage2 = 1
                    g1 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
            else:
                if g1_totalfullness <=1200 and g1_totalfullness > 800:
                    $ g1_fullstage =3
                    if g1_near == 1 and g1_stage3 == 0:
                        $ g1_stage3 = 1
                        g1 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                else:
                    if g1_totalfullness <=1600 and g1_totalfullness > 1200:
                        $ g1_fullstage =4
                        if g1_near == 1 and g1_stage4 == 0:
                            $ g1_stage4 = 1
                            g1 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                    else:
                        if g1_totalfullness <=2000 and g1_totalfullness > 1600:
                            $ g1_fullstage =5
                            if g1_near == 1 and g1_stage5 == 0:
                                $ g1_stage5 = 1
                                g1 "If you can keep feeding me like this, I might just make a new record!"
                        else:
                            if g1_totalfullness <=2400 and g1_totalfullness > 2000:
                                $ g1_fullstage =6
                                if g1_near == 1 and g1_stage6 == 0:
                                    $ g1_stage6 = 1
                                    g1 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                            else:
                                if g1_totalfullness <=2800 and g1_totalfullness > 2400:
                                    $ g1_fullstage =7
                                    if g1_near == 1 and g1_stage7 == 0:
                                        $ g1_stage7 = 1
                                        g1 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                else:
                                    if g1_totalfullness <=3200 and g1_totalfullness > 2800:
                                        $ g1_fullstage =8
                                        if g1_near == 1:
                                            if g1_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                g1 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                $ g1_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g1_totalfullness <=3600 and g1_totalfullness > 3200:
                                            $ g1_fullstage =9
                                            if g1_near == 1:
                                                if g1_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g1 "Did you hear that? I think that was my skin stretching"
                                                    $ g1_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g1_totalfullness <=4000 and g1_totalfullness > 3600:
                                                $ g1_fullstage =10
                                                if g1_near == 1:
                                                    if g1_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g1 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                        $ g1_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g1_totalfullness <=4400 and g1_totalfullness > 4000:
                                                    $ g1_fullstage =11
                                                    if g1_near == 1:
                                                        if g1_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g1 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                            $ g1_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g1_totalfullness <=4800 and g1_totalfullness > 4400:
                                                        $ g1_fullstage =12
                                                        if g1_near == 1:
                                                            if g1_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g1 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                $ g1_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g1_totalfullness <=5200 and g1_totalfullness > 4800:
                                                            $ g1_fullstage =13
                                                            if g1_near == 1:
                                                                if g1_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g1 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                    $ g1_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g1_totalfullness <=5600 and g1_totalfullness > 5200:
                                                                $ g1_fullstage =14
                                                                if g1_near == 1:
                                                                    if g1_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g1 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                        $ g1_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g1_totalfullness <=6000 and g1_totalfullness > 5600:
                                                                    $ g1_fullstage =15
                                                                    if g1_near == 1:
                                                                        if g1_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g1 "I don't know how I'm still eating!"
                                                                            $ g1_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g1_totalfullness <=6400 and g1_totalfullness > 6000:
                                                                        $ g1_fullstage =16
                                                                        if g1_near == 1:
                                                                            if g1_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g1 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                $ g1_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g1_totalfullness <=6800 and g1_totalfullness > 6400:
                                                                            $ g1_fullstage =17
                                                                            if g1_near == 1:
                                                                                if g1_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g1 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                    $ g1_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g1_totalfullness <=7200 and g1_totalfullness > 6800:
                                                                                $ g1_fullstage =18
                                                                                if g1_near == 1:
                                                                                    if g1_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g1 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                        $ g1_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g1_totalfullness <=7600 and g1_totalfullness > 7200:
                                                                                    $ g1_fullstage =19
                                                                                    if g1_near == 1:
                                                                                        if g1_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g1 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                            $ g1_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g1_totalfullness <=8000 and g1_totalfullness > 7600:
                                                                                        $ g1_fullstage =20
                                                                                        if g1_near == 1:
                                                                                            if g1_stretch20 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                g1 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                $ g1_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g1_totalfullness > 8000:
                                                                                            $ g1_fullstage =20
                                                                                            if g1_near == 1:
                                                                                                if g1_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g1_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g1_maxfulltext == 0:
                                                                                                        g1 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                    if g1_maxfulltext == 1:
                                                                                                        $ g1_burp = renpy.random.randint(0,1)
                                                                                                        if g1_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g1_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        g1 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g1_maxfulltext == 2:
                                                                                                        g1 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                    $ g1_stretch21 += 1
                                                                                            else:
                                                                                                pass
        return


    label g2girl:
        $ g2_fullnessoz = int(g2_fullness*0.034)

        $ g2_totalfullness = g2_fullness + g2_intfullness
        #if girl == "g2":
        if g2_totalfullness <= 400:
            $ g2_fullstage = 1
            if g2_near == 1 and g2_stage1 == 0:
                $ g2_stage1 = 1
                g2 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
        else:
            if g2_totalfullness <=800 and g2_totalfullness > 400:
                $ g2_fullstage =2
                if g2_near == 1 and g2_stage2 == 0:
                    $ g2_stage2 = 1
                    g2 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
            else:
                if g2_totalfullness <=1200 and g2_totalfullness > 800:
                    $ g2_fullstage =3
                    if g2_near == 1 and g2_stage3 == 0:
                        $ g2_stage3 = 1
                        g2 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                else:
                    if g2_totalfullness <=1600 and g2_totalfullness > 1200:
                        $ g2_fullstage =4
                        if g2_near == 1 and g2_stage4 == 0:
                            $ g2_stage4 = 1
                            g2 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                    else:
                        if g2_totalfullness <=2000 and g2_totalfullness > 1600:
                            $ g2_fullstage =5
                            if g2_near == 1 and g2_stage5 == 0:
                                $ g2_stage5 = 1
                                g2 "If you can keep feeding me like this, I might just make a new record!"
                        else:
                            if g2_totalfullness <=2400 and g2_totalfullness > 2000:
                                $ g2_fullstage =6
                                if g2_near == 1 and g2_stage6 == 0:
                                    $ g2_stage6 = 1
                                    g2 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                            else:
                                if g2_totalfullness <=2800 and g2_totalfullness > 2400:
                                    $ g2_fullstage =7
                                    if g2_near == 1 and g2_stage7 == 0:
                                        $ g2_stage7 = 1
                                        g2 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                else:
                                    if g2_totalfullness <=3200 and g2_totalfullness > 2800:
                                        $ g2_fullstage =8
                                        if g2_near == 1:
                                            if g2_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                g2 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                $ g2_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g2_totalfullness <=3600 and g2_totalfullness > 3200:
                                            $ g2_fullstage =9
                                            if g2_near == 1:
                                                if g2_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g2 "Did you hear that? I think that was my skin stretching"
                                                    $ g2_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g2_totalfullness <=4000 and g2_totalfullness > 3600:
                                                $ g2_fullstage =10
                                                if g2_near == 1:
                                                    if g2_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g2 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                        $ g2_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g2_totalfullness <=4400 and g2_totalfullness > 4000:
                                                    $ g2_fullstage =11
                                                    if g2_near == 1:
                                                        if g2_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g2 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                            $ g2_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g2_totalfullness <=4800 and g2_totalfullness > 4400:
                                                        $ g2_fullstage =12
                                                        if g2_near == 1:
                                                            if g2_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g2 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                $ g2_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g2_totalfullness <=5200 and g2_totalfullness > 4800:
                                                            $ g2_fullstage =13
                                                            if g2_near == 1:
                                                                if g2_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g2 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                    $ g2_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g2_totalfullness <=5600 and g2_totalfullness > 5200:
                                                                $ g2_fullstage =14
                                                                if g2_near == 1:
                                                                    if g2_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g2 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                        $ g2_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g2_totalfullness <=6000 and g2_totalfullness > 5600:
                                                                    $ g2_fullstage =15
                                                                    if g2_near == 1:
                                                                        if g2_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g2 "I don't know how I'm still eating!"
                                                                            $ g2_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g2_totalfullness <=6400 and g2_totalfullness > 6000:
                                                                        $ g2_fullstage =16
                                                                        if g2_near == 1:
                                                                            if g2_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g2 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                $ g2_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g2_totalfullness <=6800 and g2_totalfullness > 6400:
                                                                            $ g2_fullstage =17
                                                                            if g2_near == 1:
                                                                                if g2_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g2 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                    $ g2_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g2_totalfullness <=7200 and g2_totalfullness > 6800:
                                                                                $ g2_fullstage =18
                                                                                if g2_near == 1:
                                                                                    if g2_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g2 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                        $ g2_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g2_totalfullness <=7600 and g2_totalfullness > 7200:
                                                                                    $ g2_fullstage =19
                                                                                    if g2_near == 1:
                                                                                        if g2_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g2 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                            $ g2_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g2_totalfullness <=8000 and g2_totalfullness > 7600:
                                                                                        $ g2_fullstage =20
                                                                                        if g2_near == 1:
                                                                                            if g2_stretch20 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                g2 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                $ g2_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g2_totalfullness > 8000:
                                                                                            $ g2_fullstage =20
                                                                                            if g2_near == 1:
                                                                                                if g2_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g2_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g2_maxfulltext == 0:
                                                                                                        g2 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                    if g2_maxfulltext == 1:
                                                                                                        $ g2_burp = renpy.random.randint(0,1)
                                                                                                        if g2_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g2_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        g2 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g2_maxfulltext == 2:
                                                                                                        g2 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                    $ g2_stretch21 += 1
                                                                                            else:
                                                                                                pass
        return

    label g3girl:
        $ g3_fullnessoz = int(g3_fullness*0.034)

        $ g3_totalfullness = g3_fullness + g3_intfullness
        #if girl == "g3":
        if g3_totalfullness <= 400:
            $ g3_fullstage = 1
            if g3_near == 1 and g3_stage1 == 0:
                $ g3_stage1 = 1
                g3 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
        else:
            if g3_totalfullness <=800 and g3_totalfullness > 400:
                $ g3_fullstage =2
                if g3_near == 1 and g3_stage2 == 0:
                    $ g3_stage2 = 1
                    g3 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
            else:
                if g3_totalfullness <=1200 and g3_totalfullness > 800:
                    $ g3_fullstage =3
                    if g3_near == 1 and g3_stage3 == 0:
                        $ g3_stage3 = 1
                        g3 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                else:
                    if g3_totalfullness <=1600 and g3_totalfullness > 1200:
                        $ g3_fullstage =4
                        if g3_near == 1 and g3_stage4 == 0:
                            $ g3_stage4 = 1
                            g3 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                    else:
                        if g3_totalfullness <=2000 and g3_totalfullness > 1600:
                            $ g3_fullstage =5
                            if g3_near == 1 and g3_stage5 == 0:
                                $ g3_stage5 = 1
                                g3 "If you can keep feeding me like this, I might just make a new record!"
                        else:
                            if g3_totalfullness <=2400 and g3_totalfullness > 2000:
                                $ g3_fullstage =6
                                if g3_near == 1 and g3_stage6 == 0:
                                    $ g3_stage6 = 1
                                    g3 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                            else:
                                if g3_totalfullness <=2800 and g3_totalfullness > 2400:
                                    $ g3_fullstage =7
                                    if g3_near == 1 and g3_stage7 == 0:
                                        $ g3_stage7 = 1
                                        g3 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                else:
                                    if g3_totalfullness <=3200 and g3_totalfullness > 2800:
                                        $ g3_fullstage =8
                                        if g3_near == 1:
                                            if g3_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                g3 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                $ g3_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g3_totalfullness <=3600 and g3_totalfullness > 3200:
                                            $ g3_fullstage =9
                                            if g3_near == 1:
                                                if g3_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g3 "Did you hear that? I think that was my skin stretching"
                                                    $ g3_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g3_totalfullness <=4000 and g3_totalfullness > 3600:
                                                $ g3_fullstage =10
                                                if g3_near == 1:
                                                    if g3_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g3 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                        $ g3_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g3_totalfullness <=4400 and g3_totalfullness > 4000:
                                                    $ g3_fullstage =11
                                                    if g3_near == 1:
                                                        if g3_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g3 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                            $ g3_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g3_totalfullness <=4800 and g3_totalfullness > 4400:
                                                        $ g3_fullstage =12
                                                        if g3_near == 1:
                                                            if g3_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g3 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                $ g3_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g3_totalfullness <=5200 and g3_totalfullness > 4800:
                                                            $ g3_fullstage =13
                                                            if g3_near == 1:
                                                                if g3_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g3 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                    $ g3_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g3_totalfullness <=5600 and g3_totalfullness > 5200:
                                                                $ g3_fullstage =14
                                                                if g3_near == 1:
                                                                    if g3_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g3 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                        $ g3_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g3_totalfullness <=6000 and g3_totalfullness > 5600:
                                                                    $ g3_fullstage =15
                                                                    if g3_near == 1:
                                                                        if g3_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g3 "I don't know how I'm still eating!"
                                                                            $ g3_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g3_totalfullness <=6400 and g3_totalfullness > 6000:
                                                                        $ g3_fullstage =16
                                                                        if g3_near == 1:
                                                                            if g3_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g3 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                $ g3_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g3_totalfullness <=6800 and g3_totalfullness > 6400:
                                                                            $ g3_fullstage =17
                                                                            if g3_near == 1:
                                                                                if g3_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g3 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                    $ g3_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g3_totalfullness <=7200 and g3_totalfullness > 6800:
                                                                                $ g3_fullstage =18
                                                                                if g3_near == 1:
                                                                                    if g3_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g3 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                        $ g3_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g3_totalfullness <=7600 and g3_totalfullness > 7200:
                                                                                    $ g3_fullstage =19
                                                                                    if g3_near == 1:
                                                                                        if g3_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g3 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                            $ g3_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g3_totalfullness <=8000 and g3_totalfullness > 7600:
                                                                                        $ g3_fullstage =20
                                                                                        if g3_near == 1:
                                                                                            if g3_stretch20 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                g3 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                $ g3_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g3_totalfullness > 8000:
                                                                                            $ g3_fullstage =20
                                                                                            if g3_near == 1:
                                                                                                if g3_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g3_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g3_maxfulltext == 0:
                                                                                                        g3 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                    if g3_maxfulltext == 1:
                                                                                                        $ g3_burp = renpy.random.randint(0,1)
                                                                                                        if g3_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g3_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        g3 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g3_maxfulltext == 2:
                                                                                                        g3 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                    $ g3_stretch21 += 1
                                                                                            else:
                                                                                                pass
        return
    label g4girl:
        $ g4_fullnessoz = int(g4_fullness*0.034)

        #if girl == "g4":
        if g4_fullness <= 400:
            $ g4_fullstage = 1
        else:
            if g4_fullness <=800 and g4_fullness > 400:
                $ g4_fullstage =2
            else:
                if g4_fullness <=1200 and g4_fullness > 800:
                    $ g4_fullstage =3
                else:
                    if g4_fullness <=1600 and g4_fullness > 1200:
                        $ g4_fullstage =4
                    else:
                        if g4_fullness <=2000 and g4_fullness > 1600:
                            $ g4_fullstage =5
                        else:
                            if g4_fullness <=2400 and g4_fullness > 2000:
                                $ g4_fullstage =6
                            else:
                                if g4_fullness <=2800 and g4_fullness > 2400:
                                    $ g4_fullstage =7
                                else:
                                    if g4_fullness <=3200 and g4_fullness > 2800:
                                        $ g4_fullstage =8
                                        if stretch8 < 1 and g4_clothes == 1:
                                            play sound "audio/skinstreatching short.mp3"
                                            $ stretch8 += 1
                                        else:
                                            pass
                                    else:
                                        if g4_fullness <=3600 and g4_fullness > 3200:
                                            $ g4_fullstage =9
                                            if stretch9 < 1 and g4_clothes == 1:
                                                play sound "audio/skinstreatching short.mp3"
                                                $ stretch9 += 1
                                            else:
                                                pass
                                        else:
                                            if g4_fullness <=4000 and g4_fullness > 3600:
                                                $ g4_fullstage =10
                                                if stretch10 < 1 and g4_clothes == 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    $ stretch10 += 1
                                                else:
                                                    pass
                                            else:
                                                if g4_fullness > 4000:
                                                    $ g4_fullstage =10
                                                    if explode10 < 1:
                                                        $ explode10 = 1
                                                        # a "[name], I can't be here any more, I'm eating constantly and I feel like I'm about to explode! Let's do some modeling, please!"
                                                    else:
                                                        pass
        return

    label g5girl:
        $ g5_fullnessoz = int(g5_fullness*0.034)

        $ g5_totalfullness = g5_fullness + g5_intfullness
        #if girl == "g5":
        if g5_totalfullness <= 400:
            $ g5_fullstage = 1
            if g5_near == 1 and g5_stage1 == 0:
                $ g5_stage1 = 1
                g5 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
        else:
            if g5_totalfullness <=800 and g5_totalfullness > 400:
                $ g5_fullstage =2
                if g5_near == 1 and g5_stage2 == 0:
                    $ g5_stage2 = 1
                    g5 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
            else:
                if g5_totalfullness <=1200 and g5_totalfullness > 800:
                    $ g5_fullstage =3
                    if g5_near == 1 and g5_stage3 == 0:
                        $ g5_stage3 = 1
                        g5 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                else:
                    if g5_totalfullness <=1600 and g5_totalfullness > 1200:
                        $ g5_fullstage =4
                        if g5_near == 1 and g5_stage4 == 0:
                            $ g5_stage4 = 1
                            g5 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                    else:
                        if g5_totalfullness <=2000 and g5_totalfullness > 1600:
                            $ g5_fullstage =5
                            if g5_near == 1 and g5_stage5 == 0:
                                $ g5_stage5 = 1
                                g5 "If you can keep feeding me like this, I might just make a new record!"
                        else:
                            if g5_totalfullness <=2400 and g5_totalfullness > 2000:
                                $ g5_fullstage =6
                                if g5_near == 1 and g5_stage6 == 0:
                                    $ g5_stage6 = 1
                                    g5 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                            else:
                                if g5_totalfullness <=2800 and g5_totalfullness > 2400:
                                    $ g5_fullstage =7
                                    if g5_near == 1 and g5_stage7 == 0:
                                        $ g5_stage7 = 1
                                        g5 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                else:
                                    if g5_totalfullness <=3200 and g5_totalfullness > 2800:
                                        $ g5_fullstage =8
                                        if g5_near == 1:
                                            if g5_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                g5 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                $ g5_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g5_totalfullness <=3600 and g5_totalfullness > 3200:
                                            $ g5_fullstage =9
                                            if g5_near == 1:
                                                if g5_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g5 "Did you hear that? I think that was my skin stretching"
                                                    $ g5_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g5_totalfullness <=4000 and g5_totalfullness > 3600:
                                                $ g5_fullstage =10
                                                if g5_near == 1:
                                                    if g5_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g5 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                        $ g5_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g5_totalfullness <=4400 and g5_totalfullness > 4000:
                                                    $ g5_fullstage =11
                                                    if g5_near == 1:
                                                        if g5_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g5 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                            $ g5_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g5_totalfullness <=4800 and g5_totalfullness > 4400:
                                                        $ g5_fullstage =12
                                                        if g5_near == 1:
                                                            if g5_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g5 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                $ g5_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g5_totalfullness <=5200 and g5_totalfullness > 4800:
                                                            $ g5_fullstage =13
                                                            if g5_near == 1:
                                                                if g5_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g5 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                    $ g5_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g5_totalfullness <=5600 and g5_totalfullness > 5200:
                                                                $ g5_fullstage =14
                                                                if g5_near == 1:
                                                                    if g5_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g5 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                        $ g5_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g5_totalfullness <=6000 and g5_totalfullness > 5600:
                                                                    $ g5_fullstage =15
                                                                    if g5_near == 1:
                                                                        if g5_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g5 "I don't know how I'm still eating!"
                                                                            $ g5_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g5_totalfullness <=6400 and g5_totalfullness > 6000:
                                                                        $ g5_fullstage =16
                                                                        if g5_near == 1:
                                                                            if g5_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g5 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                $ g5_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g5_totalfullness <=6800 and g5_totalfullness > 6400:
                                                                            $ g5_fullstage =17
                                                                            if g5_near == 1:
                                                                                if g5_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g5 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                    $ g5_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g5_totalfullness <=7200 and g5_totalfullness > 6800:
                                                                                $ g5_fullstage =18
                                                                                if g5_near == 1:
                                                                                    if g5_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g5 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                        $ g5_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g5_totalfullness <=7600 and g5_totalfullness > 7200:
                                                                                    $ g5_fullstage =19
                                                                                    if g5_near == 1:
                                                                                        if g5_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g5 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                            $ g5_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g5_totalfullness <=8000 and g5_totalfullness > 7600:
                                                                                        $ g5_fullstage =20
                                                                                        if g5_near == 1:
                                                                                            if g5_stretch20 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                g5 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                $ g5_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g5_totalfullness > 8000:
                                                                                            $ g5_fullstage =20
                                                                                            if g5_near == 1:
                                                                                                if g5_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g5_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g5_maxfulltext == 0:
                                                                                                        g5 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                    if g5_maxfulltext == 1:
                                                                                                        $ g5_burp = renpy.random.randint(0,1)
                                                                                                        if g5_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g5_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        g5 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g5_maxfulltext == 2:
                                                                                                        g5 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                    $ g5_stretch21 += 1
                                                                                            else:
                                                                                                pass
        return


    label g6girl:
        $ g6_fullnessoz = int(g6_fullness*0.034)
        $ g6_totalfullness = g6_fullness + g6_intfullness
        #if girl == "g6":
        if g6_totalfullness <= 400:
            $ g6_fullstage = 1
            if g6_near == 1 and g6_stage1 == 0:
                $ g6_stage1 = 1
                g6 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
        else:
            if g6_totalfullness <=800 and g6_totalfullness > 400:
                $ g6_fullstage =2
                if g6_near == 1 and g6_stage2 == 0:
                    $ g6_stage2 = 1
                    g6 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
            else:
                if g6_totalfullness <=1200 and g6_totalfullness > 800:
                    $ g6_fullstage =3
                    if g6_near == 1 and g6_stage3 == 0:
                        $ g6_stage3 = 1
                        g6 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                else:
                    if g6_totalfullness <=1600 and g6_totalfullness > 1200:
                        $ g6_fullstage =4
                        if g6_near == 1 and g6_stage4 == 0:
                            $ g6_stage4 = 1
                            g6 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                    else:
                        if g6_totalfullness <=2000 and g6_totalfullness > 1600:
                            $ g6_fullstage =5
                            if g6_near == 1 and g6_stage5 == 0:
                                $ g6_stage5 = 1
                                g6 "If you can keep feeding me like this, I might just make a new record!"
                        else:
                            if g6_totalfullness <=2400 and g6_totalfullness > 2000:
                                $ g6_fullstage =6
                                if g6_near == 1 and g6_stage6 == 0:
                                    $ g6_stage6 = 1
                                    g6 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                            else:
                                if g6_totalfullness <=2800 and g6_totalfullness > 2400:
                                    $ g6_fullstage =7
                                    if g6_near == 1 and g6_stage7 == 0:
                                        $ g6_stage7 = 1
                                        g6 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                else:
                                    if g6_totalfullness <=3200 and g6_totalfullness > 2800:
                                        $ g6_fullstage =8
                                        if g6_near == 1:
                                            if g6_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                g6 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                $ g6_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g6_totalfullness <=3600 and g6_totalfullness > 3200:
                                            $ g6_fullstage =9
                                            if g6_near == 1:
                                                if g6_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g6 "Did you hear that? I think that was my skin stretching"
                                                    $ g6_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g6_totalfullness <=4000 and g6_totalfullness > 3600:
                                                $ g6_fullstage =10
                                                if g6_near == 1:
                                                    if g6_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g6 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                        $ g6_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g6_totalfullness <=4400 and g6_totalfullness > 4000:
                                                    $ g6_fullstage =11
                                                    if g6_near == 1:
                                                        if g6_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g6 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                            $ g6_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g6_totalfullness <=4800 and g6_totalfullness > 4400:
                                                        $ g6_fullstage =12
                                                        if g6_near == 1:
                                                            if g6_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g6 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                $ g6_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g6_totalfullness <=5200 and g6_totalfullness > 4800:
                                                            $ g6_fullstage =13
                                                            if g6_near == 1:
                                                                if g6_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g6 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                    $ g6_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g6_totalfullness <=5600 and g6_totalfullness > 5200:
                                                                $ g6_fullstage =14
                                                                if g6_near == 1:
                                                                    if g6_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g6 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                        $ g6_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g6_totalfullness <=6000 and g6_totalfullness > 5600:
                                                                    $ g6_fullstage =15
                                                                    if g6_near == 1:
                                                                        if g6_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g6 "I don't know how I'm still eating!"
                                                                            $ g6_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g6_totalfullness <=6400 and g6_totalfullness > 6000:
                                                                        $ g6_fullstage =16
                                                                        if g6_near == 1:
                                                                            if g6_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g6 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                $ g6_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g6_totalfullness <=6800 and g6_totalfullness > 6400:
                                                                            $ g6_fullstage =17
                                                                            if g6_near == 1:
                                                                                if g6_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g6 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                    $ g6_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g6_totalfullness <=7200 and g6_totalfullness > 6800 and g6_nolimits == 1:
                                                                                $ g6_fullstage =18
                                                                                if g6_near == 1:
                                                                                    if g6_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g6 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                        $ g6_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g6_totalfullness <=7600 and g6_totalfullness > 7200 and g6_nolimits == 1:
                                                                                    $ g6_fullstage =19
                                                                                    if g6_near == 1:
                                                                                        if g6_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g6 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                            $ g6_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g6_totalfullness <=8000 and g6_totalfullness > 7600 and g6_nolimits == 1:
                                                                                        $ g6_fullstage =20
                                                                                        if g6_near == 1:
                                                                                            if g6_stretch20 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                g6 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                $ g6_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g6_totalfullness > 8000 and g6_nolimits == 1:
                                                                                            $ g6_fullstage =20
                                                                                            if g6_near == 1:
                                                                                                if g6_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g6_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g6_maxfulltext == 0:
                                                                                                        g6 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                    if g6_maxfulltext == 1:
                                                                                                        $ g6_burp = renpy.random.randint(0,1)
                                                                                                        if g6_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g6_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        g6 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g6_maxfulltext == 2:
                                                                                                        g6 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                    $ g6_stretch21 += 1
                                                                                            else:
                                                                                                pass
        return

label g7girl:
    $ g7_fullnessoz = int(g7_fullness*0.034)
    $ g7_totalfullness = g7_fullness + g7_intfullness
    #if girl == "g7":
    if g7_totalfullness <= 400:
        $ g7_fullstage = 1
        if g7_near == 1 and g7_stage1 == 0:
            $ g7_stage1 = 1
            g7 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
    else:
        if g7_totalfullness <=800 and g7_totalfullness > 400:
            $ g7_fullstage =2
            if g7_near == 1 and g7_stage2 == 0:
                $ g7_stage2 = 1
                g7 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
        else:
            if g7_totalfullness <=1200 and g7_totalfullness > 800:
                $ g7_fullstage =3
                if g7_near == 1 and g7_stage3 == 0:
                    $ g7_stage3 = 1
                    g7 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
            else:
                if g7_totalfullness <=1600 and g7_totalfullness > 1200:
                    $ g7_fullstage =4
                    if g7_near == 1 and g7_stage4 == 0:
                        $ g7_stage4 = 1
                        g7 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                else:
                    if g7_totalfullness <=2000 and g7_totalfullness > 1600:
                        $ g7_fullstage =5
                        if g7_near == 1 and g7_stage5 == 0:
                            $ g7_stage5 = 1
                            g7 "If you can keep feeding me like this, I might just make a new record!"
                    else:
                        if g7_totalfullness <=2400 and g7_totalfullness > 2000:
                            $ g7_fullstage =6
                            if g7_near == 1 and g7_stage6 == 0:
                                $ g7_stage6 = 1
                                g7 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                        else:
                            if g7_totalfullness <=2800 and g7_totalfullness > 2400:
                                $ g7_fullstage =7
                                if g7_near == 1 and g7_stage7 == 0:
                                    $ g7_stage7 = 1
                                    g7 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                            else:
                                if g7_totalfullness <=3200 and g7_totalfullness > 2800:
                                    $ g7_fullstage =8
                                    if g7_near == 1:
                                        if g7_stretch8 < 1:
                                            # play sound "audio/skinstreatching short.mp3"
                                            g7 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                            $ g7_stretch8 += 1
                                        else:
                                            pass
                                else:
                                    if g7_totalfullness <=3600 and g7_totalfullness > 3200:
                                        $ g7_fullstage =9
                                        if g7_near == 1:
                                            if g7_stretch9 < 1:
                                                play sound "audio/skinstreatching short.mp3"
                                                g7 "Did you hear that? I think that was my skin stretching"
                                                $ g7_stretch9 += 1
                                            else:
                                                pass
                                    else:
                                        if g7_totalfullness <=4000 and g7_totalfullness > 3600:
                                            $ g7_fullstage =10
                                            if g7_near == 1:
                                                if g7_stretch10 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g7 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                    $ g7_stretch10 += 1
                                                else:
                                                    pass
                                        else:
                                            if g7_totalfullness <=4400 and g7_totalfullness > 4000:
                                                $ g7_fullstage =11
                                                if g7_near == 1:
                                                    if g7_stretch11 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g7 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                        $ g7_stretch11 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g7_totalfullness <=4800 and g7_totalfullness > 4400:
                                                    $ g7_fullstage =12
                                                    if g7_near == 1:
                                                        if g7_stretch12 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g7 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                            $ g7_stretch12 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g7_totalfullness <=5200 and g7_totalfullness > 4800:
                                                        $ g7_fullstage =13
                                                        if g7_near == 1:
                                                            if g7_stretch13 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g7 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                $ g7_stretch13 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g7_totalfullness <=5600 and g7_totalfullness > 5200:
                                                            $ g7_fullstage =14
                                                            if g7_near == 1:
                                                                if g7_stretch14 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g7 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                    $ g7_stretch14 += 1
                                                                else:
                                                                    pass

                                                        else:
                                                            if g7_totalfullness <=6000 and g7_totalfullness > 5600:
                                                                $ g7_fullstage =15
                                                                if g7_near == 1:
                                                                    if g7_stretch15 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g7 "I don't know how I'm still eating!"
                                                                        $ g7_stretch15 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g7_totalfullness <=6400 and g7_totalfullness > 6000:
                                                                    $ g7_fullstage =16
                                                                    if g7_near == 1:
                                                                        if g7_stretch16 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g7 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                            $ g7_stretch16 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g7_totalfullness <=6800 and g7_totalfullness > 6400:
                                                                        $ g7_fullstage =17
                                                                        if g7_near == 1:
                                                                            if g7_stretch17 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g7 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                $ g7_stretch17 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g7_totalfullness <=7200 and g7_totalfullness > 6800:
                                                                            $ g7_fullstage =18
                                                                            if g7_near == 1:
                                                                                if g7_stretch18 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g7 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                    $ g7_stretch18 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g7_totalfullness <=7600 and g7_totalfullness > 7200:
                                                                                $ g7_fullstage =19
                                                                                if g7_near == 1:
                                                                                    if g7_stretch19 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g7 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                        $ g7_stretch19 += 1
                                                                                    else:
                                                                                        pass
                                                                            else:
                                                                                if g7_totalfullness <=8000 and g7_totalfullness > 7600:
                                                                                    $ g7_fullstage =20
                                                                                    if g7_near == 1:
                                                                                        if g7_stretch20 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g7 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                            $ g7_stretch20 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g7_totalfullness > 8000:
                                                                                        $ g7_fullstage =20
                                                                                        if g7_near == 1:
                                                                                            if g7_stretch21 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                $ g7_maxfulltext = renpy.random.randint(0,2)
                                                                                                if g7_maxfulltext == 0:
                                                                                                    g7 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                if g7_maxfulltext == 1:
                                                                                                    $ g7_burp = renpy.random.randint(0,1)
                                                                                                    if g7_burp == 0:
                                                                                                        play sound "audio/burp.mp3"
                                                                                                    if g7_burp == 1:
                                                                                                        play sound "audio/burp2.mp3"
                                                                                                    g7 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                if g7_maxfulltext == 2:
                                                                                                    g7 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                $ g7_stretch21 += 1
                                                                                        else:
                                                                                            pass
    return


    label g8girl:
        $ g8_fullnessoz = int(g8_fullness*0.034)
        $ g8_totalfullness = g8_fullness + g8_intfullness
        #if girl == "g8":
        if g8_totalfullness <= 400:
            $ g8_fullstage = 1
            if g8_near == 1 and g8_stage1 == 0:
                $ g8_stage1 = 1
                g8 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
        else:
            if g8_totalfullness <=800 and g8_totalfullness > 400:
                $ g8_fullstage =2
                if g8_near == 1 and g8_stage2 == 0:
                    $ g8_stage2 = 1
                    g8 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
            else:
                if g8_totalfullness <=1200 and g8_totalfullness > 800:
                    $ g8_fullstage =3
                    if g8_near == 1 and g8_stage3 == 0:
                        $ g8_stage3 = 1
                        g8 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                else:
                    if g8_totalfullness <=1600 and g8_totalfullness > 1200:
                        $ g8_fullstage =4
                        if g8_near == 1 and g8_stage4 == 0:
                            $ g8_stage4 = 1
                            g8 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                    else:
                        if g8_totalfullness <=2000 and g8_totalfullness > 1600:
                            $ g8_fullstage =5
                            if g8_near == 1 and g8_stage5 == 0:
                                $ g8_stage5 = 1
                                g8 "If you can keep feeding me like this, I might just make a new record!"
                        else:
                            if g8_totalfullness <=2400 and g8_totalfullness > 2000:
                                $ g8_fullstage =6
                                if g8_near == 1 and g8_stage6 == 0:
                                    $ g8_stage6 = 1
                                    g8 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                            else:
                                if g8_totalfullness <=2800 and g8_totalfullness > 2400:
                                    $ g8_fullstage =7
                                    if g8_near == 1 and g8_stage7 == 0:
                                        $ g8_stage7 = 1
                                        g8 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                else:
                                    if g8_totalfullness <=3200 and g8_totalfullness > 2800:
                                        $ g8_fullstage =8
                                        if g8_near == 1:
                                            if g8_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                g8 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                $ g8_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g8_totalfullness <=3600 and g8_totalfullness > 3200:
                                            $ g8_fullstage =9
                                            if g8_near == 1:
                                                if g8_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g8 "Did you hear that? I think that was my skin stretching"
                                                    $ g8_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g8_totalfullness <=4000 and g8_totalfullness > 3600:
                                                $ g8_fullstage =10
                                                if g8_near == 1:
                                                    if g8_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g8 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                        $ g8_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g8_totalfullness <=4400 and g8_totalfullness > 4000:
                                                    $ g8_fullstage =11
                                                    if g8_near == 1:
                                                        if g8_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g8 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                            $ g8_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g8_totalfullness <=4800 and g8_totalfullness > 4400:
                                                        $ g8_fullstage =12
                                                        if g8_near == 1:
                                                            if g8_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g8 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                $ g8_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g8_totalfullness <=5200 and g8_totalfullness > 4800:
                                                            $ g8_fullstage =13
                                                            if g8_near == 1:
                                                                if g8_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g8 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                    $ g8_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g8_totalfullness <=5600 and g8_totalfullness > 5200:
                                                                $ g8_fullstage =14
                                                                if g8_near == 1:
                                                                    if g8_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g8 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                        $ g8_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g8_totalfullness <=6000 and g8_totalfullness > 5600:
                                                                    $ g8_fullstage =15
                                                                    if g8_near == 1:
                                                                        if g8_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g8 "I don't know how I'm still eating!"
                                                                            $ g8_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g8_totalfullness <=6400 and g8_totalfullness > 6000:
                                                                        $ g8_fullstage =16
                                                                        if g8_near == 1:
                                                                            if g8_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g8 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                $ g8_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g8_totalfullness <=6800 and g8_totalfullness > 6400:
                                                                            $ g8_fullstage =17
                                                                            if g8_near == 1:
                                                                                if g8_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g8 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                    $ g8_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g8_totalfullness <=7200 and g8_totalfullness > 6800:
                                                                                $ g8_fullstage =18
                                                                                if g8_near == 1:
                                                                                    if g8_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g8 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                        $ g8_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g8_totalfullness <=7600 and g8_totalfullness > 7200:
                                                                                    $ g8_fullstage =19
                                                                                    if g8_near == 1:
                                                                                        if g8_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g8 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                            $ g8_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g8_totalfullness <=8000 and g8_totalfullness > 7600:
                                                                                        $ g8_fullstage =20
                                                                                        if g8_near == 1:
                                                                                            if g8_stretch20 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                g8 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                $ g8_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g8_totalfullness > 8000:
                                                                                            $ g8_fullstage =20
                                                                                            if g8_near == 1:
                                                                                                if g8_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g8_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g8_maxfulltext == 0:
                                                                                                        g8 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                    if g8_maxfulltext == 1:
                                                                                                        $ g8_burp = renpy.random.randint(0,1)
                                                                                                        if g8_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g8_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        g8 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g8_maxfulltext == 2:
                                                                                                        g8 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                    $ g8_stretch21 += 1
                                                                                            else:
                                                                                                pass
    return

    label g9girl:

        if g9_bellystage == 1:
            if g9_fullness == 0:
                $ g9_fullstage = 1
            else:

                if g9_fullness <= 200 and g9_fullness > 0:
                    $ g9_fullstage = 2
                else:
                    if g9_fullness <=400 and g9_fullness > 200:
                        $ g9_fullstage =3
                    else:
                        if g9_fullness <=800 and g9_fullness > 400:
                            $ g9_fullstage =4
                        else:
                            if g9_fullness <=1000 and g9_fullness > 800:
                                $ g9_fullstage =5
                            else:
                                if g9_fullness <=1200 and g9_fullness > 1000:
                                    $ g9_fullstage =6
                                else:
                                    if g9_fullness <=1400 and g9_fullness > 1200:
                                        $ g9_fullstage =7
                                    else:
                                        if g9_fullness <=1600 and g9_fullness > 1400:
                                            $ g9_fullstage =8
                                        else:
                                            if g9_fullness <=1800 and g9_fullness > 1600:
                                                $ g9_fullstage =9
                                            else:
                                                if g9_fullness <=2000 and g9_fullness > 1800:
                                                    $ g9_fullstage =10
                                                else:
                                                    if g9_fullness <=2200 and g9_fullness > 2000:
                                                        $ g9_fullstage =11
                                                    else:
                                                        if g9_fullness <=2400 and g9_fullness > 2200:
                                                            $ g9_fullstage =12
                                                        else:
                                                            if g9_fullness <=2600 and g9_fullness > 2400:
                                                                $ g9_fullstage =13
                                                            else:
                                                                if g9_fullness <=2800 and g9_fullness > 2600:
                                                                    $ g9_fullstage =14
                                                                else:
                                                                    if g9_fullness <=3000 and g9_fullness > 2800:
                                                                        $ g9_fullstage =15
                                                                    else:
                                                                        if g9_fullness <=3200 and g9_fullness > 3000:
                                                                            $ g9_fullstage =16
                                                                        else:
                                                                            if g9_fullness <=3400 and g9_fullness > 3200:
                                                                                $ g9_fullstage =17
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                            else:
                                                                                if g9_fullness <=3600 and g9_fullness > 3400:
                                                                                    $ g9_fullstage =18
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                else:
                                                                                    if g9_fullness <=3800 and g9_fullness > 3600:
                                                                                        $ g9_fullstage =19
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                    else:
                                                                                        if g9_fullness <=4000 and g9_fullness > 3800:
                                                                                            $ g9_fullstage =20
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                        else:
                                                                                            if g9_fullness >4000:
                                                                                                $ g9_fullstage =20
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                            else:
                                                                                                pass
        else:
            if g9_bellystage == 2:
                if g9_fullness == 0:
                    $ g9_fullstage = 1
                else:

                    if g9_fullness <= 300 and g9_fullness > 0:
                        $ g9_fullstage = 2
                    else:
                        if g9_fullness <=600 and g9_fullness > 300:
                            $ g9_fullstage =3
                        else:
                            if g9_fullness <=900 and g9_fullness > 600:
                                $ g9_fullstage =4
                            else:
                                if g9_fullness <=1200 and g9_fullness > 900:
                                    $ g9_fullstage =5
                                else:
                                    if g9_fullness <=1500 and g9_fullness > 1200:
                                        $ g9_fullstage =6
                                    else:
                                        if g9_fullness <=1800 and g9_fullness > 1500:
                                            $ g9_fullstage =7
                                        else:
                                            if g9_fullness <=2100 and g9_fullness > 1800:
                                                $ g9_fullstage =8
                                            else:
                                                if g9_fullness <=2400 and g9_fullness > 2100:
                                                    $ g9_fullstage =9
                                                else:
                                                    if g9_fullness <=2700 and g9_fullness > 2400:
                                                        $ g9_fullstage =10
                                                    else:
                                                        if g9_fullness <=3000 and g9_fullness > 2700:
                                                            $ g9_fullstage =11
                                                        else:
                                                            if g9_fullness <=3300 and g9_fullness > 3000:
                                                                $ g9_fullstage =12
                                                            else:
                                                                if g9_fullness <=3600 and g9_fullness > 3300:
                                                                    $ g9_fullstage =13
                                                                else:
                                                                    if g9_fullness <=3900 and g9_fullness > 3600:
                                                                        $ g9_fullstage =14
                                                                    else:
                                                                        if g9_fullness <=4200 and g9_fullness > 3900:
                                                                            $ g9_fullstage =15
                                                                        else:
                                                                            if g9_fullness <=4500 and g9_fullness > 4200:
                                                                                $ g9_fullstage =16
                                                                            else:
                                                                                if g9_fullness <=4800 and g9_fullness > 4500:
                                                                                    $ g9_fullstage =17
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                else:
                                                                                    if g9_fullness <=5100 and g9_fullness > 4800:
                                                                                        $ g9_fullstage =18
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                    else:
                                                                                        if g9_fullness <=5400 and g9_fullness > 5100:
                                                                                            $ g9_fullstage =19
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                        else:
                                                                                            if g9_fullness <=5700 and g9_fullness > 5400:
                                                                                                $ g9_fullstage =20
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                            else:
                                                                                                if g9_fullness >5700:
                                                                                                    $ g9_fullstage =20
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                else:
                                                                                                    pass
            else:
                if g9_bellystage == 3:
                    if g9_fullness == 0:
                        $ g9_fullstage = 1
                    else:

                        if g9_fullness <= 400 and g9_fullness > 0:
                            $ g9_fullstage = 2
                        else:
                            if g9_fullness <=800 and g9_fullness > 400:
                                $ g9_fullstage =3
                            else:
                                if g9_fullness <=1200 and g9_fullness > 800:
                                    $ g9_fullstage =4
                                else:
                                    if g9_fullness <=1600 and g9_fullness > 1200:
                                        $ g9_fullstage =5
                                    else:
                                        if g9_fullness <=2000 and g9_fullness > 1600:
                                            $ g9_fullstage =6
                                        else:
                                            if g9_fullness <=2400 and g9_fullness > 2000:
                                                $ g9_fullstage =7
                                            else:
                                                if g9_fullness <=2800 and g9_fullness > 2400:
                                                    $ g9_fullstage =8
                                                else:
                                                    if g9_fullness <=3200 and g9_fullness > 2800:
                                                        $ g9_fullstage =9
                                                    else:
                                                        if g9_fullness <=3600 and g9_fullness > 3200:
                                                            $ g9_fullstage =10
                                                        else:
                                                            if g9_fullness <=4000 and g9_fullness > 3600:
                                                                $ g9_fullstage =11
                                                            else:
                                                                if g9_fullness <=4400 and g9_fullness > 4000:
                                                                    $ g9_fullstage =12
                                                                else:
                                                                    if g9_fullness <=4800 and g9_fullness > 4400:
                                                                        $ g9_fullstage =13
                                                                    else:
                                                                        if g9_fullness <=5200 and g9_fullness > 4800:
                                                                            $ g9_fullstage =14
                                                                        else:
                                                                            if g9_fullness <=5600 and g9_fullness > 5200:
                                                                                $ g9_fullstage =15
                                                                            else:
                                                                                if g9_fullness <=6000 and g9_fullness > 5600:
                                                                                    $ g9_fullstage =16
                                                                                else:
                                                                                    if g9_fullness <=6400 and g9_fullness > 6000:
                                                                                        $ g9_fullstage =17
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                    else:
                                                                                        if g9_fullness <=6800 and g9_fullness > 6400:
                                                                                            $ g9_fullstage =18
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                        else:
                                                                                            if g9_fullness <=7200 and g9_fullness > 6800:
                                                                                                $ g9_fullstage =19
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                            else:
                                                                                                if g9_fullness <=7600 and g9_fullness > 7200:
                                                                                                    $ g9_fullstage =20
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                else:
                                                                                                    if g9_fullness >7600:
                                                                                                        $ g9_fullstage =20
                                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                                    else:
                                                                                                        pass
                else:
                    if g9_bellystage == 4:
                        if g9_fullness == 0:
                            $ g9_fullstage = 1
                        else:

                            if g9_fullness <= 500 and g9_fullness > 0:
                                $ g9_fullstage = 2
                            else:
                                if g9_fullness <=1000 and g9_fullness > 500:
                                    $ g9_fullstage =3
                                else:
                                    if g9_fullness <=1500 and g9_fullness > 1000:
                                        $ g9_fullstage =4
                                    else:
                                        if g9_fullness <=2000 and g9_fullness > 1500:
                                            $ g9_fullstage =5
                                        else:
                                            if g9_fullness <=2500 and g9_fullness > 2000:
                                                $ g9_fullstage =6
                                            else:
                                                if g9_fullness <=3000 and g9_fullness > 2500:
                                                    $ g9_fullstage =7
                                                else:
                                                    if g9_fullness <=3500 and g9_fullness > 3000:
                                                        $ g9_fullstage =8
                                                    else:
                                                        if g9_fullness <=4000 and g9_fullness > 3500:
                                                            $ g9_fullstage =9
                                                        else:
                                                            if g9_fullness <=4500 and g9_fullness > 4000:
                                                                $ g9_fullstage =10
                                                            else:
                                                                if g9_fullness <=5000 and g9_fullness > 4500:
                                                                    $ g9_fullstage =11
                                                                else:
                                                                    if g9_fullness <=5500 and g9_fullness > 5000:
                                                                        $ g9_fullstage =12
                                                                    else:
                                                                        if g9_fullness <=6000 and g9_fullness > 5500:
                                                                            $ g9_fullstage =13
                                                                        else:
                                                                            if g9_fullness <=6500 and g9_fullness > 6000:
                                                                                $ g9_fullstage =14
                                                                            else:
                                                                                if g9_fullness <=7000 and g9_fullness > 6500:
                                                                                    $ g9_fullstage =15
                                                                                else:
                                                                                    if g9_fullness <=7500 and g9_fullness > 7000:
                                                                                        $ g9_fullstage =16
                                                                                    else:
                                                                                        if g9_fullness <=8000 and g9_fullness > 7500:
                                                                                            $ g9_fullstage =17
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                        else:
                                                                                            if g9_fullness <=8500 and g9_fullness > 8000:
                                                                                                $ g9_fullstage =18
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                            else:
                                                                                                if g9_fullness <=9000 and g9_fullness > 8500:
                                                                                                    $ g9_fullstage =19
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                else:
                                                                                                    if g9_fullness <=9500 and g9_fullness > 9000:
                                                                                                        $ g9_fullstage =20
                                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                                    else:
                                                                                                        if g9_fullness >9500:
                                                                                                            $ g9_fullstage =20
                                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                                        else:
                                                                                                            pass

        label g10girl:
            #if girl == "g10":
            if g10_fullness <= 400:
                $ g10_fullstage = 1
            else:
                if g10_fullness <=800 and g10_fullness > 400:
                    $ g10_fullstage =2
                    k "Oh, I'm so greedy today!"
                else:
                    if g10_fullness <=1200 and g10_fullness > 800:
                        $ g10_fullstage =3
                        k "I'm growing for sure"
                    else:
                        if g10_fullness <=1600 and g10_fullness > 1200:
                            $ g10_fullstage =4
                            k "That's a serious belly for me!"
                        else:
                            if g10_fullness <=2000 and g10_fullness > 1600:
                                $ g10_fullstage =5
                                k "I'm expanding just like a rubber baloon!"
                            else:
                                if g10_fullness <=2400 and g10_fullness > 2000:
                                    $ g10_fullstage =6
                                    k "Wait, I can be bigger? Is there a limit to my growth?"
                                else:
                                    if g10_fullness <=2800 and g10_fullness > 2400:
                                        $ g10_fullstage =7
                                        k "Now this is how 7 months pregnant look, right?"
                                    else:
                                        if g10_fullness <=3200 and g10_fullness > 2800:
                                            $ g10_fullstage =8
                                            if stretch8 < 1 and g10_clothes == 1:
                                                play sound "audio/skinstreatching short.mp3"
                                                k "Now you can hear my skin is at the edge!"
                                                $ stretch8 += 1
                                            else:
                                                pass
                                        else:
                                            if g10_fullness <=3600 and g10_fullness > 3200:
                                                $ g10_fullstage =9
                                                if stretch9 < 1 and g10_clothes == 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    k "Oh, I can hardly breathe, talk and stand now. I need to stop, but can I be bigger?"
                                                    $ stretch9 += 1
                                                else:
                                                    pass
                                            else:
                                                if g10_fullness <=4000 and g10_fullness > 3600:
                                                    $ g10_fullstage =10
                                                    if stretch10 < 1 and g10_clothes == 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        k "Listen, this is the sound of stretchmarks forming. But I feel a little more capacity to grow"
                                                        $ stretch10 += 1
                                                    else:
                                                        pass
                                                else:
                                                    if g10_fullness > 4000:
                                                        $ g10_fullstage =10
                                                        if explode10 < 1:
                                                            $ explode10 = 1
                                                            k "Now ths is the exploding edge of my belly. So hard, so heavy. If anything more will get inside me I will explode!"
                                                        else:
                                                            pass

        label g11girl:
            $ g11_totalfullness = g11_fullness + g11_intfullness
            #if girl == "g11":
            if g11_totalfullness <= 400:
                $ g11_fullstage = 1
                if g11_near == 1 and g11_stage1 == 0:
                    $ g11_stage1 = 1
                    l "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
            else:
                if g11_totalfullness <=800 and g11_totalfullness > 400:
                    $ g11_fullstage =2
                    if g11_near == 1 and g11_stage2 == 0:
                        $ g11_stage2 = 1
                        l "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
                else:
                    if g11_totalfullness <=1200 and g11_totalfullness > 800:
                        $ g11_fullstage =3
                        if g11_near == 1 and g11_stage3 == 0:
                            $ g11_stage3 = 1
                            l "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                    else:
                        if g11_totalfullness <=1600 and g11_totalfullness > 1200:
                            $ g11_fullstage =4
                            if g11_near == 1 and g11_stage4 == 0:
                                $ g11_stage4 = 1
                                l "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                        else:
                            if g11_totalfullness <=2000 and g11_totalfullness > 1600:
                                $ g11_fullstage =5
                                if g11_near == 1 and g11_stage5 == 0:
                                    $ g11_stage5 = 1
                                    l "If you can keep feeding me like this, I might just make a new record!"
                            else:
                                if g11_totalfullness <=2400 and g11_totalfullness > 2000:
                                    $ g11_fullstage =6
                                    if g11_near == 1 and g11_stage6 == 0:
                                        $ g11_stage6 = 1
                                        l "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                                else:
                                    if g11_totalfullness <=2800 and g11_totalfullness > 2400:
                                        $ g11_fullstage =7
                                        if g11_near == 1 and g11_stage7 == 0:
                                            $ g11_stage7 = 1
                                            l "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                    else:
                                        if g11_totalfullness <=3200 and g11_totalfullness > 2800:
                                            $ g11_fullstage =8
                                            if g11_near == 1:
                                                if g11_stretch8 < 1:
                                                    # play sound "audio/skinstreatching short.mp3"
                                                    l "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                    $ g11_stretch8 += 1
                                                else:
                                                    pass
                                        else:
                                            if g11_totalfullness <=3600 and g11_totalfullness > 3200:
                                                $ g11_fullstage =9
                                                if g11_near == 1:
                                                    if g11_stretch9 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        l "Did you hear that? I think that was my skin stretching"
                                                        $ g11_stretch9 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g11_totalfullness <=4000 and g11_totalfullness > 3600:
                                                    $ g11_fullstage =10
                                                    if g11_near == 1:
                                                        if g11_stretch10 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            l "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                            $ g11_stretch10 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g11_totalfullness <=4400 and g11_totalfullness > 4000:
                                                        $ g11_fullstage =11
                                                        if g11_near == 1:
                                                            if g11_stretch11 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                l "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                                $ g11_stretch11 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g11_totalfullness <=4800 and g11_totalfullness > 4400:
                                                            $ g11_fullstage =12
                                                            if g11_near == 1:
                                                                if g11_stretch12 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    l "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                    $ g11_stretch12 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g11_totalfullness <=5200 and g11_totalfullness > 4800:
                                                                $ g11_fullstage =13
                                                                if g11_near == 1:
                                                                    if g11_stretch13 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        l "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                        $ g11_stretch13 += 1
                                                                    else:
                                                                        pass
                                                            else:
                                                                if g11_totalfullness <=5600 and g11_totalfullness > 5200:
                                                                    $ g11_fullstage =14
                                                                    if g11_near == 1:
                                                                        if g11_stretch14 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            l "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                            $ g11_stretch14 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g11_totalfullness <=6000 and g11_totalfullness > 5600:
                                                                        $ g11_fullstage =15
                                                                        if g11_near == 1:
                                                                            if g11_stretch15 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                l "I don't know how I'm still eating!"
                                                                                $ g11_stretch15 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g11_totalfullness <=6400 and g11_totalfullness > 6000:
                                                                            $ g11_fullstage =16
                                                                            if g11_near == 1:
                                                                                if g11_stretch16 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    l "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                    $ g11_stretch16 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g11_totalfullness <=6800 and g11_totalfullness > 6400:
                                                                                $ g11_fullstage =17
                                                                                if g11_near == 1:
                                                                                    if g11_stretch17 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        l "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                        $ g11_stretch17 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g11_totalfullness <=7200 and g11_totalfullness > 6800:
                                                                                    $ g11_fullstage =18
                                                                                    if g11_near == 1:
                                                                                        if g11_stretch18 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            l "Aren't you proud of how big and swollen with your food I've become?"
                                                                                            $ g11_stretch18 += 1
                                                                                        else:
                                                                                            pass

                                                                                else:
                                                                                    if g11_totalfullness <=7600 and g11_totalfullness > 7200:
                                                                                        $ g11_fullstage =19
                                                                                        if g11_near == 1:
                                                                                            if g11_stretch19 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                l "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                                $ g11_stretch19 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g11_totalfullness <=8000 and g11_totalfullness > 7600:
                                                                                            $ g11_fullstage =20
                                                                                            if g11_near == 1:
                                                                                                if g11_stretch20 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    l "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                    $ g11_stretch20 += 1
                                                                                                else:
                                                                                                    pass
                                                                                        else:
                                                                                            if g11_totalfullness > 8000:
                                                                                                $ g11_fullstage =20
                                                                                                if g11_near == 1:
                                                                                                    if g11_stretch21 < 1:
                                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                                        $ g11_maxfulltext = renpy.random.randint(0,2)
                                                                                                        if g11_maxfulltext == 0:
                                                                                                            l "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                        if g11_maxfulltext == 1:
                                                                                                            $ g11_burp = renpy.random.randint(0,1)
                                                                                                            if g11_burp == 0:
                                                                                                                play sound "audio/burp.mp3"
                                                                                                            if g11_burp == 1:
                                                                                                                play sound "audio/burp2.mp3"
                                                                                                            l "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                        if g11_maxfulltext == 2:
                                                                                                            l "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                        $ g11_stretch21 += 1
                                                                                                else:
                                                                                                    pass
    return

    label g11girldrunk:
        $ g11_totalfullness = g11_fullness + g11_intfullness
        #if girl == "g11":
        if g11_totalfullness <= 400:
            $ g11_fullstage = 1
            if g11_near == 1 and g11_stage1 == 0:
                $ g11_stage1 = 1
                l "Thanks for the drink"
        else:
            if g11_totalfullness <=800 and g11_totalfullness > 400:
                $ g11_fullstage =2
                if g11_near == 1 and g11_stage2 == 0:
                    $ g11_stage2 = 1
                    play sound "audio/hiccup.mp3"
                    l "Verry nice thankyou"
            else:
                if g11_totalfullness <=1200 and g11_totalfullness > 800:
                    $ g11_fullstage =3
                    if g11_near == 1 and g11_stage3 == 0:
                        $ g11_stage3 = 1
                        l "Ihave hiccups now!"
                else:
                    if g11_totalfullness <=1600 and g11_totalfullness > 1200:
                        $ g11_fullstage =4
                        if g11_near == 1 and g11_stage4 == 0:
                            $ g11_stage4 = 1
                            l "Sooo thenn honey brin' the nesst zzrings"
                    else:
                        if g11_totalfullness <=2000 and g11_totalfullness > 1600:
                            $ g11_fullstage =5
                            if g11_near == 1 and g11_stage5 == 0:
                                $ g11_stage5 = 1
                                play sound "audio/hiccup.mp3"
                                l "Ooh  iam genn sooo horrnny now"
                        else:
                            if g11_totalfullness <=2400 and g11_totalfullness > 2000:
                                $ g11_fullstage =6
                                if g11_near == 1 and g11_stage6 == 0:
                                    $ g11_stage6 = 1
                                    l "Ok won glazz more wonn hurd"
                            else:
                                if g11_totalfullness <=2800 and g11_totalfullness > 2400:
                                    $ g11_fullstage =7
                                    if g11_near == 1 and g11_stage7 == 0:
                                        $ g11_stage7 = 1
                                        l "D'you liyke my big zzrunken belly"
                                else:
                                    if g11_totalfullness <=3200 and g11_totalfullness > 2800:
                                        $ g11_fullstage =8
                                        if g11_near == 1:
                                            if g11_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                l "I'm genn preee big are'nn i? i kinna wanna stopp here, bud.  fer yoo, i wanna give it my alll"
                                                $ g11_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g11_totalfullness <=3600 and g11_totalfullness > 3200:
                                            $ g11_fullstage =9
                                            if g11_near == 1:
                                                if g11_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    l "Dizz you hear thad? i thing my belly wanns a rub"
                                                    $ g11_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g11_totalfullness <=4000 and g11_totalfullness > 3600:
                                                $ g11_fullstage =10
                                                if g11_near == 1:
                                                    if g11_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        l "Is thiss a boll orr yur dick thad liyke my belly?"
                                                        $ g11_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g11_totalfullness <=4400 and g11_totalfullness > 4000:
                                                    $ g11_fullstage =11
                                                    if g11_near == 1:
                                                        if g11_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            l "Whad arr yoo doin' sooo wiss me? iam the wx in yer hann"
                                                            $ g11_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g11_totalfullness <=4800 and g11_totalfullness > 4400:
                                                        $ g11_fullstage =12
                                                        if g11_near == 1:
                                                            if g11_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                l "More!? yoo wanna feed me more!? izz'nn thiss enough fer yoo? bud.  My ssomash duzzen feel any more full"
                                                                $ g11_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g11_totalfullness <=5200 and g11_totalfullness > 4800:
                                                            $ g11_fullstage =13
                                                            if g11_near == 1:
                                                                if g11_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    l "I doan nowe where iss alll goan anymore, bud my big fat belly is deffininnly ssill growin' fer yoo"
                                                                    $ g11_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g11_totalfullness <=5600 and g11_totalfullness > 5200:
                                                                $ g11_fullstage =14
                                                                if g11_near == 1:
                                                                    if g11_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        l "Thiss shunnn be, bud fer yoo, i'll doo anythin"
                                                                        play sound "audio/burp2.mp3"
                                                                        l "Includin' genn sooo zzzrunk ann sooo full thad i canned ssann upp"
                                                                        $ g11_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g11_totalfullness <=6000 and g11_totalfullness > 5600:
                                                                    $ g11_fullstage =15
                                                                    if g11_near == 1:
                                                                        if g11_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            l "I'm sooo big ann sloshin' wann yoo feel my big sexssy belly wiss yer hard cock?!"
                                                                            $ g11_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g11_totalfullness <=6400 and g11_totalfullness > 6000:
                                                                        $ g11_fullstage =16
                                                                        if g11_near == 1:
                                                                            if g11_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                l "d'you thing yoo c'n mayke a big barrel outa me?"
                                                                                menu:
                                                                                    "ifanswer yes":
                                                                                        "*Smiles* sooo thenn honey brin' the nesst zzrings"
                                                                                    "Naa":
                                                                                        pass

                                                                                $ g11_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g11_totalfullness <=6800 and g11_totalfullness > 6400:
                                                                            $ g11_fullstage =17
                                                                            if g11_near == 1:
                                                                                if g11_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    l "Thiss muzz be thad zzzrinkin' paradise i've hearnned 'bout, i keepdrinkin' ann zzzrinkin' ann zzzrinkin', bud genn everytime new zzrings sheers"
                                                                                    $ g11_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g11_totalfullness <=7200 and g11_totalfullness > 6800:
                                                                                $ g11_fullstage =18
                                                                                if g11_near == 1:
                                                                                    if g11_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        l "I wish i had more room fer zzrinin'"
                                                                                        $ g11_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g11_totalfullness <=7600 and g11_totalfullness > 7200:
                                                                                    $ g11_fullstage =19
                                                                                    if g11_near == 1:
                                                                                        if g11_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            l "Wow more ann yoo c'n roll me outa here"
                                                                                            $ g11_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g11_totalfullness <=8000 and g11_totalfullness > 7600:
                                                                                        $ g11_fullstage =20
                                                                                        if g11_near == 1:
                                                                                            if g11_stretch20 < 1:

                                                                                                play sound "audio/burp.mp3"
                                                                                                l "Uurpss fffuck my zzrunken braim oud"
                                                                                                $ g11_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g11_totalfullness > 8000:
                                                                                            $ g11_fullstage =20
                                                                                            if g11_near == 1:
                                                                                                if g11_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g11_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g11_maxfulltext == 0:
                                                                                                        l "Won more drob ann thiss barrell is killin' thiss sexssy girl"
                                                                                                    if g11_maxfulltext == 1:
                                                                                                        $ g11_burp = renpy.random.randint(0,1)
                                                                                                        if g11_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g11_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        l "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g11_maxfulltext == 2:
                                                                                                        play sound "audio/hiccup.mp3"
                                                                                                        l "Thad... thad... wuzza grade pardy (hiccups) i hope i c'n ged it home t' yer bed my bi(hiccup) honeybozz i am verry very zzzrunk now"
                                                                                                    $ g11_stretch21 += 1
                                                                                            else:
                                                                                                pass
                                                                                                return

label g12girl:
    $ g12_fullnessoz = int(g12_fullness*0.034)
    $ g12_totalfullness = g12_fullness + g12_intfullness
    #if girl == "g12":
    if g12_totalfullness <= 400:
        $ g12_fullstage = 1
        if g12_near == 1 and g12_stage1 == 0:
            $ g12_stage1 = 1
            g12 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
    else:
        if g12_totalfullness <=800 and g12_totalfullness > 400:
            $ g12_fullstage =2
            if g12_near == 1 and g12_stage2 == 0:
                $ g12_stage2 = 1
                g12 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
        else:
            if g12_totalfullness <=1200 and g12_totalfullness > 800:
                $ g12_fullstage =3
                if g12_near == 1 and g12_stage3 == 0:
                    $ g12_stage3 = 1
                    g12 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
            else:
                if g12_totalfullness <=1600 and g12_totalfullness > 1200:
                    $ g12_fullstage =4
                    if g12_near == 1 and g12_stage4 == 0:
                        $ g12_stage4 = 1
                        g12 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                else:
                    if g12_totalfullness <=2000 and g12_totalfullness > 1600:
                        $ g12_fullstage =5
                        if g12_near == 1 and g12_stage5 == 0:
                            $ g12_stage5 = 1
                            g12 "If you can keep feeding me like this, I might just make a new record!"
                    else:
                        if g12_totalfullness <=2400 and g12_totalfullness > 2000:
                            $ g12_fullstage =6
                            if g12_near == 1 and g12_stage6 == 0:
                                $ g12_stage6 = 1
                                g12 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                        else:
                            if g12_totalfullness <=2800 and g12_totalfullness > 2400:
                                $ g12_fullstage =7
                                if g12_near == 1 and g12_stage7 == 0:
                                    $ g12_stage7 = 1
                                    g12 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                            else:
                                if g12_totalfullness <=3200 and g12_totalfullness > 2800:
                                    $ g12_fullstage =8
                                    if g12_near == 1:
                                        if g12_stretch8 < 1:
                                            # play sound "audio/skinstreatching short.mp3"
                                            g12 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                            $ g12_stretch8 += 1
                                        else:
                                            pass
                                else:
                                    if g12_totalfullness <=3600 and g12_totalfullness > 3200:
                                        $ g12_fullstage =9
                                        if g12_near == 1:
                                            if g12_stretch9 < 1:
                                                play sound "audio/skinstreatching short.mp3"
                                                g12 "Did you hear that? I think that was my skin stretching"
                                                $ g12_stretch9 += 1
                                            else:
                                                pass
                                    else:
                                        if g12_totalfullness <=4000 and g12_totalfullness > 3600:
                                            $ g12_fullstage =10
                                            if g12_near == 1:
                                                if g12_stretch10 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g12 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                    $ g12_stretch10 += 1
                                                else:
                                                    pass
                                        else:
                                            if g12_totalfullness <=4400 and g12_totalfullness > 4000:
                                                $ g12_fullstage =11
                                                if g12_near == 1:
                                                    if g12_stretch11 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g12 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                        $ g12_stretch11 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g12_totalfullness <=4800 and g12_totalfullness > 4400:
                                                    $ g12_fullstage =12
                                                    if g12_near == 1:
                                                        if g12_stretch12 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g12 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                            $ g12_stretch12 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g12_totalfullness <=5200 and g12_totalfullness > 4800:
                                                        $ g12_fullstage =13
                                                        if g12_near == 1:
                                                            if g12_stretch13 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g12 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                $ g12_stretch13 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g12_totalfullness <=5600 and g12_totalfullness > 5200:
                                                            $ g12_fullstage =14
                                                            if g12_near == 1:
                                                                if g12_stretch14 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g12 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                    $ g12_stretch14 += 1
                                                                else:
                                                                    pass

                                                        else:
                                                            if g12_totalfullness <=6000 and g12_totalfullness > 5600:
                                                                $ g12_fullstage =15
                                                                if g12_near == 1:
                                                                    if g12_stretch15 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g12 "I don't know how I'm still eating!"
                                                                        $ g12_stretch15 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g12_totalfullness <=6400 and g12_totalfullness > 6000:
                                                                    $ g12_fullstage =16
                                                                    if g12_near == 1:
                                                                        if g12_stretch16 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g12 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                            $ g12_stretch16 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g12_totalfullness <=6800 and g12_totalfullness > 6400:
                                                                        $ g12_fullstage =17
                                                                        if g12_near == 1:
                                                                            if g12_stretch17 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g12 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                $ g12_stretch17 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g12_totalfullness <=7200 and g12_totalfullness > 6800 and g12_nolimits == 1:
                                                                            $ g12_fullstage =18
                                                                            if g12_near == 1:
                                                                                if g12_stretch18 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g12 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                    $ g12_stretch18 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g12_totalfullness <=7600 and g12_totalfullness > 7200 and g12_nolimits == 1:
                                                                                $ g12_fullstage =19
                                                                                if g12_near == 1:
                                                                                    if g12_stretch19 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g12 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                        $ g12_stretch19 += 1
                                                                                    else:
                                                                                        pass
                                                                            else:
                                                                                if g12_totalfullness <=8000 and g12_totalfullness > 7600 and g12_nolimits == 1:
                                                                                    $ g12_fullstage =20
                                                                                    if g12_near == 1:
                                                                                        if g12_stretch20 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g12 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                            $ g12_stretch20 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g12_totalfullness > 8000 and g12_nolimits == 1:
                                                                                        $ g12_fullstage =20
                                                                                        if g12_near == 1:
                                                                                            if g12_stretch21 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                $ g12_maxfulltext = renpy.random.randint(0,2)
                                                                                                if g12_maxfulltext == 0:
                                                                                                    g12 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                if g12_maxfulltext == 1:
                                                                                                    $ g12_burp = renpy.random.randint(0,1)
                                                                                                    if g12_burp == 0:
                                                                                                        play sound "audio/burp.mp3"
                                                                                                    if g12_burp == 1:
                                                                                                        play sound "audio/burp2.mp3"
                                                                                                    g12 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                if g12_maxfulltext == 2:
                                                                                                    g12 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                $ g12_stretch21 += 1
                                                                                        else:
                                                                                            pass
    return


    label g13girl:
        $ g13_fullnessoz = int(g13_fullness*0.034)
        $ g13_totalfullness = g13_fullness + g13_intfullness
        #if girl == "g13":
        if g13_totalfullness <= 400:
            $ g13_fullstage = 1
            if g13_near == 1 and g13_stage1 == 0:
                $ g13_stage1 = 1
                g13 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
        else:
            if g13_totalfullness <=800 and g13_totalfullness > 400:
                $ g13_fullstage =2
                if g13_near == 1 and g13_stage2 == 0:
                    $ g13_stage2 = 1
                    g13 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
            else:
                if g13_totalfullness <=1200 and g13_totalfullness > 800:
                    $ g13_fullstage =3
                    if g13_near == 1 and g13_stage3 == 0:
                        $ g13_stage3 = 1
                        g13 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                else:
                    if g13_totalfullness <=1600 and g13_totalfullness > 1200:
                        $ g13_fullstage =4
                        if g13_near == 1 and g13_stage4 == 0:
                            $ g13_stage4 = 1
                            g13 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                    else:
                        if g13_totalfullness <=2000 and g13_totalfullness > 1600:
                            $ g13_fullstage =5
                            if g13_near == 1 and g13_stage5 == 0:
                                $ g13_stage5 = 1
                                g13 "If you can keep feeding me like this, I might just make a new record!"
                        else:
                            if g13_totalfullness <=2400 and g13_totalfullness > 2000:
                                $ g13_fullstage =6
                                if g13_near == 1 and g13_stage6 == 0:
                                    $ g13_stage6 = 1
                                    g13 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                            else:
                                if g13_totalfullness <=2800 and g13_totalfullness > 2400:
                                    $ g13_fullstage =7
                                    if g13_near == 1 and g13_stage7 == 0:
                                        $ g13_stage7 = 1
                                        g13 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                else:
                                    if g13_totalfullness <=3200 and g13_totalfullness > 2800:
                                        $ g13_fullstage =8
                                        if g13_near == 1:
                                            if g13_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                g13 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                $ g13_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g13_totalfullness <=3600 and g13_totalfullness > 3200:
                                            $ g13_fullstage =9
                                            if g13_near == 1:
                                                if g13_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g13 "Did you hear that? I think that was my skin stretching"
                                                    $ g13_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g13_totalfullness <=4000 and g13_totalfullness > 3600:
                                                $ g13_fullstage =10
                                                if g13_near == 1:
                                                    if g13_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g13 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                        $ g13_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g13_totalfullness <=4400 and g13_totalfullness > 4000:
                                                    $ g13_fullstage =11
                                                    if g13_near == 1:
                                                        if g13_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g13 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                            $ g13_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g13_totalfullness <=4800 and g13_totalfullness > 4400:
                                                        $ g13_fullstage =12
                                                        if g13_near == 1:
                                                            if g13_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g13 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                $ g13_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g13_totalfullness <=5200 and g13_totalfullness > 4800:
                                                            $ g13_fullstage =13
                                                            if g13_near == 1:
                                                                if g13_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g13 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                    $ g13_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g13_totalfullness <=5600 and g13_totalfullness > 5200:
                                                                $ g13_fullstage =14
                                                                if g13_near == 1:
                                                                    if g13_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g13 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                        $ g13_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g13_totalfullness <=6000 and g13_totalfullness > 5600:
                                                                    $ g13_fullstage =15
                                                                    if g13_near == 1:
                                                                        if g13_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g13 "I don't know how I'm still eating!"
                                                                            $ g13_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g13_totalfullness <=6400 and g13_totalfullness > 6000:
                                                                        $ g13_fullstage =16
                                                                        if g13_near == 1:
                                                                            if g13_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g13 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                $ g13_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g13_totalfullness <=6800 and g13_totalfullness > 6400:
                                                                            $ g13_fullstage =17
                                                                            if g13_near == 1:
                                                                                if g13_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g13 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                    $ g13_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g13_totalfullness <=7200 and g13_totalfullness > 6800 and g13_nolimits == 1:
                                                                                $ g13_fullstage =18
                                                                                if g13_near == 1:
                                                                                    if g13_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g13 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                        $ g13_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g13_totalfullness <=7600 and g13_totalfullness > 7200 and g13_nolimits == 1:
                                                                                    $ g13_fullstage =19
                                                                                    if g13_near == 1:
                                                                                        if g13_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g13 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                            $ g13_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g13_totalfullness <=8000 and g13_totalfullness > 7600 and g13_nolimits == 1:
                                                                                        $ g13_fullstage =20
                                                                                        if g13_near == 1:
                                                                                            if g13_stretch20 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                g13 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                $ g13_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g13_totalfullness > 8000 and g13_nolimits == 1:
                                                                                            $ g13_fullstage =20
                                                                                            if g13_near == 1:
                                                                                                if g13_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g13_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g13_maxfulltext == 0:
                                                                                                        g13 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                    if g13_maxfulltext == 1:
                                                                                                        $ g13_burp = renpy.random.randint(0,1)
                                                                                                        if g13_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g13_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        g13 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g13_maxfulltext == 2:
                                                                                                        g13 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                    $ g13_stretch21 += 1
                                                                                            else:
                                                                                                pass
        return

    label g14girl:
        $ g14_fullnessoz = int(g14_fullness*0.034)
        $ g14_totalfullness = g14_fullness + g14_intfullness
        #if girl == "g14":
        if g14_totalfullness <= 400:
            $ g14_fullstage = 1
            if g14_near == 1 and g14_stage1 == 0:
                $ g14_stage1 = 1
                g14 "Look at how flat my belly is. Aren't you excited to see how much it will grow tonight?"
        else:
            if g14_totalfullness <=800 and g14_totalfullness > 400:
                $ g14_fullstage =2
                if g14_near == 1 and g14_stage2 == 0:
                    $ g14_stage2 = 1
                    g14 "Is that all? I thought you were going to engorge me beyond my wildest dreams. If you thought you were going to fill me up on that little morsel, think again"
            else:
                if g14_totalfullness <=1200 and g14_totalfullness > 800:
                    $ g14_fullstage =3
                    if g14_near == 1 and g14_stage3 == 0:
                        $ g14_stage3 = 1
                        g14 "Look at my little belly starting to grow. I have so much more room. Keep the food coming!"
                else:
                    if g14_totalfullness <=1600 and g14_totalfullness > 1200:
                        $ g14_fullstage =4
                        if g14_near == 1 and g14_stage4 == 0:
                            $ g14_stage4 = 1
                            g14 "Mmm, that last meal was good. My stomach's starting to fill up, but I need more"
                    else:
                        if g14_totalfullness <=2000 and g14_totalfullness > 1600:
                            $ g14_fullstage =5
                            if g14_near == 1 and g14_stage5 == 0:
                                $ g14_stage5 = 1
                                g14 "If you can keep feeding me like this, I might just make a new record!"
                        else:
                            if g14_totalfullness <=2400 and g14_totalfullness > 2000:
                                $ g14_fullstage =6
                                if g14_near == 1 and g14_stage6 == 0:
                                    $ g14_stage6 = 1
                                    g14 "Ok, wow. This is the most I've ever eaten in one sitting, but I'm feeling pretty good. Let's see how much more I can eat for you"
                            else:
                                if g14_totalfullness <=2800 and g14_totalfullness > 2400:
                                    $ g14_fullstage =7
                                    if g14_near == 1 and g14_stage7 == 0:
                                        $ g14_stage7 = 1
                                        g14 "My belly is starting to feel pretty tight, I don't know how much more of your food that I can take"
                                else:
                                    if g14_totalfullness <=3200 and g14_totalfullness > 2800:
                                        $ g14_fullstage =8
                                        if g14_near == 1:
                                            if g14_stretch8 < 1:
                                                # play sound "audio/skinstreatching short.mp3"
                                                g14 "I'm getting pretty big aren't I? I kinda want to stop here, but... for you, I want to give it my all"
                                                $ g14_stretch8 += 1
                                            else:
                                                pass
                                    else:
                                        if g14_totalfullness <=3600 and g14_totalfullness > 3200:
                                            $ g14_fullstage =9
                                            if g14_near == 1:
                                                if g14_stretch9 < 1:
                                                    play sound "audio/skinstreatching short.mp3"
                                                    g14 "Did you hear that? I think that was my skin stretching"
                                                    $ g14_stretch9 += 1
                                                else:
                                                    pass
                                        else:
                                            if g14_totalfullness <=4000 and g14_totalfullness > 3600:
                                                $ g14_fullstage =10
                                                if g14_near == 1:
                                                    if g14_stretch10 < 1:
                                                        play sound "audio/skinstreatching short.mp3"
                                                        g14 "I can't eat another bite! I can feel the food in the back of my throat, there's just no more room! ...Unless you force feed me."
                                                        $ g14_stretch10 += 1
                                                    else:
                                                        pass
                                            else:
                                                if g14_totalfullness <=4400 and g14_totalfullness > 4000:
                                                    $ g14_fullstage =11
                                                    if g14_near == 1:
                                                        if g14_stretch11 < 1:
                                                            play sound "audio/skinstreatching short.mp3"
                                                            g14 "...Whoa. This is it. My stomach literally cannot stretch anymore. I will never be able to outdo this. I'm so absolutely engorged I don't know if I can stand up. My belly is so huge and so incredibly tight I can barely breathe"
                                                            $ g14_stretch11 += 1
                                                        else:
                                                            pass
                                                else:
                                                    if g14_totalfullness <=4800 and g14_totalfullness > 4400:
                                                        $ g14_fullstage =12
                                                        if g14_near == 1:
                                                            if g14_stretch12 < 1:
                                                                play sound "audio/skinstreatching short.mp3"
                                                                g14 "More!? You want to feed me more!? Isn't this enough for you? But... My stomach doesn't feel any more full..."
                                                                $ g14_stretch12 += 1
                                                            else:
                                                                pass
                                                    else:
                                                        if g14_totalfullness <=5200 and g14_totalfullness > 4800:
                                                            $ g14_fullstage =13
                                                            if g14_near == 1:
                                                                if g14_stretch13 < 1:
                                                                    play sound "audio/skinstreatching short.mp3"
                                                                    g14 "I don't know where its all going anymore, but I'm not feeling any difference? My belly is definitely still growing"
                                                                    $ g14_stretch13 += 1
                                                                else:
                                                                    pass
                                                        else:
                                                            if g14_totalfullness <=5600 and g14_totalfullness > 5200:
                                                                $ g14_fullstage =14
                                                                if g14_near == 1:
                                                                    if g14_stretch14 < 1:
                                                                        play sound "audio/skinstreatching short.mp3"
                                                                        g14 "This shouldn't be humanly possible, but for you, I'll do anything. Including growing so full that I can't stand up"
                                                                        $ g14_stretch14 += 1
                                                                    else:
                                                                        pass

                                                            else:
                                                                if g14_totalfullness <=6000 and g14_totalfullness > 5600:
                                                                    $ g14_fullstage =15
                                                                    if g14_near == 1:
                                                                        if g14_stretch15 < 1:
                                                                            play sound "audio/skinstreatching short.mp3"
                                                                            g14 "I don't know how I'm still eating!"
                                                                            $ g14_stretch15 += 1
                                                                        else:
                                                                            pass

                                                                else:
                                                                    if g14_totalfullness <=6400 and g14_totalfullness > 6000:
                                                                        $ g14_fullstage =16
                                                                        if g14_near == 1:
                                                                            if g14_stretch16 < 1:
                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                g14 "I'm starting to think you might like seeing me grow like this don't you? Its more than just cooking right? *laughs*"
                                                                                $ g14_stretch16 += 1
                                                                            else:
                                                                                pass

                                                                    else:
                                                                        if g14_totalfullness <=6800 and g14_totalfullness > 6400:
                                                                            $ g14_fullstage =17
                                                                            if g14_near == 1:
                                                                                if g14_stretch17 < 1:
                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                    g14 "This must be that stuffing nirvana I've heard about, I keep eating, but don't seem to get any more full..."
                                                                                    $ g14_stretch17 += 1
                                                                                else:
                                                                                    pass

                                                                        else:
                                                                            if g14_totalfullness <=7200 and g14_totalfullness > 6800 and g14_nolimits == 1:
                                                                                $ g14_fullstage =18
                                                                                if g14_near == 1:
                                                                                    if g14_stretch18 < 1:
                                                                                        play sound "audio/skinstreatching short.mp3"
                                                                                        g14 "Aren't you proud of how big and swollen with your food I've become?"
                                                                                        $ g14_stretch18 += 1
                                                                                    else:
                                                                                        pass

                                                                            else:
                                                                                if g14_totalfullness <=7600 and g14_totalfullness > 7200 and g14_nolimits == 1:
                                                                                    $ g14_fullstage =19
                                                                                    if g14_near == 1:
                                                                                        if g14_stretch19 < 1:
                                                                                            play sound "audio/skinstreatching short.mp3"
                                                                                            g14 "You should really open up a restaurant. If your food could do this to me, you'll always sell out! You might actually be able to afford how much food you feed me"
                                                                                            $ g14_stretch19 += 1
                                                                                        else:
                                                                                            pass
                                                                                else:
                                                                                    if g14_totalfullness <=8000 and g14_totalfullness > 7600 and g14_nolimits == 1:
                                                                                        $ g14_fullstage =20
                                                                                        if g14_near == 1:
                                                                                            if g14_stretch20 < 1:
                                                                                                play sound "audio/skinstreatching short.mp3"
                                                                                                g14 "I have to be getting close to my limit, there's no way I can just keep expanding, r-right?"
                                                                                                $ g14_stretch20 += 1
                                                                                            else:
                                                                                                pass
                                                                                    else:
                                                                                        if g14_totalfullness > 8000 and g14_nolimits == 1:
                                                                                            $ g14_fullstage =20
                                                                                            if g14_near == 1:
                                                                                                if g14_stretch21 < 1:
                                                                                                    play sound "audio/skinstreatching short.mp3"
                                                                                                    $ g14_maxfulltext = renpy.random.randint(0,2)
                                                                                                    if g14_maxfulltext == 0:
                                                                                                        g14 "It's so hard to swallow anything anymore, it's all I can do to keep everything down, let alone force more inside me"
                                                                                                    if g14_maxfulltext == 1:
                                                                                                        $ g14_burp = renpy.random.randint(0,1)
                                                                                                        if g14_burp == 0:
                                                                                                            play sound "audio/burp.mp3"
                                                                                                        if g14_burp == 1:
                                                                                                            play sound "audio/burp2.mp3"
                                                                                                        g14 "U-uurp! Excuse me! There's just so much pressure inside my stomach, its hard to keep it all in"
                                                                                                    if g14_maxfulltext == 2:
                                                                                                        g14 "Enough! My skin is stretched so tight, it has no more give! There is no more room in my body for anything else! Anything else will have catastrophic consequences!!"
                                                                                                    $ g14_stretch21 += 1
                                                                                            else:
                                                                                                pass
        return


        label client1girl:

            #if girl == "client1":
            if client1_fullness <= 400:
                $ client1_fullstage = 1

            else:
                if client1_fullness <=800 and client1_fullness > 400:
                    $ client1_fullstage =2

                else:
                    if client1_fullness <=1200 and client1_fullness > 800:
                        $ client1_fullstage =3

                    else:
                        if client1_fullness <=1600 and client1_fullness > 1200:
                            $ client1_fullstage =4

                        else:
                            if client1_fullness <=2000 and client1_fullness > 1600:
                                $ client1_fullstage =5

                            else:
                                if client1_fullness <=2400 and client1_fullness > 2000:
                                    $ client1_fullstage =6

                                else:
                                    if client1_fullness <=2800 and client1_fullness > 2400:
                                        $ client1_fullstage =7

                                    else:
                                        if client1_fullness <=3200 and client1_fullness > 2800:
                                            $ client1_fullstage =8

                                        else:
                                            if client1_fullness <=3600 and client1_fullness > 3200:
                                                $ client1_fullstage =9

                                            else:
                                                if client1_fullness <=4000 and client1_fullness > 3600:
                                                    $ client1_fullstage =10

                                                else:
                                                    if client1_fullness <=4400 and client1_fullness > 4000:
                                                        $ client1_fullstage =11

                                                    else:
                                                        if client1_fullness <=4800 and client1_fullness > 4400:
                                                            $ client1_fullstage =12

                                                        else:
                                                            if client1_fullness <=5200 and client1_fullness > 4800:
                                                                $ client1_fullstage =13

                                                            else:
                                                                if client1_fullness <=5600 and client1_fullness > 5200:
                                                                    $ client1_fullstage =14

                                                                else:
                                                                    if client1_fullness <=6000 and client1_fullness > 5600:
                                                                        $ client1_fullstage =15

                                                                    else:
                                                                        if client1_fullness <=6400 and client1_fullness > 6000:
                                                                            $ client1_fullstage =16

                                                                        else:
                                                                            if client1_fullness <=6800 and client1_fullness > 6400:
                                                                                $ client1_fullstage =17

                                                                            else:
                                                                                if client1_fullness <=7200 and client1_fullness > 6800:
                                                                                    $ client1_fullstage =18

                                                                                else:
                                                                                    if client1_fullness <=7600 and client1_fullness > 7200:
                                                                                        $ client1_fullstage =19

                                                                                    else:
                                                                                        if client1_fullness <=8000 and client1_fullness > 7600:
                                                                                            $ client1_fullstage =20

                                                                                        else:
                                                                                            if client1_fullness > 8000:
                                                                                                $ client1_fullstage =20

                                                                                            else:
                                                                                                pass


        label client2girl:

            #if girl == "client2":
            if client2_fullness <= 400:
                $ client2_fullstage = 1

            else:
                if client2_fullness <=800 and client2_fullness > 400:
                    $ client2_fullstage =2

                else:
                    if client2_fullness <=1200 and client2_fullness > 800:
                        $ client2_fullstage =3

                    else:
                        if client2_fullness <=1600 and client2_fullness > 1200:
                            $ client2_fullstage =4

                        else:
                            if client2_fullness <=2000 and client2_fullness > 1600:
                                $ client2_fullstage =5

                            else:
                                if client2_fullness <=2400 and client2_fullness > 2000:
                                    $ client2_fullstage =6

                                else:
                                    if client2_fullness <=2800 and client2_fullness > 2400:
                                        $ client2_fullstage =7

                                    else:
                                        if client2_fullness <=3200 and client2_fullness > 2800:
                                            $ client2_fullstage =8

                                        else:
                                            if client2_fullness <=3600 and client2_fullness > 3200:
                                                $ client2_fullstage =9

                                            else:
                                                if client2_fullness <=4000 and client2_fullness > 3600:
                                                    $ client2_fullstage =10

                                                else:
                                                    if client2_fullness <=4400 and client2_fullness > 4000:
                                                        $ client2_fullstage =11

                                                    else:
                                                        if client2_fullness <=4800 and client2_fullness > 4400:
                                                            $ client2_fullstage =12

                                                        else:
                                                            if client2_fullness <=5200 and client2_fullness > 4800:
                                                                $ client2_fullstage =13

                                                            else:
                                                                if client2_fullness <=5600 and client2_fullness > 5200:
                                                                    $ client2_fullstage =14

                                                                else:
                                                                    if client2_fullness <=6000 and client2_fullness > 5600:
                                                                        $ client2_fullstage =15

                                                                    else:
                                                                        if client2_fullness <=6400 and client2_fullness > 6000:
                                                                            $ client2_fullstage =16

                                                                        else:
                                                                            if client2_fullness <=6800 and client2_fullness > 6400:
                                                                                $ client2_fullstage =17

                                                                            else:
                                                                                if client2_fullness <=7200 and client2_fullness > 6800:
                                                                                    $ client2_fullstage =18

                                                                                else:
                                                                                    if client2_fullness <=7600 and client2_fullness > 7200:
                                                                                        $ client2_fullstage =19

                                                                                    else:
                                                                                        if client2_fullness <=8000 and client2_fullness > 7600:
                                                                                            $ client2_fullstage =20

                                                                                        else:
                                                                                            if client2_fullness > 8000:
                                                                                                $ client2_fullstage =20

                                                                                            else:
                                                                                                pass

        label client3girl:

            #if girl == "client3":
            if client3_fullness <= 400:
                $ client3_fullstage = 1

            else:
                if client3_fullness <=800 and client3_fullness > 400:
                    $ client3_fullstage =2

                else:
                    if client3_fullness <=1200 and client3_fullness > 800:
                        $ client3_fullstage =3

                    else:
                        if client3_fullness <=1600 and client3_fullness > 1200:
                            $ client3_fullstage =4

                        else:
                            if client3_fullness <=2000 and client3_fullness > 1600:
                                $ client3_fullstage =5

                            else:
                                if client3_fullness <=2400 and client3_fullness > 2000:
                                    $ client3_fullstage =6

                                else:
                                    if client3_fullness <=2800 and client3_fullness > 2400:
                                        $ client3_fullstage =7

                                    else:
                                        if client3_fullness <=3200 and client3_fullness > 2800:
                                            $ client3_fullstage =8

                                        else:
                                            if client3_fullness <=3600 and client3_fullness > 3200:
                                                $ client3_fullstage =9

                                            else:
                                                if client3_fullness <=4000 and client3_fullness > 3600:
                                                    $ client3_fullstage =10

                                                else:
                                                    if client3_fullness <=4400 and client3_fullness > 4000:
                                                        $ client3_fullstage =11

                                                    else:
                                                        if client3_fullness <=4800 and client3_fullness > 4400:
                                                            $ client3_fullstage =12

                                                        else:
                                                            if client3_fullness <=5200 and client3_fullness > 4800:
                                                                $ client3_fullstage =13

                                                            else:
                                                                if client3_fullness <=5600 and client3_fullness > 5200:
                                                                    $ client3_fullstage =14

                                                                else:
                                                                    if client3_fullness <=6000 and client3_fullness > 5600:
                                                                        $ client3_fullstage =15

                                                                    else:
                                                                        if client3_fullness <=6400 and client3_fullness > 6000:
                                                                            $ client3_fullstage =16

                                                                        else:
                                                                            if client3_fullness <=6800 and client3_fullness > 6400:
                                                                                $ client3_fullstage =17

                                                                            else:
                                                                                if client3_fullness <=7200 and client3_fullness > 6800:
                                                                                    $ client3_fullstage =18

                                                                                else:
                                                                                    if client3_fullness <=7600 and client3_fullness > 7200:
                                                                                        $ client3_fullstage =19

                                                                                    else:
                                                                                        if client3_fullness <=8000 and client3_fullness > 7600:
                                                                                            $ client3_fullstage =20

                                                                                        else:
                                                                                            if client3_fullness > 8000:
                                                                                                $ client3_fullstage =20

                                                                                            else:
                                                                                                pass

        label client4girl:

            #if girl == "client4":
            if client4_fullness <= 400:
                $ client4_fullstage = 1

            else:
                if client4_fullness <=800 and client4_fullness > 400:
                    $ client4_fullstage =2

                else:
                    if client4_fullness <=1200 and client4_fullness > 800:
                        $ client4_fullstage =3

                    else:
                        if client4_fullness <=1600 and client4_fullness > 1200:
                            $ client4_fullstage =4

                        else:
                            if client4_fullness <=2000 and client4_fullness > 1600:
                                $ client4_fullstage =5

                            else:
                                if client4_fullness <=2400 and client4_fullness > 2000:
                                    $ client4_fullstage =6

                                else:
                                    if client4_fullness <=2800 and client4_fullness > 2400:
                                        $ client4_fullstage =7

                                    else:
                                        if client4_fullness <=3200 and client4_fullness > 2800:
                                            $ client4_fullstage =8

                                        else:
                                            if client4_fullness <=3600 and client4_fullness > 3200:
                                                $ client4_fullstage =9

                                            else:
                                                if client4_fullness <=4000 and client4_fullness > 3600:
                                                    $ client4_fullstage =10

                                                else:
                                                    if client4_fullness <=4400 and client4_fullness > 4000:
                                                        $ client4_fullstage =11

                                                    else:
                                                        if client4_fullness <=4800 and client4_fullness > 4400:
                                                            $ client4_fullstage =12

                                                        else:
                                                            if client4_fullness <=5200 and client4_fullness > 4800:
                                                                $ client4_fullstage =13

                                                            else:
                                                                if client4_fullness <=5600 and client4_fullness > 5200:
                                                                    $ client4_fullstage =14

                                                                else:
                                                                    if client4_fullness <=6000 and client4_fullness > 5600:
                                                                        $ client4_fullstage =15

                                                                    else:
                                                                        if client4_fullness <=6400 and client4_fullness > 6000:
                                                                            $ client4_fullstage =16

                                                                        else:
                                                                            if client4_fullness <=6800 and client4_fullness > 6400:
                                                                                $ client4_fullstage =17

                                                                            else:
                                                                                if client4_fullness <=7200 and client4_fullness > 6800:
                                                                                    $ client4_fullstage =18

                                                                                else:
                                                                                    if client4_fullness <=7600 and client4_fullness > 7200:
                                                                                        $ client4_fullstage =19

                                                                                    else:
                                                                                        if client4_fullness <=8000 and client4_fullness > 7600:
                                                                                            $ client4_fullstage =20

                                                                                        else:
                                                                                            if client4_fullness > 8000:
                                                                                                $ client4_fullstage =20

                                                                                            else:
                                                                                                pass


    label g12weight:
        if weightgain > 0:
            $ g12_weight = int(g12_defaultweight + (g12_calories/7000))
            if g12_weight <= 53:
                $ g12_weightstage = 1
            else:
                if g12_weight <= 56 and g12_weight > 53:
                    $ g12_weightstage = 2
                    $ g12_gainquestion = 1
                else:
                    if g12_weight <= 62 and g12_weight > 59:
                        $ g12_weightstage = 3
                        $ g12_gainquestion = 1
                    else:
                        if g12_weight <= 65 and g12_weight > 62:
                            $ g12_weightstage = 4
                            $ g12_gainquestion = 1
                        else:
                            if g12_weight <= 68 and g12_weight > 65:
                                $ g12_weightstage = 5
                                $ g12_gainquestion = 1
                            else:
                                if g12_weight <= 71 and g12_weight > 68:
                                    $ g12_weightstage = 6
                                    $ g12_gainquestion = 1
                                else:
                                    if g12_weight >71:
                                        $ g12_weightstage = 6
        else:
            $ g12_weightstage = 1

return
