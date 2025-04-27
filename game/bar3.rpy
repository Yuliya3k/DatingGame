label bar3:
    call closescreens
    $ calendar.AddMinutes(20)
    $ myrandom = renpy.random.randint(1,5)

    if myrandom == 3 and hayoonintro == 1:
        $ hayoonatthebar = 1


    play music "audio/bar.mp3" volume 0.3

    if hayoonatthebar == 1:
        $ hayoon_fullness = renpy.random.randint(1,2000)
        $ position = "kirahayoonenter"
        call sceneimg
        player "I walk into the bar, greeted by the warm hum of chatter and clinking glasses."
        $ position = "kiraquestion2"
        call sceneimg
        Kira "Hey there! The usual tonight?"
    else:        
        $ position = "kiraenterance"
        call sceneimg
        player "I walk into the bar, greeted by the warm hum of chatter and clinking glasses."
        $ position = "kiraquestion2"
        call sceneimg
        Kira "Hey there! The usual tonight?"
    if hayoonatthebar == 1 and hayoonfirstmeet == 0:
        $ position = "kiraexplain"
        call sceneimg
        $  hayoonfirstmeet = 1
        $ myrandom = renpy.random.randint(1,3)
        if myrandom == 1:
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "Hey, remember when I mentioned HaYoon, the town's doctor?"
            $ position = "kiraquestion"
            call sceneimg
            player "Yeah, I remember. What about her?"
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "Well, look who just walked in. She's sitting at the bar, a few stools down from you."
            $ position = "kiraquestion"
            call sceneimg
            player "Oh, I see her. She's alone?"
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "Yeah, she often comes here to unwind after a long day at the clinic. She's a great person, and you might find her company enjoyable."
            $ position = "kiraquestion"
            call sceneimg
            player "That sounds interesting. Do you think you could introduce us?"
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "Of course! Just give me a moment to wrap up some orders, and I'll make the introduction."  
            $ position = "kiraworking2"
            call sceneimg
            pause
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "Alright, it's time. Let's go meet HaYoon."
            $ position = "kiraleaningtohayoon"
            call sceneimg
            Kira "Hey, HaYoon! Mind if I introduce you to someone?"
            $ position = "barhayoonhey"
            call sceneimg
            HaYoon "Kira, always a pleasure. Introduce away!"
            $ position = "kiraleaningtohayoon"
            call sceneimg
            Kira "HaYoon, this is, our newest resident in town. Meet HaYoon, our amazing doctor."
            $ position = "barhayoonwhat"
            call sceneimg
            player "Nice to meet you, HaYoon."
            $ position = "barhayoonexplaining"
            call sceneimg
            HaYoon "Likewise. Welcome to our town. Kira has been singing your praises."
            $ position = "barhayoonwhat"
            call sceneimg
            player "Well, Kira has been a wonderful guide so far. I am looking forward to getting to know more people in town."
            $ position = "barhayoonexplaining"
            call sceneimg
            HaYoon "Then, here is to new beginnings and new friendships. Cheers!"

        



        if myrandom == 2:
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "Hey, see that woman at the bar? That's HaYoon, the doctor I mentioned to you before."
            $ position = "kiraquestion"
            call sceneimg
            player "Yeah, you told me about her. She's the town's doctor, right?"
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "That's her. She's a regular here after her long shifts at the clinic. If you're interested, I can introduce you two. She's really friendly and great to chat with."
            $ position = "kiraquestion"
            call sceneimg
            player "That sounds like a good idea, Kira. I'd love to meet her and maybe learn more about the town."
            $ position = "kiraleaningtohayoon"
            call sceneimg
            Kira "Perfect. I'll go over and talk to her for a moment, then I'll bring her over to meet you. Just be yourself; you'll get along just fine."
            $ position = "barhayoonhey"
            call sceneimg
            HaYoon "Hi there, I'm HaYoon. Kira tells me you're new in town. Nice to meet you!"
            $ position = "barhayoonwhat"
            call sceneimg
            player "Hi, HaYoon. Yeah, I just moved here recently. It's a pleasure to meet you too. Kira mentioned you work at the clinic. That must keep you pretty busy."
            $ position = "barhayoonexplaining"
            call sceneimg
            HaYoon "It can be, but I love what I do. And it's always nice to unwind with good company. Kira speaks highly of you."
            $ position = "barhayoonwhat"
            call sceneimg
            player "Likewise, HaYoon. I'm looking forward to getting to know the people in this town better."
            $ position = "barhayoonexplaining"
            call sceneimg
            HaYoon "Well, you're off to a good start. If you have any questions about the town or need recommendations, feel free to ask anytime."
            $ position = "barhayoonwhat"
            call sceneimg
            player "Thanks, HaYoon. I'll definitely keep that in mind. It's great to have such welcoming neighbors."
            $ position = "kiraquestion"
            call sceneimg
            Kira "I knew you two would hit it off. Enjoy your chat, and don't hesitate to ask if you need anything else!"



        if myrandom == 3:
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "Hey, remember I mentioned HaYoon sometimes swings by here after her shifts at the hospital?"
            $ position = "kiraquestion"
            call sceneimg
            player "Yeah, you did. That's the doctor you were talking about, right?"
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "The very same. She's sitting at the bar right now. Want me to introduce you?"
            $ position = "kiraquestion"
            call sceneimg
            player "That would be great, Kira. Thanks for offering.But, you know, I don't want to bother her if she's busy or anything."
            $ position = "kiraleaningwhispering"
            call sceneimg
            Kira "Oh, don't worry about that. HaYoon's usually pretty chill when she's here. Let's go over, and I'll make the introduction."
            $ position = "kiraquestion"
            call sceneimg
            player "That sounds good, Kira. Lead the way."
            $ position = "kiraleaningtohayoon"
            call sceneimg
            Kira "HaYoon, meet.This is HaYoon, one of our regulars and an amazing doctor at the hospital."
            $ position = "barhayoonhey"
            call sceneimg
            HaYoon "Nice to meet you. Kira's been telling me you're new in town. How are you finding it so far?"
            $ position = "barhayoonwhat"
            call sceneimg
            player "Pleasure to meet you too, HaYoon. It's been quite an adventure settling in, but everyone's been so welcoming."
            $ position = "barhayoonexplaining"
            call sceneimg
            HaYoon "Well, you've got a fantastic spot here with Kira. She's a gem, always making sure everyone's taken care of."
            $ position = "barhayoonwhat"
            call sceneimg
            player "I can tell. Kira's been great."
            $ position = "kiraflirting"
            call sceneimg
            Kira "Alright, you two, I'll leave you to your conversation. If you need anything, just holler."
            $ position = "barhayoonexplaining"
            call sceneimg
            HaYoon "So, what brings you to our little town?"
            $ position = "barhayoonwhat"
            call sceneimg
            player "Oh, a mix of things, really. New job, new surroundings. I'm also a cook, so I'm looking forward to exploring the local food scene."
            $ position = "barhayoonexplaining"
            call sceneimg
            HaYoon "That sounds intriguing. If you ever need a food critic, count me in. (winks)"
            $ position = "barhayoonwhat"
            call sceneimg
            player "You've got a deal, HaYoon. I might just take you up on that."

    $ usual = 1
    label bar3loop:
        $ position = "kiraquestion2"
        call sceneimg
        menu:
            "Absolutely, Kira. You know me too well" if usual == 1:
                $ usual = 0
                $ kira_calories += 200
                call drinkthank
            "I'm curious to explore the menu a bit. I'll take a look at what else you've got behind that bar" if usual == 1:
                $ usual = 0
                call bardrinks
            "I want to know more about the town" if towninfo == 0:
                $ towninfo = 1
                call kiracitydescription
            "Kira, you must meet all sorts of people here. Who are some of the most fascinating folks in town?" if hayoonintro == 0 or avaintro == 0 or linintro == 0 or sallyintro == 0:
                pass
                call kirapeopledescription
            "Where can I find all these people?" if overallpeople == 1:
                $ position = "kiraexplain"
                call sceneimg
                if hayoonintro == 1:
                    Kira "Well, Ha-Yoon frequents this place quite often, especially during her downtime. So, you're in the right spot to bump into her. "
                if linintro == 1:
                    Kira "Lin, the fitness trainer, usually hangs out at the local gym."
                if avaintro == 1:
                    Kira "Ava, the lifeguard, spends her free time at the beach, of course. "
                if sallyintro == 1:
                    Kira "And Sally, the maid, often visits the park nearby, enjoying some fresh air on her days off."
                    $ sallypark = 1
                $ overallpeople = 2
            "Talk to HaYoon" if hayoonfirstmeet > 0:

                jump hayoonfirstmeet
            "Go home":
                pass
                jump barleaving

             


        

        
        
        jump bar3loop