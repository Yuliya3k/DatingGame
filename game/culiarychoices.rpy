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
        $ monthworkresulthours += dayworksuccessfulhours
        $ dayworksuccessfulhours = 0
        
        if calendar.Days == 1:
            $ money += monthsalary
            $ monthsalary = 0            
            $ monthworkresulthours = 0
            $ cooksalaryperhour = 23.5*salarystatus
        else:
            pass
        
        
        $ position = "backyard"
        call sceneimg
        menu:
            "Go upstairs and look around":
                jump balcony
            "Sleep":
                call dayvariables
            "Go talk to Aurora" if auroraseen == 1:
                jump aurorafirstmeet
            "Test":
                call hayoonfirstmeet
            
        
        


        jump cchoicesloop