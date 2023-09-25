label bar3:
    $ myrandom = renpy.random.randint(1,5)

    play music "audio/bar.mp3" volume 0.3
    $ position = "kiraenterance"
    call sceneimg
    player "I walk into the bar, greeted by the warm hum of chatter and clinking glasses."
    $ position = "kiraquestion2"
    call sceneimg
    Kira "Hey there! The usual tonight?"

    $ usual = 1
    label bar3loop:
        $ position = "kiraquestion2"
        call sceneimg
        menu:
            "Absolutely, Kira. You know me too well" if usual == 1:
                $ usual = 0
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
                Kira "Well, Ha-Yoon frequents this place quite often, especially during her downtime. So, you're in the right spot to bump into her. "
                Kira "Lin, the fitness trainer, usually hangs out at the local gym."
                Kira "Ava, the lifeguard, spends her free time at the beach, of course. "
                Kira "And Sally, the maid, often visits the park nearby, enjoying some fresh air on her days off. Just keep your eyes open, and you'll run into them sooner or later. Who knows, you might even make some new friends!"
                $ overallpeople = 2
            "Go home":
                pass
                jump barleaving

             


        

        
        
        jump bar3loop