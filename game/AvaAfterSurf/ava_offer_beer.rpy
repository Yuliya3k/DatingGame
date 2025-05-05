##############################################################################
#  Ava – offer beer (expanded with extra dialogue & randomness)
##############################################################################

label ava_offer_beer:

    #---------------------------------------------------------------------#
    #   0) Too little attitude → instant decline
    #---------------------------------------------------------------------#
    if ava_attitude < 20:
        $ position = "avaaftersurfinglisteningclose"
        call sceneimg
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            Ava "Mm-hmm, thanks… but I’m still technically on guard duty. Better not."
        elif myrandom == 2:
            Ava "Appreciate it, but I’ve got to keep a clear head just in case."
        else:
            Ava "Tempting, but rules are rules. Rain-check?"
        return


    #---------------------------------------------------------------------#
    #   1) She’s already stuffed (attitude 20-50, stage ≥5)
    #---------------------------------------------------------------------#
    if 20 <= ava_attitude <= 50 and ava_fullstage >= 5:
        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            Ava "Uff… I’m sloshing already.  Mind if we hit pause?"
        elif myrandom == 2:
            Ava "One more gulp and I’ll need a tow-line!"
        else:
            Ava "Think I’ve reached critical mass – gonna sit this round out."

        menu:
            "Give her a friendly nod":
                
                $ reputationchange = 3
                $ nigirlimage = "niava"
                call reputationchange
                player "Totally get it—let’s just chill and watch the waves."
                $ position = "avaaftersurfinglisteningclose"
                call sceneimg
                Ava "Thanks, appreciate the breather."
                return

            "Press her anyway":
                $ reputationchange = -3
                $ nigirlimage = "niava"
                call reputationchange
                
                player "Ah, come on—half a bottle won’t sink you!"
                $ position = "avaaftersurfinglisteningclose"
                call sceneimg
                Ava "I said no, hero.  Push again and you’re body-boarding without the board."
                return

            "Crack a joke and back off (no change)":
                player "Fair enough—mother ocean says time-out."
                return



    #---------------------------------------------------------------------#
    #   2) Maxed out even for high attitude (stage ≥10)
    #---------------------------------------------------------------------#
    if ava_attitude > 50 and ava_fullstage == 10:
        $ position = "avaaftersurfingtalkingclose"
        call sceneimg
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            play audio "audio/burpsinglesilent.mp3"
            Ava "*tiny burp*  I’m at capacity, captain."
        elif myrandom == 2:
            Ava "If I tilt another bottle I’ll roll back into the surf."
        else:
            Ava "Let’s not test Newton’s laws on my stomach, okay?"
        $ position = "avastandsbellylook"
        call sceneimg    
        $ view = renpy.random.randint(1,10)

        if view == 1:
            "Wow… that belly’s bigger than I imagined beer could manage."
        elif view == 2:
            "Her bikini strings are working overtime right now."
        elif view == 3:
            "That curve is almost perfectly round."
        elif view == 4:
            "I can see the skin tighten with every breath."
        elif view == 5:
            "She shifts and I hear the liquid slosh inside."
        elif view == 6:
            "She honestly looks like she swallowed a beach ball."
        elif view == 7:
            "One gentle poke would probably set it wobbling for ages."
        elif view == 8:
            "Hard to believe all of that is just beer."
        elif view == 9:
            "The late sun makes that dome shine like polished bronze."
        else:
            "Better not mention seconds—she’s clearly past that point."
        
        return


    #---------------------------------------------------------------------#
    #   3) She accepts the beer
    #---------------------------------------------------------------------#
    $ position = "avastandsthirstyside"
    call sceneimg
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        Ava "Oh yes, please – my throat’s dryer than beach sand."
    elif myrandom == 2:
        Ava "Thought you’d never ask. Hand it over!"
    else:
        Ava "Beer me – lifesaver’s privilege."

    # --- sip SFX (random of 3) ------------------------------------------
    $ position = "avaaftersurfingdrinkingclose"
    call sceneimg
    $ fullnesschange = 330
    $ nigirlimage = "niava"
    call fullnesschange
    pause 0.7
    $ calorieschange = 183
    $ nigirlimage = "niava"
    call calorieschange
    
    $ myrandom = renpy.random.randint(1,3)
    if myrandom == 1:
        play sound "audio/beersipfromthebottle1.mp3"
    elif myrandom == 2:
        play sound "audio/beersipfromthebottle2.mp3"
    else:
        play sound "audio/beersipfromthebottle3.mp3"

    "Ava tips the bottle back, golden liquid catching the sunlight."

    # --- stat changes ----------------------------------------------------
    $ ava_fullstage += 1
    $ calendar.AddMinutes(5)
    if ava_attitude < 50:
        $ ava_attitude += 2
    else:
        $ ava_attitude += 1


    #---------------------------------------------------------------------#
    #   4) Short reaction lines – now 3 variants for each fullness tier
    #---------------------------------------------------------------------#
    $ myrandom = renpy.random.randint(1,3)

    if ava_fullstage == 1:
        $ position = "avastandsbellylook"
        call sceneimg
        if myrandom == 1:
            Ava "That hits the spot."
        elif myrandom == 2:
            Ava "Ahh… liquid sunshine."
        else:
            Ava "Perfect post-surf reward."
    elif ava_fullstage <= 3:
        if myrandom == 1:
            Ava "You know, beer tastes saltier when the ocean’s still in your hair."
        elif myrandom == 2:
            Ava "Can you hear the waves applauding our choices?"
        else:
            Ava "Beach, brew, and a breeze – triple-B perfection."
    elif ava_fullstage == 5:
        if myrandom == 1:
            Ava "*rubs belly*  Whoa, surge warning in my midsection."
        elif myrandom == 2:
            Ava "Starting to feel like a water balloon."
        else:
            Ava "Next wave I ride might be inside me."
    elif ava_fullstage >= 8:
        if myrandom == 1:
            Ava "If I lie on my back I’ll probably drift out to sea."
        elif myrandom == 2:
            Ava "Note to self: petition for beer-proof rescue tubes."
        else:
            Ava "*giggles* I’m basically a human keg now."

    return
