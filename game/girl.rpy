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


    