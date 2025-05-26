label hayooncantresisttowatch:

    
    $ myrandom = renpy.random.randint(1,13-hayoon_fullstage)
    if myrandom == 1:
        $ position = "barhayoonbellyview"
        call sceneimg
        if hayoon_fullstage == 1:
            # should be something, well, nothing interesting here, just boring flat belly
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... Flat as a board—guess everyone's gotta start somewhere."
            if myrandom == 2:
                "inner monologue... Nothing exciting going on... yet. But I’ve got my eye on it."
            if myrandom == 3:
                "inner monologue... Just the calm before the storm, right? Right?"

        if hayoon_fullstage == 2:
            # well, player can notice a little bit of something in her belly
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... Is that a tiny bulge? Someone's been snacking, hmm?"
            if myrandom == 2:
                "inner monologue... Oh-ho, what’s this little curve trying to be?"
            if myrandom == 3:
                "inner monologue... She’s hiding something under that outfit… and I like where this is going."

        if hayoon_fullstage == 3:
            # well, she may have eaten something at least
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... That’s more like it! Somebody had a big lunch, didn’t she?"
            if myrandom == 2:
                "inner monologue... That little swell is becoming a statement piece."
            if myrandom == 3:
                "inner monologue... I could swear she’s fuller than yesterday… someone’s enjoying herself."

        if hayoon_fullstage == 4:
            # this looks fine already, good view
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... Okay, wow. That’s a belly worth admiring."
            if myrandom == 2:
                "inner monologue... She’s really filling out—like, deliciously so."
            if myrandom == 3:
                "inner monologue... That curve should come with a warning label. It’s dangerously distracting."

        if hayoon_fullstage == 5:
            # this is more than something, I want to look at it permanently, but I need to look at her eyes
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... I want to stare forever—but she’ll totally catch me. Eyes up!"
            if myrandom == 2:
                "inner monologue... That belly is practically hypnotic. Stay cool. Look normal!"
            if myrandom == 3:
                "inner monologue... If this keeps up, I might need sunglasses just to keep my gaze in check."

        if hayoon_fullstage == 6:
            # this is impossible to resist! She is so huge! keep yourself in hands, talk to her as if you are normal person!
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... She’s huge. Gloriously, jaw-droppingly huge. Just… act natural!"
            if myrandom == 2:
                "inner monologue... I’m pretty sure gravity’s orbiting her belly right now."
            if myrandom == 3:
                "inner monologue... Don’t drool. Don’t freeze. Just pretend this is totally normal. Yep. Totally."
        
        if hayoon_fullstage == 7:
            # she’s getting enormous—past full, into unbelievable territory
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... That belly could have its own passport. This is beyond anything I imagined."
            if myrandom == 2:
                "inner monologue... I think she’s bigger than the booth. How is she even standing like that?"
            if myrandom == 3:
                "inner monologue... Okay, this is cartoon-level roundness. I might actually be blushing."

        if hayoon_fullstage == 8:
            # she’s borderline surreal now, a spectacle of fullness
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... Is it possible to fall for a belly? Because I think I just did."
            if myrandom == 2:
                "inner monologue... I could bounce a coin off that dome. And maybe lose it in the curve."
            if myrandom == 3:
                "inner monologue... She's like a goddess of indulgence—and I'm just her stunned follower."

        if hayoon_fullstage == 9:
            # we're in legendary territory; awe and disbelief collide
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... If she turns too fast, I think the room might tilt."
            if myrandom == 2:
                "inner monologue... This is the stuff of myths—ancient scrolls would have written about her belly."
            if myrandom == 3:
                "inner monologue... I don’t know whether to stare, bow, or build a monument in its honor."

        if hayoon_fullstage == 10:
            # sheer overwhelming fullness; words struggle to keep up with what you're seeing
            $ myrandom = renpy.random.randint(1,3)
            if myrandom == 1:
                "inner monologue... Her belly has reached critical mass. I’m not sure physics was ready for this."
            if myrandom == 2:
                "inner monologue... Is this even real? She’s like a walking planet—and I’m hopelessly in orbit."
            if myrandom == 3:
                "inner monologue... This isn't a belly anymore. This is an event. A phenomenon. A miracle in motion."

    else:
        # player resisted to watch
        pass

return
