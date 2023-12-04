label culinarychoices:
    $ calendar.AddMinutes(20)

    $ myrandom = renpy.random.randint(1,10)
    if myrandom == 5 and krisstory < 3:
        jump krisfirstmeet

    play music "audio/campfire.mp3" 
    call closescreens

    $ myrandom = renpy.random.randint(1,10)
    if krisbackyard == 1 and myrandom == 1 and krisnottoday == 0:
        jump krisbackyard


    label cchoicesloop: 
        
        $ position = "backyard"
        call sceneimg
        menu:
            "Go upstairs and look around":
                jump balcony
            "Sleep":
                call dayvariables
            "Go talk to Aurora" if auroraseen == 1:
                jump aurorafirstmeet
            
            
            
        
        


        jump cchoicesloop